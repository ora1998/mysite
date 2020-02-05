from django import forms
from . import models

class RegisterForm(forms.Form):
    # provincecho = models.Province.objects.all()
    # print(provincecho)
    # citycho =  models.City.objects.all()
    # print(citycho)
    # mstatus = (
    #     (1, "在线"),
    #     (2, "休息"),
    # )
    username = forms.CharField(required=True, label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),error_messages={'required':u'用户名不能为空'})
    password1 = forms.CharField(required=True, label="密码", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, label="确认密码", max_length=128, widget=forms.PasswordInput(attrs={'class':
                                                                                                   'form-control'}))
    companyname = forms.CharField(label="公司名字", max_length=256, widget=forms.TextInput(attrs={'class':
                                                                                                   'form-control'}))
    contactperson = forms.CharField(required=True, label="联系人姓名", max_length=256, widget=forms.TextInput(attrs={'class':
                                                                                                   'form-control'}))
    phoneno = forms.CharField(required=True, label="电话号码", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, label="地址", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(required=True, label="市", queryset=models.City.objects.all(),widget = forms.Select(
        attrs={'size': 1,'style':'width: 5cm'}))
    province = forms.ModelChoiceField(required=True, label="省", queryset=models.Province.objects.all(),widget = forms.Select(
        attrs={'size': 1,'style':'width: 5cm'}))
    # postcode = forms.CharField(label="邮编", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postcode = forms.CharField(required=False, label="邮编", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    wechatid = forms.CharField(required=False, label="微信号", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Email地址",
                             widget=forms.EmailInput(attrs={'class':'form-control'}))
    # //regdate = forms.DateField(label="注册日期", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # //merchantscore = forms.IntegerField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class':
    # //'form-control'}))
    #//merchantclass = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class':
    # //'form-control'}))
    # merchantintro = forms.CharField(label="简介", widget=forms.Textarea(attrs={'cols': 22, 'rows': 5}),)
    merchantintro = forms.CharField(label="简介", required=False, widget=forms.Textarea,)
    # merchantstatus = forms.ChoiceField(label='工作状态', choices=mstatus)
    #systemstatus



    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self['username'].field.widget.attrs.update(value='必填，建议使用电话号码作用用户名',
                onFocus="if(value==defaultValue){value='';this.style.color='#000'}",
                onBlur="if(!value){value=defaultValue;this.style.color='#999'}",
                style="color:#999999")
        # self['password1'].field.widget.attrs.update(value='任意填写',
        #         onFocus="if(value==defaultValue){value='';this.style.color='#000'}",
        #         onBlur="if(!value){value=defaultValue;this.style.color='#999'}",
        #         style="color:#999999")
        # self['password2'].field.widget.attrs.update(value='请再次填写密码，必须和上面相同',
        #         onFocus="if(value==defaultValue){value='';this.style.color='#000'}",
        #         onBlur="if(!value){value=defaultValue;this.style.color='#999'}",
        #         style="color:#999999")
        self['companyname'].field.widget.attrs.update(value='必填：如果没有可随便写一个',
                onFocus="if(value==defaultValue){value='';this.style.color='#000'}",
                onBlur="if(!value){value=defaultValue;this.style.color='#999'}",
                style="color:#999999")
        self['contactperson'].field.widget.attrs.update(value='必填',
                onFocus="if(value==defaultValue){value='';this.style.color='#000'}",
                onBlur="if(!value){value=defaultValue;this.style.color='#999'}",
                style="color:#999999")
        self['phoneno'].field.widget.attrs.update(value='必填',
                onFocus="if(value==defaultValue){value='';this.style.color='#000'}",
                onBlur="if(!value){value=defaultValue;this.style.color='#999'}",
                style="color:#999999")
        self['email'].field.widget.attrs.update(value='必填，密码丢失后只能通过该邮件可以找回',
                onFocus="if(value==defaultValue){value='';this.style.color='#000'}",
                onBlur="if(!value){value=defaultValue;this.style.color='#999'}",
                style="color:#999999")

        self['merchantintro'].field.widget = forms.Textarea(attrs={'cols': 53, 'rows': 10})

# RegisterForm(auto_id=False)

"""
class ServiceForm(forms.Form):
    # provincecho = models.Province.objects.all()
    # print(provincecho)
    # citycho =  models.City.objects.all()
    # print(citycho)
    # mstatus = (
    #     (1, "在线"),
    #     (2, "休息"),
    # )
    class Meta:
        model = models.Merchantservice
        fields = ['name', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, *kwargs)
        self.fields['name'].label = '用户名'
        self.fields['password'].label = '密码'


    username = forms.CharField(required=True, label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               error_messages={'required': u'用户名不能为空'})
    password1 = forms.CharField(required=True, label="密码", max_length=128,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, label="确认密码", max_length=128,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    companyname = forms.CharField(label="公司名字", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contactperson = forms.CharField(required=True, label="联系人姓名", max_length=256,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    phoneno = forms.CharField(required=True, label="电话号码", max_length=128,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, label="地址", max_length=256,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
"""