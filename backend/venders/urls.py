from django.urls import path
from .views import VenderListView, VenderView, TopSellerView


urlpatterns = [
    path('', VenderListView.as_view()), 
    path('topseller', TopSellerView.as_view()), 
    path('<pk>', VenderView.as_view()), 
]
