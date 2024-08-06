from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun1(request):
    return HttpResponse("Welcome")

def fun2(request):
    return HttpResponse("helo")

def fun3(request,a,b):
    return HttpResponse(str(a)+'   '+b)

def fun4(request,a,b):
    if a>b:
        print("A is grater than B")
        return HttpResponse(str(a)+" is grater than  "+str(b))
    elif a==b:
        print("A = B")
        return HttpResponse(str(a)+" equal to "+str(b))
    else:
        print("B is grater than A")
        return HttpResponse(str(b)+" is grater than "+str(a))
   

def emp(request,year,sal):
    
    if year>5:
        return HttpResponse("Your salary '"+str(sal)+"' increased by 5% , Bonus : "+str(sal*1.05))
    else:
        return HttpResponse("You are not eligible !")
    
def bill(request,unit):
    if unit<=100:
        return HttpResponse("Electricity bill for "+str(unit)+" unit is free !")
    elif unit<+200:
        return HttpResponse("Electricity bill for "+str(unit)+" unit  is : "+str((unit-100)*5))
    elif unit>200:
        return HttpResponse("Electricity bill for "+str(unit)+" unit  is : "+str((unit-200)*10+500))
    
def day(request,day):
    if day==1:
        return HttpResponse("Sunday")
    elif day==2:
        return HttpResponse("Monday")   
    elif day==3:
        return HttpResponse("Tuesday")
    elif day==4:
        return HttpResponse("Wednesday")
    elif day==5:
        return HttpResponse("Thursday")
    elif day==6:
        return HttpResponse("Friday")
    elif day==7:
        return HttpResponse("Saturday")
    else:
        return HttpResponse("Invalid input !")
    
def city(request,city):
    if city=='delhi':
        return HttpResponse("Monument of "+str(city)+" is Red Fort")
    elif city=='agra':
        return HttpResponse("Monument of "+str(city)+" is Taj Mahal") 
    elif city=='jaipur':
        return HttpResponse("Monument of "+str(city)+" is Jai Mahal") 
    else:
        return HttpResponse("Invalid input !")