from django.urls import path
# from . import views
from .views import *
from . import views
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView


urlpatterns = [
    path('', views.Home, name='Home'),
    path('sign-in/', views.SignIn, name='sign-in'),
    path('sign-up/', views.SignUp, name='sign-up'),
    path('logout/', views.LogOut, name='logout'),

    path('blogs/', views.BlogsView, name='blogs'),
    path('blog/<str:pk>/', views.BlogView, name='blog'),
    path('delete-message/blog/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('delete-comment/usefull/<str:pk>/', views.deleteMessageUsefull, name='delete-comment'),

    path('usefulls/', views.UsefullsView, name='usefulls'),
    path('usefull/<str:pk>/', views.UsefullView, name='usefull'),

    path('visas/', views.VisasViews, name='visas'),

    path('like/<int:pk>/', like_blog, name='like_blog'),

    path('likes/', views.likesView, name='likes'),
    path('profile/', views.userProfile, name='profile'),

    path('like-u/<int:pk>/', like_usefull, name='like_usefull'),

    path('termsof_services_privacy_policy/', views.termsPrivasy, name='termsof_services_privacy_policy'),

    path('successfully/', views.succesN, name='successfully'),

    path('<path:path>/', TemplateView.as_view(template_name='Home/404.html'), name='custom_404'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)