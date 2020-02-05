# from django.http import HttpResponse
import json

from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms



from django.core.mail import send_mail
from django.shortcuts import get_object_or_404,get_list_or_404
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if username.strip() and password:
            # print(username + ":" + password)
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                # print(user.password)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})

            if user.password == password:
                # print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')

def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")



def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/merchant_index/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            companyname = register_form.cleaned_data['companyname']
            contactperson = register_form.cleaned_data['contactperson']
            phoneno = register_form.cleaned_data['phoneno']
            address = register_form.cleaned_data['address']
            province = register_form.cleaned_data['province']
            city = register_form.cleaned_data['city']
            postcode = register_form.cleaned_data['postcode']
            wechatid = register_form.cleaned_data['wechatid']
            email = register_form.cleaned_data['email']
            # merchantstatus = register_form.cleaned_data['merchantstatus']
            merchantintro = register_form.cleaned_data['merchantintro']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'renoapp/register.html', locals())
            else:
                same_name_user = models.Merchant.objects.filter(merchantid=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'renoapp/register.html', locals())
                same_email_user = models.Merchant.objects.filter(emailaddr=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'renoapp/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.Merchant()

                new_user.merchantid = username
                new_user.password = password1
                new_user.companyname = companyname
                new_user.contactperson = contactperson
                new_user.phoneno = phoneno
                new_user.address = address
                new_user.procode = province
                new_user.citycode = city
                new_user.postcode = postcode
                new_user.wechatid = wechatid
                new_user.emailaddr = email
                new_user.regdate = datetime.date.today()
                new_user.merchantscore = 0

                # new_user.merchantclass = (models.Memberclass.objects.get(id=1)).memclass
                new_user.merchantclass = models.Merchantclass.objects.get(id=1)
                print(new_user.merchantstatus)
                new_user.merchantstatus = 1
                new_user.systemstatus = 1
                new_user.merchantintro = merchantintro

                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())



def findback(request):
    if request.method == "POST":
        # 确保当数据请求中没有username键时不会抛出异常，而是返回一个我们指定的默认值None
        username = request.POST.get('username', None)
        username = username.strip()
        message = "请正确填写会员号或手机号！"

        if username:    # 确保用户名和手机号都不为空
            try:
                user = models.Merchant.objects.get(merchantid=username)
            except:
                try:
                    user = models.Merchant.objects.get(phoneno=username)
                except:
                    message = "用户名或手机号不存在！"
                    return render(request, 'login/findback.html', {"message": message})
            # emailaddress=user.emailaddr
            message = '密码已发送至： '+user.emailaddr
            print(username, user.password, user.emailaddr)
            send(user.merchantid,user.password,user.emailaddr,)
            return render(request, 'login/findback.html', {"message": message})


        # return render(request, 'renoapp/findback.html', {"message": message})

    return render(request, 'login/findback.html')

def send(userid, passwd, emailid):
    # msg='<a href="http://www.baidu.com" target="_blank">点击激活</a>'
    # send_mail('测试邮件','Here is the message.',settings.EMAIL_FROM,['zhubaolin@gmail.com'],html_message=msg)
    msg='您的用户名是：'+userid+'      '+"\n"+'您的密码是：'+passwd
    send_mail('爱加家i++密码找回邮件', msg, 'zhubl2000@yahoo.com', [emailid],
              fail_silently=False)
    print('已成功发送至：'+emailid)
    # findpassword('发送完成了')
    # return render(request, 'base.html')
    return