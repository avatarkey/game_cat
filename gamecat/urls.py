"""gamecat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from gamelist import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^new_game/', views.new_game, name='new_game'),
    url(r'^games/(?P<name>.*)/$', views.game_profile, name='game_profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', views.profile, name='account_profile'),
    url(r'^accounts/(?P<username>[-\w]+)/$', views.all_profiles, name='profile'),
    url(r'^wiki/$', views.wiki_test, name="wiki")
    #url(r'^games/add_game/', views.add_game, name='add_game'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
