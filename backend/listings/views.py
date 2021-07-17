from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions, serializers

from .models import Listing
from .serilizers import ListingSerilizer, listingDetailSerializer
from datetime import datetime, timezone, timedelta 

# Create your views here.

class ListingsView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    permissions_classes = (permissions.AllowAny, )
    serializer_class =  ListingSerilizer
    lookup_field = 'slug'

class ListingView(RetrieveAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = listingDetailSerializer
    lookup_field = 'slug'


### search  no bathroom, bedroom, sqft 
class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerilizer

    def post(self, request, format=None):
        queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)

        price = data['price']
        if price == '$0+':
            price = 0
        elif price == "$50+":
            price = 50
        elif price == "$100+":
            price = 100
        elif price == "$150+":
            price = 150
        elif price == "$200+":
            price = 200
        elif price == "$250+":
            price = 250
        elif price == "$300+":
            price = 300
        elif price == "$350+":
            price = 350
        
        elif price =="Any":
            price = -1

        if price != -1:
            queryset = queryset.filter(price__gre=price)

        
        ticket_type = data['ticket_type']
        queryset = queryset.filter(ticket_type__iexact=ticket_type)


        days_passed = data['days_listed']
        if days_passed == '1 or less':
            days_passed = 1 

        if days_passed == '2 or less':
            days_passed = 2 

        if days_passed == '5 or less':
            days_passed = 5 

        if days_passed == '10 or less':
            days_passed = 10

        if days_passed == '20 or less':
            days_passed = 20

        if days_passed == 'Any':
            days_passed = 0
        
        for query in queryset:
            num_days = (datetime.now(timezone.utc) - query.list_date).days

            if days_passed != 0:
                if num_days > days_passed:
                    slug=query.slug 
                    queryset = queryset.exclude(slug__iexact=slug)
        
        has_photos = data['has_photos']
        if has_photos == '1+':
            has_photos = 1 
        


