from django.shortcuts import render, redirect
from . import models
from .forms import UserForm, RegisterForm
from record import models as r_models
import hashlib
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


# Create your views here.
# def base(request):
#     pass
#     return render(request, 'base.html')
def select_index(request):
    return render(request, 'select/select_index.html')


def hash_code(s, salt='pwd'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def change_date(date):
    l_t = list(date)
    year = l_t[0] + l_t[1] + l_t[2] + l_t[3]
    month = l_t[5] + l_t[6]
    day = l_t[8] + l_t[9]
    year = int(''.join(year))
    month = int(''.join(month))
    day = int(''.join(day))
    return year, month, day


def search(request):
    year_list = range(1970, 2050)
    month_list = range(1, 13)
    day_list = range(1, 32)
    stu_no = request.session['user_name']
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    # print(date_from, date_to)
    if date_from and date_to:
        date_from = datetime.datetime(change_date(date_from)[0], change_date(date_from)[1], change_date(date_from)[2])
        date_to = datetime.datetime(change_date(date_to)[0], change_date(date_to)[1], change_date(date_to)[2])
        stu = r_models.record_user.objects.filter(stu_no=stu_no, time__range=(date_from, date_to)).order_by("-time")
    else:
        stu = r_models.record_user.objects.filter(stu_no=stu_no).order_by("-time")

    paginator = Paginator(stu, 5, 2)  # Show 25 contacts per page
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'login/search.html',
                  {"stu": contacts, "year_list": year_list, "month_list": month_list, "day_list": day_list})


def login(request):
    if request.session.get('is_login', None):
        return redirect('/search/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(stu_no=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.stu_no
                    return redirect('/search/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            stu_no = register_form.cleaned_data['stu_no']
            name = register_form.cleaned_data['name']
            sex = register_form.cleaned_data['sex']
            password = register_form.cleaned_data['password']
            password1 = register_form.cleaned_data['password1']
            email = register_form.cleaned_data['email']
            phone = register_form.cleaned_data['phone']
            dorm_name = register_form.cleaned_data['dorm_name']
            dorm_no = register_form.cleaned_data['dorm_no']

            if password != password1:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(stu_no=stu_no)
                if same_name_user:  # 学号唯一
                    message = '该学号已被注册，请重新输入学号！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.stu_no = stu_no
                new_user.name = name
                new_user.password = hash_code(password)
                new_user.sex = sex
                new_user.email = email
                new_user.phone = phone
                new_user.dorm_name = dorm_name
                new_user.dorm_no = dorm_no
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
