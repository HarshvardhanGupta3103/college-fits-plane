from django.shortcuts import render
from plans.models import FitnessPlan
from subscriptions.models import Subscription


def home(request):
    plans = FitnessPlan.objects.all()
    subscribed_plans = []
    if request.user.is_authenticated:
        subscribed_plans = Subscription.objects.filter(user=request.user).values_list('plan_id', flat=True)
    return render(request, 'index.html', {'plans': plans, 'subscribed_plans': subscribed_plans})
