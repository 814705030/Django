from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名(学号)", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label="验证码", error_messages={'invalid': '验证码输入有误'})


class RegisterForm(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    stu_no = forms.CharField(label="学号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label="性别", choices=gender)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="电话", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dorm_name = forms.CharField(label="宿舍楼", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dorm_no = forms.CharField(label="门牌号", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label="验证码", error_messages={'invalid': '验证码输入有误'})
