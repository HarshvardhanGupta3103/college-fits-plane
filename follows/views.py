from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Follow
from plans.models import FitnessPlan
from subscriptions.models import Subscription

@login_required
def follow_trainer(request, trainer_id):
    Follow.objects.get_or_create(user=request.user, trainer_id=trainer_id)
    return redirect('user_feed')

@login_required
def unfollow_trainer(request, trainer_id):
    Follow.objects.filter(user=request.user, trainer_id=trainer_id).delete()
    return redirect('user_feed')

@login_required
def user_feed(request):
    followed_trainers = Follow.objects.filter(user=request.user).values_list('trainer', flat=True)
    plans = FitnessPlan.objects.filter(trainer__in=followed_trainers)
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'plans/user_feed.html', {'plans': plans, 'subscriptions': subscriptions})
