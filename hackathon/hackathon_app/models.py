from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to="hackathon/backgrounds")
    hackathon_image = models.ImageField(upload_to="hackathon/images")
    submission_type = models.CharField(
        choices=(("image", "Image"), ("file", "File"), ("link", "Link")), max_length=10
    )
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User, through="HackathonRegistration")


class HackathonRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Submission(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    submission_type = models.CharField(
        choices=(("image", "Image"), ("file", "File"), ("link", "Link")), max_length=10
    )
    submission_file = models.FileField(upload_to="submissions", blank=True, null=True)
    submission_link = models.URLField(blank=True, null=True)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through="UserSubmission")
    created_at = models.DateTimeField(auto_now_add=True)


class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
