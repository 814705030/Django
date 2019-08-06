from django import forms
from captcha.fields import CaptchaField

gender = (
    ('进', '进'),
    ('出', '出'),
)


class UserForm(forms.Form):
    stu_no = forms.CharField(label="用户名(学号)", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_out = forms.ChoiceField(label="进出", choices=gender)
    remark = forms.CharField(label="备注", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label="验证码", error_messages={'invalid': '验证码输入有误'})


class VisitorForm(forms.Form):
    visitor_name = forms.CharField(label="姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_out = forms.ChoiceField(label="进出", choices=gender)
    idcard = forms.CharField(label="身份证号", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    remark = forms.CharField(label="备注", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="手机号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
