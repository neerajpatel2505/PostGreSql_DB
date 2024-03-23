from django.shortcuts import render
from django.http import HttpResponse
from .models import DataStore

# Create your views here.
def home(request):
    return render(request,'home.html')


def regeister(request):
    if request.method=="POST":
        firstName=request.POST['fname']
        lastName=request.POST['lname']  
        quali=request.POST['quali']
        dob = request.POST['dob']
        age = request.POST['age']
        language = request.POST.getlist("language[]")
        # print("firstName=",firstName)
        # print("lirstName=",lastName)
        # print("Qualification=",Quali)
        # print("Date of Birth=",dob)
        # print("age=",age)
        # print("languages known :",language)
        DataStore.objects.create(
            First_Name=firstName,
            Last_Name=lastName,
            Age=age,
            Qualification=quali,
            DOB=dob,
            Language_Known=language)
        return render(request,'register.html')
        # data={
        #     'fname':firstName,
        #     'lname':lastName,
        #     'quali':Quali,
        #     'age':age,
        #     'dob':dob,
        #     'language':language
        # }
        # return render(request,'app/register.html',{'data':data})
    
    return HttpResponse("You send a GET mehtod with request")

def data(request):
    all_stu = DataStore.objects.all()
    # print(all_stu)
    students = all_stu.values()
    # print(students)
    return render(request,'all_data.html',{'data':students})

def login(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        user = DataStore.objects.get(First_Name=fname)
        print(user.First_Name)
        print(user.Last_Name)
        print(user.Age)
        print(user.Qualification)
        print(user.DOB)
        print(user.Language_Known)