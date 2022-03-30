from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render 
from blog.forms import User_Signup, User_Login, PostForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login, logout
from blog.models import Post
from django.contrib import messages
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html",{'posts':posts})

def contact(request):
    return render(request, "blog/contact.html")

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = User_Signup(request.POST)
            if fm.is_valid():
                user = fm.save()
                group = Group.objects.get(name="Autho")
                user.groups.add(group)
                messages.success(request, "Congratulations! You have become an Author")                
                return HttpResponseRedirect('/signup/')
        else:
            fm = User_Signup()
        return render(request, "blog/signup.html", {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        uname = user.username
        fname = user.first_name
        lname = user.last_name
        email = user.email
        groups = groups = user.groups.all()
        context = {
            'uname':uname,
            'fname':fname,
            'lname':lname,
            'email':email,
            'groups':groups,
        }
        return render(request,'blog/profile.html',context)
    else:
        return HttpResponseRedirect('/login/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = User_Login(request = request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = User_Login()
        return render(request,'blog/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def dashboard(request):    
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all() 
        context = {
            'posts':posts,
            'full_name':full_name,
            'groups':groups
        }
        return render(request,'blog/dashboard.html',context)
    else:
        return HttpResponseRedirect('/login/')
        
def post_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Post Added Successfully!")
                return HttpResponseRedirect('/post-add/')
        else:
            form = PostForm()
        return render(request,'blog/post_add.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def post_update(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, "Post Update Successfully!")
                return HttpResponseRedirect('/dashboard/')
        else:
            post = Post.objects.get(pk=id)
            form = PostForm(instance=post)
        return render(request,'blog/post_update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def post_delete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(pk=id)
            post.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')