from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from users.serializers import GroupSerializer, UserSerializer
from django.contrib.auth import login
from .forms import UserRegisterForm
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()         # save user
            login(request, user)       # log in the user immediately
            return redirect('index')   # redirect to signed-in index
        return render(request, 'users/register.html', {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
