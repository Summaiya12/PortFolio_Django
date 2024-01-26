from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.Index, name="index"),
                  path('service/', views.Service, name="service"),
                  path('portfolio/', views.Portfolio, name="portfolio"),
                  path('contact/', views.Contact, name="contact"),
                  path('cv/', views.cv, name='cv'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
