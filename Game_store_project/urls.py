from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('Game_store_project.game_store.urls')),
                  path('authentication/', include('Game_store_project.auth_app.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)