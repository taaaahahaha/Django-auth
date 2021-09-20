from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signin(request):

    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)


        if user is not None:
            login(request, user)
            address = user.first_name
            email = user.email
            context={
                'username':username,
                'address':address,
                'email':email,
                'flag':True
            }
            return render(request,"details.html",context)
            # return HttpResponse("Logged")
        
        else:
            # return redirect("/")
            # return HttpResponse("Not an user")
            context={
                'username':username,
                "flag":False
            }
            return render(request,"details.html",context)

    return render(request, "signin.html")

def about(request):
    return render(request, "about.html")

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        address = request.POST['address']

        if pass1 != pass2:
            return HttpResponse("Please input same passwords.")

        if username=='taaha':
            return HttpResponse("Sorry, a superuser is using that username, try another one") # /admin > id =' taaha' pass = 'taaha25'
        
        try:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = address #used first_name as address

            myuser.save()

            return redirect("/")
        except:
            return HttpResponse('That Username is already taken.')

        # return HttpResponse("Hello there")

    return render(request,"signup.html")

def details(request):
    return render(request,"details.html",)

def logout_view(request):
    logout(request)
    return redirect('/')

def editpass(request,username):
    
    if request.method=='POST':
        pass1 = request.POST['pass1']
        u = User.objects.get(username=username)
        u.set_password(pass1)
        u.save()
        return redirect('signin')
    
    return render(request,'editpassword.html',{'username':username})
    
def edituname(request,username):
    
    if request.method=='POST':
        new_username = request.POST['username']
        u = User.objects.get(username=username)
        u.username = new_username
        u.save()
        return redirect('signin')
    
    return render(request,'editusername.html',{'username':username})

def editadd(request,username):
    
    if request.method=='POST':
        new_address = request.POST['address']
        u = User.objects.get(username=username)
        u.first_name = new_address
        u.save()
        return redirect('signin')
    
    return render(request,'editaddress.html',{'username':username})

def editemail(request,username):
    print(username)
    
    if request.method=='POST':
        new_email = request.POST['email']
        u = User.objects.get(username=username)
        u.email = new_email
        u.save()
        return redirect('signin')
    
    return render(request,'editemail.html',{'username':username})


def delete(request,username):
    u = User.objects.get(username=username)
    u.delete()
    
    return redirect('signin')


