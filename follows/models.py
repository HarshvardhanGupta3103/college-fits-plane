from django.db import models
from accounts.models import User

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainer')
