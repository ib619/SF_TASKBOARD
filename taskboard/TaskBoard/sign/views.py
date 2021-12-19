import random

from django.shortcuts import render, redirect, HttpResponse
from .forms import MemberForm
from .models import Member
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail


def Membership(request):

    global registered
    global u1
    global email
    registered = False
    if(request.method == 'POST'):
        Member = MemberForm(request.POST, request.FILES)

        if Member.is_valid():
            user = Member.save()
            username = request.POST.get('Name', '')
            u1 = username
            password = request.POST.get('password', '')
            email = request.POST.get('Email', '')
            user.save()
            user = authenticate(request, username=username, password=password, email=email)

            if user is None:
                user = get_user_model().objects.create_user(username=username, password=password, email=email)
                user.save()

        else:
            print('user_form.errors')
        return redirect('otp')

    else:
        Member = MemberForm()
        return render(request, 'premium.html', { 'mem': Member, 'registered': registered, })


global no
no = 0


def otp(request):
    global no
    if request.method == 'POST':
        otp = request.POST.get('otp', '')
        if int(otp) == int(no):
            return redirect('greet')
        else:
            u = Member.objects.filter(Name=u1)
            u.delete()
            us = User.objects.get(username=u1)
            us.delete()
            return redirect('otpfail')

    else:
        no = random.randrange(1000,9999)
        send_mail('Your Code Verification', f'Your Code is {no}', 'igorbodnarprog@yandex.ru', [email], fail_silently=True)
        return render(request, 'otp.html')

def greet(request):
    return render(request, 'greet.html')


def otpfail(request):
    return render(request, 'otpfail.html')
