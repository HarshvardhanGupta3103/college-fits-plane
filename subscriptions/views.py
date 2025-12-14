from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Subscription
from plans.models import FitnessPlan

@login_required
def subscribe(request, plan_id):
    plan = FitnessPlan.objects.get(id=plan_id)
    Subscription.objects.get_or_create(user=request.user, plan=plan)
    return redirect('user_feed')
