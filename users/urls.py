from django.urls import path , include
from .views import RegisterView
from django.contrib.auth import views as auth_views
from rest_framework import routers
import users.views
##Wiring API using automatic URL routing
# Additional we include login URLs for the browsable API
router = routers.DefaultRouter()
router.register(r'users', users.views.UserViewSet)
router.register(r'groups', users.views.GroupViewSet)


urlpatterns = [ 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login" ),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
    path('api-path/', include('rest_framework.urls', namespace='rest_framework')),
]





