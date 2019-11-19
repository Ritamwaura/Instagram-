from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
    path('user_profile/<username>/', user_profile, name='user_profile'),
    path('post/<int:id>', post_comment, name='comment'),
    path('like', like_post, name='like_post'),
    path('search/', search_profile, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    # path('comment/<id>',post_comment, name='comment'),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
