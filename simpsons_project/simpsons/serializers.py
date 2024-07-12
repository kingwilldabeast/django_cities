from rest_framework import serializers
from .models import City, Attraction, Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )

    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        source='attraction'
    )

    class Meta:
        model = Review
        fields = ('id', 'attraction', 'attraction_id', 'title', 'description', 'photo_url')

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )

    reviews = ReviewSerializer(
        # view_name='review',
        many=True,
        read_only=True
    )

    class Meta:
        model = Attraction
        fields = ('id', 'city', 'city_id', 'name', 'price', 'photo_url', 'reviews')
        
        
class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        # view_name='attraction',
        many=True,
        read_only=True
    )

    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
    )

    class Meta:
       model = City
       fields = ('id', 'city_url', 'name', 'population', 'photo_url', 'attractions')
