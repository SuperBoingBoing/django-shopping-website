from django.shortcuts import render, redirect
from .models import Phone, Snack, Movie
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import Http404


# Create your views here.
def home(request):
    return render(request, "home.html", {"home": home})

def phone(request):
    phones = Phone.objects.all()
    return render(request, "phone.html", {"phones": phones})

def snack(request):
    snacks = Snack.objects.all()
    return render(request, 'snack.html', {'snacks': snacks})

def movie(request):
    movies = Movie.objects.all()
    return render(request, "movie.html", {'movies':movies})
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Your Username Has Been Created. ')
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Your Email Has Been Created. ')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1)
                user.save()
                return redirect('signin')  
        else:
            messages.info(request, 'Your Password Does Not Match. ')
    else:
        return render(request, "signup.html")
    
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Your Username Or Password Is Incorrect.')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

def calculator(request):
    return render(request, 'calculator.html')

def addtocart(request):
    # phone = Phone.objects.get(id=phone_id)
    # cart = request.session.get('cart', {})
    # if phone_id in cart:
    #     cart[phone_id] += 1
    # else:
    #     cart[phone_id] = 1
    #     request.session['cart'] = cart
    return redirect('/')