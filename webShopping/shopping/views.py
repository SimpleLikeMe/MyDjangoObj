from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'shopping/blog-details.html')


def home(request, page):
    print(page)
    if page == '1':
        return render(request, 'shopping/index.html')
    elif page == '2':
        return render(request, 'shopping/index-2.html')
    elif page == '3':
        return render(request, 'shopping/index-3.html')
    elif page == '4':
        return render(request, 'shopping/index-4.html')
    else:
        return HttpResponse('页面不存在')


def blog(request):
    return render(request, 'shopping/blog.html')


def blog_details(request):
    return render(request, 'shopping/blog-details.html')


def contact(request):
    return render(request, 'shopping/contact.html')


def women(request):
    return render(request, 'shopping/shop-grid.html')


def men(request):
    return render(request, 'shopping/shop-grid.html')


def product_details(request):
    return render(request, 'shopping/product-details.html')


def about(request):
    return render(request, 'shopping/about.html')


def account(request):
    return render(request, 'shopping/account.html')


def wishlist(request):
    return render(request, 'shopping/wishlist.html')


def shop_list(request):
    return render(request, 'shopping/shop-list.html')


def cart(request):
    return render(request, 'shopping/cart.html')


def checkout(request):
    return render(request, 'shopping/checkout.html')


def page404(request):
    return render(request, 'shopping/404.html')


