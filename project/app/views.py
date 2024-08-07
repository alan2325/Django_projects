from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

### httpresponse(message)
def fun1(request):
    return HttpResponse("Welcome")
def fun2(request):
    return HttpResponse("helo")


### print 2 numbers from user input
def fun3(request,a,b):
    return HttpResponse(str(a)+'   '+b)


### gratest out of 2 numbers
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
   

### salary bonus 5%
def emp(request,year,sal):
    
    if year>5:
        return HttpResponse("Your salary '"+str(sal)+"' increased by 5% , Bonus : "+str(sal*1.05))
    else:
        return HttpResponse("You are not eligible !")
    

### Electricity bill
def bill(request,unit):
    if unit<=100:
        return HttpResponse("Electricity bill for "+str(unit)+" unit is free !")
    elif unit<+200:
        return HttpResponse("Electricity bill for "+str(unit)+" unit  is : "+str((unit-100)*5))
    elif unit>200:
        return HttpResponse("Electricity bill for "+str(unit)+" unit  is : "+str((unit-200)*10+500))
    


### print day
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



### display monument of city
def city(request,city):
    if city=='delhi':
        return HttpResponse("Monument of "+str(city)+" is Red Fort")
    elif city=='agra':
        return HttpResponse("Monument of "+str(city)+" is Taj Mahal") 
    elif city=='jaipur':
        return HttpResponse("Monument of "+str(city)+" is Jai Mahal") 
    else:
        return HttpResponse("Invalid input !")
    


### tax
def tax(request,costprice):
    if costprice > 100000:
        return HttpResponse("Tax is : " +str(0.15 * costprice))
    elif costprice > 50000:
            return HttpResponse("Tax is : " +str(0.10 * costprice))
    else:
            return HttpResponse("Tax is : " +str(0.05 * costprice))



### last number divisible by 3
def div(request,num):
    last_digit = num % 10
    if last_digit % 3 == 0:
        return HttpResponse("The last digit of the number is divisible by three.")
    else:
        return HttpResponse("The last digit of the number is not divisible by three.")    
                



### link html page
def html(reg):
    return render(reg,'index.html')