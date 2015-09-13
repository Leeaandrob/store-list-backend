from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from homesite.views import HomeSiteView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('api.urls')),
    url(r'^$', HomeSiteView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
