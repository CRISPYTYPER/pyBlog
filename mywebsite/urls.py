from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mywebsite.views import HomeView
from mywebsite.views import UserCreateView, UserCreateDoneTV

# from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/register/', UserCreateView.as_view(), name='register'),
                  path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
                  path('', HomeView.as_view(), name='home'),
                  path('bookmark/', include('bookmark.urls')),
                  path('blog/', include('blog.urls')),
                  path('photo/', include('photo.urls')),

                  # class-based views
                  # path('bookmark/', BookmarkLV.as_view(), name='index'),
                  # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
