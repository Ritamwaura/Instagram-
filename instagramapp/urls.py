from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import re_path

from .views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^register/', signup, name='signup'),
    re_path('account/', include('django.contrib.auth.urls')),
    re_path('^profile/<username>/', profile, name='profile'),
    re_path('^user_profile/<username>/', user_profile, name='user_profile'),
    re_path('^post/<id>', post_comment, name='comment'),
    re_path('^like', like_post, name='like_post'),
    re_path('^search/', search_profile, name='search'),
    re_path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
