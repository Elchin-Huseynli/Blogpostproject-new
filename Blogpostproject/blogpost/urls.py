from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import homepage, post, about, search, postlist, allposts,user,postlistauthor,post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('search/', search, name = 'search'),
    path('postlist/<slug>/', postlist, name = 'postlist'), 
    path('posts/', allposts, name = 'allposts'),
    path('user/', user, name = 'user'),
    path('author/<author_id>/', postlistauthor, name = 'postlistauthor'),
    path('tag/<slug:tag_slug>/',post_list, name='post_tag'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
