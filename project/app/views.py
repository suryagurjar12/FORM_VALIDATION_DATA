from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm,QueryForm
from .models import StudentModel,StudentQuery
# Create your views here.

def home(request):
    form=RegistrationForm()
    if request.method=="POST":      
        form=RegistrationForm(request.POST)
    
        if form.is_valid():
            stu_name=form.cleaned_data["stu_name"]
            stu_email=form.cleaned_data["stu_email"]
            stu_city=form.cleaned_data["stu_city"]
            stu_mobile=form.cleaned_data["stu_mobile"]
            stu_password=form.cleaned_data["stu_password"]
            print(stu_name,stu_email,stu_city,stu_mobile)
            user = StudentModel.objects.filter(stu_email=stu_email)
            if user:
                msg = "Email already exit"
                form = RegistrationForm()
                return render(request,"home.html",{"form":form,"msg":msg})
            else:
                form.save()
                msg="Registration succesfull"
                form=RegistrationForm()
                return render(request,"home.html",{"form":form,"msg":msg})
            
    else:
        return render(request,'home.html',{"form":form})

def login(request):
    form = LoginForm()
    if request.method=="POST":
        data = LoginForm(request.POST)
        if data.is_valid():
            email = data.cleaned_data['stu_email']
            password = data.cleaned_data['stu_password']
            # print(email,password)
            user = StudentModel.objects.filter(stu_email=email)
            
            if user:
                user = StudentModel.objects.get(stu_email=email)
                # print(user.stu_password)
                if user.stu_password==password:
                    name = user.stu_name
                    email = user.stu_email
                    contact = user.stu_mobile
                    city = user.stu_city
                    password = user.stu_password
                    data = {
                        'name':name,
                        'email':email,
                        'contact':contact,
                        'city':city,
                        'password':password
                    }
                    initial_data = {
                                    'stu_name': name,
                                    'stu_email': email
                                } 
                    form1=QueryForm(initial=initial_data)
                    data1=StudentQuery.objects.filter(stu_email=email)
                    return render(request,'dashboard.html',{'data':data,'query':form1,'data1':data1})
                else:
                    msg = "Email & Password not matched"
                    return render(request,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(request,'login.html',{'form':form,'msg':msg})
    else:
        return render(request,'login.html',{'form':form})
    
def query(request):
    # return HttpResponse("hi.............")
    form = QueryForm()
    if request.method=="POST":
        query_data = QueryForm(request.POST) 
        # print(query_data)
        if query_data.is_valid():
            name =  query_data.cleaned_data['stu_name']
            email = query_data.cleaned_data['stu_email']
            query = query_data.cleaned_data['stu_query']
            # print(email,name,query)
            query_data.save()
            user = StudentModel.objects.get(stu_email=email)
            if user:
                name = user.stu_name
                email = user.stu_email
                contact = user.stu_mobile
                city = user.stu_city
                password = user.stu_password
                data = {
                    'name':name,
                    'email':email,
                    'contact':contact,
                    'city':city,
                    'password':password
                }
                initial_data = {
                                'stu_name': name,
                                'stu_email': email
                            } 
                form1=QueryForm(initial=initial_data)
                data1=StudentQuery.objects.filter(stu_email=email)
                return render(request,'dashboard.html',{'data':data,'query':form1,'data1':data1})
def delete(request,pk):
    form=QueryForm()
    if request.method=="POST":
        user=StudentQuery.objects.get(id=pk)
        name =  user.stu_name
        email = user.stu_email
        user.delete()
        initial_data = {
            'stu-name':name,
            'stu_email':email,
        }
        data1=StudentQuery.objects.filter(stu_email=email)
        form1=QueryForm(initial=initial_data)
        user = StudentModel.objects.get(stu_email=email)
        name = user.stu_name
        email = user.stu_email
        contact = user.stu_mobile
        city = user.stu_city
        password = user.stu_password
        data = {
                    'name':name,
                    'email':email,
                    'contact':contact,
                    'city':city,
                    'password':password
                }
        return render(request,'dashboard.html',{'data':data,'query':form1,'data1':data1})
        
def update(request,pk):
    form=QueryForm()
    if request.method=="POST":
        user=StudentQuery.objects.get(id=pk)
        name =  user.stu_name
        email = user.stu_email
        query= user.stu_query
        id=pk
        user.delete()
        initial_data = {
            'stu_name':name,
            'stu_email':email,
            'stu_query':query
        }
        data1=StudentQuery.objects.filter(stu_email=email)
        form1=QueryForm(initial=initial_data)
        user = StudentModel.objects.get(stu_email=email)
        name = user.stu_name
        email = user.stu_email
        contact = user.stu_mobile
        city = user.stu_city
        password = user.stu_password
        data = {
                    'name':name,
                    'email':email,
                    'contact':contact,
                    'city':city,
                    'password':password
                }
        return render(request,'dashboard.html',{'data':data,'form1':form1,'data1':data1})  
        
def edit(request,pk):
    print(pk)        