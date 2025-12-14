from django.db import models
from accounts.models import User

class FitnessPlan(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()  # in days

    def __str__(self):
        return self.title
