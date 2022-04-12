from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomePage'),
    path('<int:pk>',views.CandidateView.as_view(), name='candidate'),
    path('contact/', views.ContactView.as_view(), name='ContactUs')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

