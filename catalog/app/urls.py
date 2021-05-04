from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import HomePageView
from app.views import CarList

app_name = 'app'

urlpatterns = [
	path('', HomePageView.as_view(), name = 'home'),
    path('cars/', CarList.as_view(), name='car_list'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)