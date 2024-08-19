from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
def home(request):
    galarys=Galary.objects.all()
    context={"galarys":galarys}
    return render(request,'home.html',context)


def Products(request):
    galarys=Galary.objects.all()
    products=Product.objects.all()
    catagorys=Catagory.objects.all()
    context={"products":products,"catagorys":catagorys,"galarys":galarys}

    return render(request,'products.html',context)


def About(request):
    galarys=Galary.objects.all()
    context={"galarys":galarys}
    return render(request,'about.html',context)

def Contact(request):
    if request.method=="POST":
      #  print("\n\n --------------------- POST ---------------------- \n\n")
        form =MSGForm(request.POST)
        if form.is_valid():
            form.save()
            galarys=Galary.objects.all()
            context={"galarys":galarys}
            messages.success(request,"تم ارسال رسالتك بنجاح",extra_tags="success")
            return render(request,'contact.html',context)
        else:
            galarys=Galary.objects.all()
            context={"galarys":galarys}
            messages.error(request,"حدث خطا تاكد من المعلومات",extra_tags="danger")
            return render(request,'contact.html',context)
    galarys=Galary.objects.all()
    context={"galarys":galarys}
    return render(request,'contact.html',context)


def Gallery(request):
    galary=Galary.objects.get(id=request.GET.get('id'))
    galarys=Galary.objects.all()
    photos=list(galary.galaryphoto_set.all())
    if photos:
        first=photos[0]
        del(photos[0])
        context={"galarys":galarys,"photos":photos,"first":first,"galary":galary}
    else:
        context={"galarys":galarys,"photos":"null","first":"null","galary":galary}
    return render(request,'gallery.html',context)




def login_view(request):
    if request.method == "POST":
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        user=auth.authenticate(username=uname,password=password)
        #print(email,"   ",password,"    ",user)
        if user is not None:
            login(request,user)
            return redirect('home_view')
        else:
            messages.error(request,"Invalid User Name or Password",extra_tags="danger")
        return render(request,"users/index.html")
    else:
        return render(request,"users/index.html")

@login_required(login_url='login_view')
def home_view(request):
    msg=MSG.objects.all().order_by('date')
    context={"msgs":msg}
    return render(request,"users/home.html",context)

@login_required(login_url='login_view')
def read(request):
    if request.GET.get("id"):
        msg=MSG.objects.get(id=request.GET.get("id"))
        context={"msg":msg}
    else:
        context={"msg":"null"}
    return render(request,"users/read.html",context)

@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    messages.error(request,"You Were Logged Out",extra_tags="danger")
    return redirect("login_view")