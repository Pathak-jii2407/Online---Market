from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from .models import Cloth,Review,BuyProduct
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def product_list(request):
    clothes = Cloth.objects.all()
    return render(request,'shop_base/product_list.html',{'clothes':clothes})

@login_required  
def product_detail(request, pk):
    cloth = get_object_or_404(Cloth, pk=pk)
    if request.method == 'POST':
        # Use the logged-in user as the author
        author = request.user if request.user.is_authenticated else None
        review_content = request.POST.get('review')
        Review.objects.create(clothes=cloth, author=author, content=review_content)
    
    return render(request, 'shop_base/product_detail.html', {'cloth': cloth})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            user=None
        if user !=None:
            login(request, user)
            return redirect('account')
        user = User.objects.create_user(username=username,password=password)
    return render(request,'shop_base/login.html')

def account_page(request):
    user = request.user
    purchases = BuyProduct.objects.filter(user=user)
    return render(request, 'shop_base/account.html', {'purchases': purchases})

def payment_process(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cloth = Cloth.objects.filter(id=product_id).first() 
        if cloth:
            BuyProduct.objects.create(clothes=cloth, user=request.user, price=cloth.price)
        
    return render(request,'shop_base/payment_process.html',{'cloth':cloth})


def payment_success(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        return render(request, 'shop_base/payment_success.html', {'card_number': card_number, 'expiry_date': expiry_date})
    else:
        return redirect('product_list')


def payment_failed(request):
    return render(request, 'shop_base/payment_failed.html')


