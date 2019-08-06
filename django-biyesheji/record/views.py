from django.shortcuts import render, redirect
from . import models
import login
from .forms import UserForm, VisitorForm


# Create your views here.
def index(request):
    return render(request, "record/index.html")


def user(request):
    if request.method == "POST":
        record_form = UserForm(request.POST)

        if record_form.is_valid():
            message = "提交成功！"
            stu_no = record_form.cleaned_data['stu_no']
            in_out = record_form.cleaned_data['in_out']
            remark = record_form.cleaned_data['remark']
            # print(stu_no)
            try:
                if login.models.User.objects.get(stu_no=stu_no):
                    # request.session['is_login'] = True
                    # request.session['user_id'] = user.id
                    # request.session['user_name'] = user.name
                    # return redirect('/index/')
                    new_record_user = models.record_user.objects.create()
                    new_record_user.stu_no = stu_no
                    new_record_user.in_out = in_out
                    new_record_user.remark = remark
                    # print(stu_no)
                    new_record_user.save()
                else:
                    message = "用户不存在"
            except:
                message = "用户不存在！"
        return render(request, 'record/user.html', locals())
    record_form = UserForm()
    return render(request, 'record/user.html', locals())


def visitor(request):
    if request.method == "POST":
        record_form = VisitorForm(request.POST)
        # message = "请检查填写的内容！"
        if record_form.is_valid():
            message = "提交成功！"
            visitor_name = record_form.cleaned_data['visitor_name']
            in_out = record_form.cleaned_data['in_out']
            idcard = record_form.cleaned_data['idcard']
            remark = record_form.cleaned_data['remark']
            phone = record_form.cleaned_data['phone']
            try:
                new_record_visitor = models.record_visitor.objects.create()
                new_record_visitor.visitor_name = visitor_name
                new_record_visitor.in_out = in_out
                new_record_visitor.idcard = idcard
                new_record_visitor.remark = remark
                new_record_visitor.phone = phone
                # print(stu_no)
                new_record_visitor.save()
                # message = "用户不存在"
            except:
                message = "请检查填写的内容！"
        return render(request, 'record/visitor.html', locals())
    record_form = VisitorForm()
    return render(request, 'record/visitor.html', locals())
