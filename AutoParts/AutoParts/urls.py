from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AutoParts.common.urls')),
    path('account/', include('AutoParts.accounts.urls')),
    path('parts/', include('AutoParts.parts.urls')),
    path('cart/', include('AutoParts.store.urls')),
    path('accounts/', include('AutoParts.account_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
