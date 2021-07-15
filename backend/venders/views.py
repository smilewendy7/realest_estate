from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions 
from .models import Vender
from .serializers import VenderSerializer
# Create your views here.

class VenderListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset  = Vender.objects.all()
    serializer_class = VenderSerializer
    ### 不分页
    pagination_class = None

### use the id to retrive the vender 
class VenderView(RetrieveAPIView):
    queryset = Vender.objects.all()
    serializer_class = VenderSerializer
    ### return a singal object

class TopSellerView(ListAPIView): 
    ### return a singal object
    permission_classes = (permissions.AllowAny, )
    queryset  = Vender.objects.filter(top_seller=True)
    serializer_class = VenderSerializer
    pagination_class = None
