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
def html(req):
    return render(req,'index.html')
### & passing data into a html page
def html2(req):
    a="Hai"
    b=[1,2,3,4]
    c={'name':'bla'}
    return render(req,'home.html',{'d1':a,'d2':b,'d3':c})


### student mark

def std(req):
    student=[{'name':'aa','age':22,'mark':44},
         {'name':'bb','age':23,'mark':55},
         {'name':'cc','age':24,'mark':66},
         {'name':'dd','age':25,'mark':77},
         {'name':'ee','age':26,'mark':38},]
    return render(req,'std.html',{'std':student})

def above(req):
    student=[{'name':'aa','age':22,'mark':44},
         {'name':'bb','age':23,'mark':55},
         {'name':'cc','age':24,'mark':66},
         {'name':'dd','age':25,'mark':77},
         {'name':'ee','age':26,'mark':38},]
    above_std = [] 
    for i in student:
        if i["mark"] >50:
            above_std.append(i)   
    return render(req,'above.html',{'std':above_std})

def below(req):
    student = [{'name': 'aa', 'age': 22, 'mark': 44},
        {'name': 'bb', 'age': 23, 'mark': 55},
        {'name': 'cc', 'age': 24, 'mark': 66},
        {'name': 'dd', 'age': 25, 'mark': 77},
        {'name': 'ee', 'age': 26, 'mark': 38},]
    below_std = []
    for i in student:
        if i["mark"] < 50:
            below_std.append(i)
    return render(req, 'below.html', {'std': below_std})


### new template
def view(req):
    return render(req,'static.html')
