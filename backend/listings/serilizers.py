from rest_framework import serializers
from .models import Listing 

class ListingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Listing 
        fields = ('title', 'address', 'city', 'province', 'price', 'sale_type', 'ticket_type',
                  'photo_main', 'slug',
        )


class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing 
        fields = '__all__'
        lookup_field = 'slug'
