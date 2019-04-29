from django.shortcuts import render,redirect
from .forms import *
import random
from hashlib import md5
# Create your views here.


def index(request):
    return render(request, 'bookmanage/index.html')


def login(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'bookmanage/reader_login.html', context={'form': form})
    elif request.method == 'POST':
        # 获取表单数据
        form = UserForm(request.POST)
        if form.is_valid():
            print('获取表单数据成功')
            form.save(commit=False)
            account = form.instance.account
            password = form.instance.password
            # 验证用户
            if not check_user(account, password):
                # 验证失败
                return redirect('/bookmanage/login')
            # 用户正确,设置sessionID
            request.session['account'] = request.POST.get('account')
            print('获取表单数据成功')
            return redirect('/bookmanage/home')
        print('登陆失败')
        return redirect('/bookmanage/login')


def register(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'bookmanage/register.html', context={'form': form})
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            if form.instance.password != request.POST.get('confirm'):
                return redirect('/bookmanage/register')
            if not form.instance.password:
                return redirect('/bookmanage/register')
            # 获取随机账号
            form.instance.account = make_account()
            # 加密密码
            form.instance.password = encryption_pwd(form.instance.password)
            form.save()
            return redirect('/bookmanage/login')
        else:
            return redirect('/bookmanage/register')


def home(request):
    account = request.session.get('account')
    user = User.objects.all().filter(account=account).first()
    return render(request, 'bookmanage/reader.html', context={'user': user})


def query(request):
    if request.method == 'GET':
        return render(request, 'bookmanage/reader_query.html')
    elif request.method == 'POST':
        item = request.POST.get('item')
        value = request.POST.get('query')

        if item == 'name':
            books = Book.objects.all().filter(name=value)
        elif item == 'author':
            books = Book.objects.all().filter(author=value)
        return render(request, 'bookmanage/reader_query.html', context={'books': books})


def book_info(request, bid):
    book = Book.objects.all().filter(pk=bid).first()
    borrow = BorrowHistory.manage.all().filter(book=book).filter(status=True).first()
    return render(request, 'bookmanage/reader_book.html', context={'book': book, 'borrow': borrow})


def borrowing(request, bid):
    book = Book.objects.all().filter(pk=bid).first()
    if book.status:
        # 以借
        return redirect('/bookmanage/bookinfo/%s' % (bid,))
    book.status = True
    book.save()
    user = User.objects.all().filter(account=request.session.get('account')).first()
    # 创建借阅记录
    BorrowHistory.manage.crate_borrow_history(user=user, book=book)
    return redirect('/bookmanage/bookinfo/%s' % (bid,))


def info(request):
    account = request.session.get('account')
    user = User.objects.all().filter(account=account).first()
    return render(request, 'bookmanage/reader_info.html', context={'user': user})


def history(request):
    user = User.objects.all().filter(account=request.session.get('account')).first()
    borrows = BorrowHistory.manage.all().filter(user=user)
    return render(request, 'bookmanage/reader_history.html', context={'borrows': borrows})


def modify(request):
    if request.method == 'GET':
        return render(request, 'bookmanage/reader_modify.html')
    elif request.method == 'POST':

        account = request.session.get('account')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            # 两次密码不一致
            return redirect('/bookmanage/modify')
        # 获取原密码
        old_password = request.POST.get('old_password')
        user = check_user(account, old_password)
        if not user:
            # 密码错误
            return redirect('/bookmanage/modify')
        # 验证成功,修改信息
        user.name = request.POST.get('name')
        user.password = encryption_pwd(request.POST.get('password'))
        user.email = request.POST.get('email')
        user.college = request.POST.get('college')
        user.save()
        return redirect('/bookmanage/home')


def make_account():
    account = ''
    for i in range(0, 9):
        account += str(random.randint(0, 9))
    if User.objects.all().filter(account=account).first():
        return make_account()
    return account


def encryption_pwd(password, encode='utf-8'):
    m = md5()
    password = str(password)
    m.update(password.encode(encode))
    return m.hexdigest()


def check_user(account, password):
    user = User.objects.all().filter(account=account).first()
    if not user:
        return False
    if user.password != encryption_pwd(str(password)):
        return False
    return user



