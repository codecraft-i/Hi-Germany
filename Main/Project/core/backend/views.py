from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import activate
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404

import random

from django.db.models import F
from itertools import chain

from .forms import MessageUserForm


from django.urls import reverse

# from django.shortcuts import render, get_object_or_404
from .models import *


# blogs = [
#     {'id': 1, 'name': 'Lets Learn Python !'},
#     {'id': 2, 'name': 'Lets Learn Html !'},
#     {'id': 3, 'name': 'Lets Learn JS and TS !'},
# ]



# Create your views here.

def Base(request):
    if request.method == 'POST':
        form = MessageUserForm(request.POST)
        if form.is_valid():
            instance = form.save()
            data = {'success': True, 'message': 'Data saved successfully'}
            return JsonResponse(data)
        else:
            data = {'success': False, 'errors': form.errors}
            return JsonResponse(data, status=400)
    else:
        form = MessageUserForm()
    
    context = {
        'form': form
    }

    return render(request, 'Home/base.html', context)

def Home(request):
    # Fetch all messages from Message and MessageUseful models
    all_messages = list(Message.objects.all()) + list(MessageUsefull.objects.all())

    # Shuffle the combined list of messages
    random.shuffle(all_messages)

    # Take the first 5 messages
    selected_messages = all_messages[:5]



    # Get the latest 5 entries from UsefulData
    latest_useful_data = UsefullData.objects.order_by('-created_at')[:5]

    # Get all blog and usefull data posts
    all_posts = list(chain(Blog.objects.all(), UsefullData.objects.all()))

    # Shuffle the combined list randomly
    random.shuffle(all_posts)

    # Get the first 5 posts from the shuffled list
    random_posts = all_posts[:5]

    ##
    ##

    # Barcha UsefullData obyektlarini olish
    all_usefulldata = UsefullData.objects.all()
    
    # Besh tasini tanlash
    random_usefulldata = random.sample(list(all_usefulldata), min(len(all_usefulldata), 5))



    ##
    ##


    # if request.method == 'POST':
    #     form = MessageUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('Home')  # success nomli url bo'lishi mumkin
    # else:
    #     form = MessageUserForm()

    if request.method == 'POST':
        form = MessageUserForm(request.POST)
        if form.is_valid():
            instance = form.save()
            data = {'success': True, 'message': 'Data saved successfully'}
            return JsonResponse(data)
        else:
            data = {'success': False, 'errors': form.errors}
            return JsonResponse(data, status=400)
    else:
        form = MessageUserForm()

    ##
    ##
        
    popularPosts = PopularPosts.objects.all().order_by('-created_at')
    
    context = {
        'selected_messages': selected_messages,
        'latest_useful_data': latest_useful_data,

        'random_posts': random_posts,

        'random_usefulldata': random_usefulldata,

        'form': form,

        'popularPosts': popularPosts
    }
    return render(request, 'Home/index.html', context)

def SignIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Username or Password does not exit')
    
    context = {}
    return render(request, 'Home/signin.html', context)

def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            # Check if passwords match
            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'Home/signup.html', {'form': form})

            # Check if username or email already exists
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                messages.error(request, 'Username or email is already taken.')
                return render(request, 'Home/signup.html', {'form': form})

            # Save user to the database
            user = form.save(commit=False)
            user.email = email
            user.save()

            # Authenticate and log in the user
            user = authenticate(username=username, password=password1)
            login(request, user)

            messages.success(request, 'Registration successful!')
            return redirect('Home')  # Replace 'Home' with your actual home page URL
        else:
            # Form is not valid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')

            return render(request, 'Home/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()

    return render(request, 'Home/signup.html', {'form': form})


def LogOut(request):
    logout(request, )
    return redirect('Home')

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            return HttpResponseRedirect(request.POST.get('next', '/'))
    return HttpResponseRedirect('/')

def BlogsView(request):
    blogs = Blog.objects.all().order_by('-created_at')
    allExtraBlogDatas = ExtraBlog.objects.all()

    context = {
        'blogs': blogs,
        'allExtraBlogDatas': allExtraBlogDatas,
    }

    return render(request, 'Internal/Blogs/blogs.html', context)

def BlogView(request, pk):
    blog = Blog.objects.get(id=pk)
    blog_messages = blog.message_set.all().order_by('-created_at')

    # aEBlogs = ExtraBlog.objects.all()

    # ExtraBloglarni olish
    extra_blogs = ExtraBlog.objects.filter(post=blog)

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            blog=blog,
            body=request.POST.get('body')
        )


        return redirect('blog', pk=blog.id)

    context = {
        'blog': blog,
        'blog_messages': blog_messages,

        'extra_blogs': extra_blogs
    }
    return render(request, 'Internal/MetaBlogs/blog.html', context)

