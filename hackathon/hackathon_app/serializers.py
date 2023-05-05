from rest_framework import serializers
from .models import Hackathon, HackathonRegistration, Submission


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = "__all__"


class HackathonRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonRegistration
        fields = "__all__"


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
