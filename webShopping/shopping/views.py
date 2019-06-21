from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    images = list()
    images1 = list()
    all_images = list()

    for image in HatImage.objects.all():
        all_images.append(image)
    for image in GlassesImage.objects.all():
        all_images.append(image)

    featured_hats = Hat.objects.filter(kind=ProductKind.objects.filter(name='featured products').first())

    for hat in featured_hats:
        images.append(HatImage.objects.filter(product=hat).first())
    images_2 = images[0:2]

    featured_glasses = Glasses.objects.filter(kind=ProductKind.objects.filter(name='featured products').first())
    for glasse in featured_glasses:
        images1.append(GlassesImage.objects.filter(product=glasse).first())

    images_3 = images1[0:2]
    return render(request, 'shopping/index.html', context={'images': images_2, 'images1': images_3, 'all_images':all_images})


def home(request, page):
    images = list()
    images1 = list()
    all_images = list()

    for image in HatImage.objects.all():
        all_images.append(image)
    for image in GlassesImage.objects.all():
        all_images.append(image)

    hats = Hat.objects.filter(kind=ProductKind.objects.filter(name='featured products').first())
    for hat in hats:
        images.append(HatImage.objects.filter(product=hat).first())
    images_2 = images[0:2]
    glasses = Glasses.objects.filter(kind=ProductKind.objects.filter(name='featured products').first())
    for glasse in glasses:
        images1.append(GlassesImage.objects.filter(product=glasse).first())
    images_3 = images1[0:2]

    if page == '1':
        return render(request, 'shopping/index.html', context={'images': images_2, 'images1': images_3, 'all_images':all_images})
    elif page == '2':
        return render(request, 'shopping/index-2.html', context={'images': images_2})
    elif page == '3':
        return render(request, 'shopping/index-3.html', context={'images': images_2})
    elif page == '4':
        return render(request, 'shopping/index-4.html', context={'images': images_2})
    else:
        return HttpResponse('页面不存在')


def blog(request):
    return render(request, 'shopping/blog.html')


def blog_details(request):
    return render(request, 'shopping/blog-details.html')


def contact(request):
    return render(request, 'shopping/contact.html')


def women(request):
    page = request.GET.get('page')
    page = page if page else 1

    all_images = list()
    for image in HatImage.objects.all():
        all_images.append(image)

    for image in GlassesImage.objects.all():
        all_images.append(image)
    paginator = Paginator(all_images, 2)
    page = paginator.page(page)

    return render(request, 'shopping/shop-grid.html', context={'page': page})


def men(request):
    page = request.GET.get('page')
    page = page if page else 1

    all_images = list()
    for image in HatImage.objects.all():
        all_images.append(image)

    for image in GlassesImage.objects.all():
        all_images.append(image)
    paginator = Paginator(all_images, 2)
    page = paginator.page(page)

    return render(request, 'shopping/shop-grid.html', context={'page': page})


def product_details(request):
    return render(request, 'shopping/product-details.html')


def about(request):
    return render(request, 'shopping/about.html')


def account(request):
    return render(request, 'shopping/account.html')


def wishlist(request):
    images = list()
    hats = Hat.objects.filter(is_wishlist=True)
    for hat in hats:
        images.append(hat.hatimage_set.first())

    glasses = Glasses.objects.filter(is_wishlist=True)
    for glasse in glasses:
        images.append(glasse.glassesimage_set.first())

    bags = Bag.objects.filter(is_wishlist=True)
    for bag in bags:
        images.append(bag.bagimage_set.first())


    return render(request, 'shopping/wishlist.html', context={'images': images})


def add_wishlist(request, oid):
    print(oid)
    hat = Hat.objects.filter(pk=oid).first()
    if hat:
        # 将订单设为心爱订单
        hat.is_wishlist = True
        hat.save()
    return redirect('/shopping/wishlist')


def shop_list(request):
    all_images = list()
    for image in HatImage.objects.all():
        all_images.append(image)

    for image in GlassesImage.objects.all():
        all_images.append(image)

    page = request.GET.get('page')
    page = page if page else 1
    paginator = Paginator(all_images, 2)
    page = paginator.page(page)

    return render(request, 'shopping/shop-list.html', context={'page': page})


def cart(request):
    return render(request, 'shopping/cart.html')


def add_cart(request, id):
    hat = Hat.objects.filter(pk=id).first()
    print(hat)
    order = Order()
    order.product = hat
    order.quantity = 1
    print(order)
    order.save()
    return redirect('/cart')


def checkout(request):
    return render(request, 'shopping/checkout.html')


def page404(request):
    return render(request, 'shopping/404.html')


