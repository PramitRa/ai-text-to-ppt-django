from django.contrib import admin
from django.urls import path
from presentation import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('form/', views.show_form, name='show_form'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)