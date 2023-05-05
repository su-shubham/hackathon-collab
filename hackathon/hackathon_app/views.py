from rest_framework import generics
from .models import Hackathon, HackathonRegistration, Submission
from .serializers import (
    HackathonSerializer,
    SubmissionSerializer,
    HackathonRegistrationSerializer,
)


class HackathonList(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


class HackathonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


class SubmissionList(generics.ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class HackathonRegistrationCreate(generics.CreateAPIView):
    queryset = HackathonRegistration.objects.all()
    serializer_class = HackathonRegistrationSerializer


class UserHackathonList(generics.ListAPIView):
    serializer_class = HackathonSerializer

    def get_queryset(self):
        return Hackathon.objects.filter(users=self.request.user)


class UserSubmissionList(generics.ListAPIView):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects.filter(users=self.request.user)
