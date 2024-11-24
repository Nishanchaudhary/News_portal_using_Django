from django.contrib import admin
from django.urls import path
from newsApp import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static
context = views.context_data()
urlpatterns = [
    path('', views.home, name="home-page"),
    path('login/',auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user = True,extra_context = context),name='login-page'),
    path('logout/',views.logoutuser,name='logout'),
    path('userlogin/', views.login_user, name="login-user"),
    path('profile/', views.profile, name="profile-page"),
    path('update_profile/', views.update_profile, name="update-profile"),
    path('update_password/', views.update_password, name="update-password"),
    path('new_post/', views.manage_post, name="new-post"),
    path('edit_post/<int:pk>', views.manage_post, name="edit-post"),
    path('save_post/', views.save_post, name="save-post"),
    path('post/<int:pk>', views.view_post, name="view-post"),
    path('save_comment/', views.save_comment, name="save-comment"),
    path('posts/', views.list_posts, name="all-posts"),
    path('category/<int:pk>', views.category_posts, name="category-post"),
    path('delete_post/<int:pk>', views.delete_post, name="delete-post"),
    path('delete_comment/<int:pk>', views.delete_comment, name="delete-comment"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)