@csrf_exempt
def like_blog(request, pk):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=pk)

        # Foydalanuvchining profilini olish
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Foydalanuvchi bitta blogni faqat bir marta like qila oladi
        if not user_profile.liked_blogs.filter(pk=blog.pk).exists():
            # Blogni likelar sonini o'zgartirish
            blog.likes += 1
            blog.save()

            # Foydalanuvchi uchun likelangan bloglarni saqlash
            user_profile.liked_blogs.add(blog)

            # O'zingizga kerakli ma'lumotni qaytarish
            return JsonResponse({'likes': blog.likes})

        # Eski yoki qayta boshqa blogga like qilish urinishi
        return JsonResponse({'error': 'Already liked this blog'})

    return JsonResponse({'error': 'Invalid request method'})

def UsefullsView(request):
    usefulls = UsefullData.objects.all().order_by('-created_at')

    context = {
        'usefulls': usefulls,
    }

    return render(request, 'Internal/UsefullAll/usefulls.html', context)

def UsefullView(request, pk):
    usefulls = get_object_or_404(UsefullData, id=pk)

    usefull = UsefullData.objects.get(id=pk)

    extra_usefull = ExtraUsefull.objects.filter(post=usefull)
    
    aEBUsefulls = ExtraUsefull.objects.all()

    usefull_messages = usefulls.messageusefull_set.all().order_by('-created_at')

    if request.method == "POST":
        message = MessageUsefull.objects.create(
            user=request.user,
            blog=usefulls,
            body=request.POST.get('body')
        )


        return redirect('usefull', pk=usefulls.id)

    context = {
        'usefulls': usefulls,
        'aEBUsefulls': aEBUsefulls,

        'usefull_messages': usefull_messages,

        'usefull': usefull,
        'extra_usefull': extra_usefull
    }
    return render(request, 'Internal/UsefullAll/usefull.html', context)

@csrf_exempt
def like_usefull(request, pk):
    if request.method == 'POST':
        blog = get_object_or_404(UsefullData, pk=pk)

        # Foydalanuvchining profilini olish
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Foydalanuvchi bitta blogni faqat bir marta like qila oladi
        if not user_profile.liked_blogs.filter(pk=blog.pk).exists():
            # Blogni likelar sonini o'zgartirish
            blog.likes += 1
            blog.save()

            # Foydalanuvchi uchun likelangan bloglarni saqlash
            user_profile.liked_blogs.add(blog)

            # O'zingizga kerakli ma'lumotni qaytarish
            return JsonResponse({'likes': blog.likes})

        # Eski yoki qayta boshqa blogga like qilish urinishi
        return JsonResponse({'error': 'Already liked this blog'})

    return JsonResponse({'error': 'Invalid request method'})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == "POST":
        message.delete()
        return redirect('Home')
    return render(request, 'Components/delete.html', {
        'object': message
    })

@login_required(login_url='login')
def deleteMessageUsefull(request, pk):
    message = MessageUsefull.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == "POST":
        message.delete()
        return redirect('Home')
    return render(request, 'Components/delete.html', {
        'object': message
    })


def VisasViews(request):
    visasData = VisasData.objects.all()

    context = {
        'visas': visasData,
    }

    return render(request, 'Internal/Visas/visas.html', context)

@login_required(login_url='login')
def likesView(request):
    user_profile = UserProfile.objects.get(user=request.user)
    liked_blogs = user_profile.liked_blogs.all()

    context = {
        'liked_blogs': liked_blogs
    }

    return render(request, 'Home/likes.html', context)

@login_required(login_url='login')
def userProfile(request):
    userDatas = UserProfile.objects.all()

    context = {
        'userDatas': userDatas,
    }

    return render(request, 'Home/profile.html', context)

def termsPrivasy(request):
    return render(request, 'Home/ourCondition.html')

def succesN(request):
    return render(request, 'Home/succes.html')