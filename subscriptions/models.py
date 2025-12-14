from django.db import models
from accounts.models import User
from plans.models import FitnessPlan

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(FitnessPlan, on_delete=models.CASCADE)
