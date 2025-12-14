from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FitnessPlan
from subscriptions.models import Subscription

@login_required
def trainer_dashboard(request):
    if not request.user.is_trainer:
        return redirect('home')
    plans = FitnessPlan.objects.filter(trainer=request.user)
    if request.method == 'POST':
        FitnessPlan.objects.create(
            trainer=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            price=request.POST['price'],
            duration=request.POST['duration']
        )
        return redirect('trainer_dashboard')
    return render(request, 'plans/trainer_dashboard.html', {'plans': plans})

@login_required
def plan_detail(request, id):
    plan = FitnessPlan.objects.get(id=id)
    subscribed = Subscription.objects.filter(user=request.user, plan=plan).exists()
    return render(request, 'plans/plan_detail.html', {'plan': plan, 'subscribed': subscribed})
