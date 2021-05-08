from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import math
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def getMealRate():
    meals = Meal.objects.all()
    totalMeals = 0
    for meal in meals:
        totalMeals += meal.poriman
    
    totalCost = 0
    sobkhoroch = Khoroch.objects.all()
    for khoroch in sobkhoroch:
        totalCost += khoroch.poriman

    mealRate = math.ceil(totalCost/totalMeals)
    return mealRate

def home(request):
    meals = Meal.objects.all()
    totalMeals = 0
    for meal in meals:
        totalMeals += meal.poriman
    
    totalCost = 0
    sobkhoroch = Khoroch.objects.all()
    for khoroch in sobkhoroch:
        totalCost += khoroch.poriman

    mealRate = math.ceil(totalCost/totalMeals)
    totalDeposit = 0
    members = Member.objects.all()
    for member in members:
        totalDeposit += member.joma
    
    totalDeposit = int(totalDeposit)
    members = Member.objects.all()

    context = {'totalMeals':totalMeals,'totalCost':totalCost,'mealRate':mealRate,'totalDeposit':totalDeposit,'members':members}

    return render(request, 'mealcounts/dashboard.html',context)

def user(request,pk):
    user = Member.objects.get(id=pk)
    totalMeal = 0
    meals = user.meal_set.all()
    for meal in meals:
        totalMeal += meal.poriman

    mealRate = getMealRate()
    deposit = user.joma

    totalCost = mealRate * totalMeal
    delta = deposit - totalCost

    context = {'user':user,'totalMeal':totalMeal, 'mealRate':mealRate, 'deposit':deposit, 'totalCost':totalCost, 'delta':delta}

    return render(request, 'mealcounts/user.html', context)

@login_required(login_url='login')
def edit(request):
    members = Member.objects.all()
    if request.method == 'POST':
        din = request.POST.get('din')
        tarikh = Tarikh.objects.get(din=din)
        for ele in request.POST:
            if ele == 'din' or ele == 'csrfmiddlewaretoken':
                continue
            member = Member.objects.get(id=ele)
            poriman = request.POST.get(ele)
            meal = Meal(tarikh=tarikh, member=member,poriman=poriman)
            print(meal)
            meal.save()
        return redirect('home')

    context = {'members':members}

    return render(request,'mealcounts/edit.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')

    context = {}

    return render(request,'mealcounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')