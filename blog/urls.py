from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import Index , DetailArticleView , LikeArticle, Featured, DeletePostView, CategoryView, ImageView , CategoryViewSet, ArticleViewSet
#URL import for REST_API
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>/', DetailArticleView.as_view(), name="detail_article"),
    path('<int:pk>/like', LikeArticle.as_view(), name="like_article"),
    path('<int:pk>/delete', DeletePostView.as_view(), name="delete_article"),
    path('category/<slug:slug>/', CategoryView.as_view(), name="category_detail"),
    path('featured/', Featured.as_view(), name="featured"),
    path('upload/', ImageView.image_upload, name='image_upload'),
    path('', include(router.urls)),
    path('article/<int:pk>/', DetailArticleView.as_view(), name='article_detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)