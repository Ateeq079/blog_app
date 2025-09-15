from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.conf import settings
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from .forms import ImageUploadForm , CommentForm
from .models import Article, Category , ImageModel
from .serializers import CategorySerializer
#from rest_framework import
from rest_framework import permissions, viewsets
# Create your views here.

class Index(ListView):
    model = Article
    queryset  = Article.objects.all().order_by('-created_date')
    template_name = 'blog/index.html'
    paginate_by = 2


class Featured(ListView):
    model = Article
    queryset  = Article.objects.filter(featured = True).order_by('-created_date')
    template_name = 'blog/featured.html'
    paginate_by = 2

#Category View
class CategoryView(View):
    def get(self , request, slug):
        category = get_object_or_404(Category, slug=slug)
        articles = Article.objects.filter(categories=category)
        return render(request, "blog/category_detail.html", {"category": category, "articles": articles})

#Writing CategoryView REST API_VIEW
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DetailArticleView(DetailView):
    model = Article
    template_name = "blog/blog_post.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)

        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        context['comments'] = article.comments.all().order_by('date_posted')
        if article.likes.filter(pk=self.request.user.id).exists():
             context['liked_by_user'] = True
        if 'form' not in context:
            context['form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect(self.get_success_url())
        return self.form_inavlid(form)

class LikeArticle(View):
    def post(self , request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        article.save()
        return redirect('detail_article', pk)
        
class ImageView(View):
    def image_upload(request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = ImageUploadForm()

        images = ImageModel.objects.all()
        return render(request, 'blog/upload.html', {'form': form , 'images': images})


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')
    def test_func(self):
        article = Article.objects.get(id=self.kwargs.get("pk"))
        return self.request.user.id == article.author.id

#View For Comments 
