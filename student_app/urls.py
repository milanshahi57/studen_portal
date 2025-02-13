from django.urls import path,include
from . import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static
from .views import notice_list
from .views import contact_view


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('about/',views.about, name='about'),
    path('year/',views.year, name='year'),
    # path('contact/',views.contact, name='contact'),
    path('subjects/<str:year>/', views.subjects, name='subjects'),
    path('notices/', notice_list, name='notice_list'),
     path('contact/', views.contact_view, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

