from django.contrib import admin
from django.urls import path, include
from posts.views import index, blog, post, last_post, contact #PAMIETAJMY, ZE VIEWS IMPORTUJE Z apki - posts!!!
from registration.views import registration_form, login_form, logout_form #user tu jest do wywalenia
#mogloby by rowniez from post import views, i wtedy w urlpatterns:     path('blog/', views.blog, name='post-list'),
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('blog/', blog, name='post-list'),
    path('post/<slug:slug>/', post, name='post-detail'),
    path('post/', last_post),
    path('contact/', contact),
    path('register/', registration_form),
    path('login/', login_form),
    # path('logout/', logout_form),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('logout/', logout_form),

    path('social-auth/', include('social_django.urls', namespace="social")),

]

# urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print("urlpatterns: ", urlpatterns)
