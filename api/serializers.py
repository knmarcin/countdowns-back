from rest_framework import serializers
from api.models import Countdown


class CountdownsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countdown
        fields = ('id','title', 'date')