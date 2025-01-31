from django.urls import path,include
from . import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('about/',views.about, name='about'),
    path('year/',views.year,name='year'),
    path('subjects/<str:year>/', views.subjects, name='subjects'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

