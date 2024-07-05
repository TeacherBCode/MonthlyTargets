from django.shortcuts import render
import random

# Create your views here.

months = [ 
    {'id': '1', 'month': 'January', 'target': 'Do walking 3kms everyday.'},
    {'id': '2', 'month': 'February', 'target': 'Do walking 4kms everyday.'},
    {'id': '3', 'month': 'March', 'target': 'Do 1 Vid and upload everyday'},
    {'id': '4', 'month': 'April', 'target': 'Partice Archery for 20 mins everyday'},
    {'id': '5', 'month': 'May', 'target': 'Do walking 3kms everyday.'},
    {'id': '6', 'month': 'June', 'target': 'Partice Archery for 30 mins everyday'},
    {'id': '7', 'month': 'July', 'target': 'Partice Archery for 60 mins everyday'},
    {'id': '8', 'month': 'August', 'target': 'Do walking 5kms everyday.'},
    {'id': '9', 'month': 'September', 'target': 'Do walking 6kms everyday.'},
    {'id': '10', 'month': 'October', 'target': 'Upload 1 vid everyday'},
    {'id': '11', 'month': 'November', 'target': 'Do archery for 60 mins everyday.'},
    {'id': '12', 'month': 'December', 'target': 'Do walking 7kms everyday.'},
]

def home(request):
    return render(request, 'months/home.html', {'months': months} )

def target(request,id):
    randomNum =  random.randint(1,12)
    targetMonth = None
    for month in months:
        if month['id'] == str(randomNum):
            targetMonth = month
    return render(request, 'months/target.html', {'month': targetMonth})