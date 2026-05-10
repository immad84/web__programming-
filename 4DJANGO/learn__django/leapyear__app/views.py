from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
     currentyear = datetime.now().year
     isleapyear = (currentyear % 4 == 0 and currentyear % 100 != 0) or (currentyear % 400 == 0)
     return render(request, "leapyear__app/index.html", {"isleapyear": isleapyear})

def isLeap(request, year):
     currentyear = int(year)
     isleapyear = (currentyear % 4 == 0 and currentyear % 100 != 0) or (currentyear % 400 == 0)
     return render(request, "leapyear__app/index.html", {"isleapyear": isleapyear})
