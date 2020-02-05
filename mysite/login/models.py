from django.db import models

# Create your models here.

# 1. 省
class Province(models.Model):
    procode = models.CharField(max_length=6, verbose_name="Abbr")
    provincename = models.CharField(max_length=50, verbose_name="Province(English)")
    provincecname = models.CharField(max_length=30, verbose_name="Province(Chinese)")
    displayseq = models.SmallIntegerField(unique=True, verbose_name='Display Sequence')     # 不可重复
    other1 = models.CharField(max_length=200, verbose_name='预留字段1', blank=True, null=True)       # 预留
    other2 = models.CharField(max_length=200, verbose_name='预留字段2', blank=True, null=True)       # 预留

    def __str__(self):
        return self.provincename
        # return self.displayseq, self.procode, self.provincename, self.provincecname

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Province'
        ordering = ['provincename']

# 2. 市
class City(models.Model):
    citycode = models.CharField(max_length=6, verbose_name="Abbr", blank=True, null=True)  # 代码，缩写
    cityname = models.CharField(max_length=30, verbose_name="Cityname(English)")
    citycname = models.CharField(max_length=30, verbose_name="Cityname(Chinese)")
    procode = models.ForeignKey('Province', on_delete=models.CASCADE, verbose_name="Belong to")   # Province.procode 所在省
    displayseq = models.SmallIntegerField(unique=True, verbose_name='Display Sequence')     # 显示顺序, 不可重复
    other1 = models.CharField(max_length=200, verbose_name='预留字段1', blank=True, null=True)       # 预留
    other2 = models.CharField(max_length=200, verbose_name='预留字段2', blank=True, null=True)       # 预留

    def __str__(self):
        return self.cityname
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'City'
        ordering = ['displayseq']

# 3. 商户等级
class Merchantclass(models.Model):
    memclass = models.SmallIntegerField(default=1, unique=True, verbose_name="ClassCode")
    memclassname = models.CharField(default='blue', max_length=30, verbose_name="Class(English)")
    memclasscname = models.CharField(default='蓝卡', max_length=30, verbose_name="Class(Chinese)")
    description = models.CharField(max_length=2000, verbose_name="Class Description", blank=True, null=True)  # 等级解释和描述

    def __str__(self):
        return self.memclassname

    class Meta:
        verbose_name = 'Merchant Class'
        verbose_name_plural = 'Merchant Class'

# 4. 商户
class Merchant(models.Model):
    merchantstatus_choice = (
        (1, 'ON'),
        (2, 'OFF'),
    )  # 商户自己可以设定自己是否营业

    systemstatus_choice = (
        (1, 'Allow'),
        (2, 'Forbid'),
    )  # 平台管理员控制该商户是否可用

    merchantid = models.CharField(max_length=30, unique=True, verbose_name="Userid")  # 商户会员号
    password = models.CharField(max_length=30, verbose_name="Password")   # 商户密码
    companyname = models.CharField(max_length=50, verbose_name="Company Name", blank=True, null=True) #没有公司可以不填写
    contactperson = models.CharField(max_length=50, verbose_name="Contact", blank=True, null=True)  # 联系人姓名
    phoneno = models.CharField(max_length=30, verbose_name="Phone Number")  # 电话号码
    address = models.CharField(max_length=90, verbose_name="Address")  # 地址
    procode = models.ForeignKey('Province', on_delete=models.CASCADE, verbose_name="Province", blank=True, null=True)   # Province.procode
    citycode = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name="City", blank=True, null=True)   # City.citycode
    postcode = models.CharField(max_length=20, verbose_name="Postcode")  # 邮编
    wechatid = models.CharField(max_length=50, verbose_name="Wechat", blank=True, null=True)  # 微信号
    emailaddr = models.EmailField(verbose_name="Email", blank=True, null=True)  # 邮件地址
    regdate = models.DateField(auto_now=True, verbose_name="Register Date")  # 注册日期
    merchantscore = models.IntegerField(default=0, verbose_name="Scores")  # 商户积分
    merchantclass = models.ForeignKey('Merchantclass', on_delete=models.CASCADE, verbose_name="Class", blank=True,
                                      null=True)  # 商户等级
    merchantstatus = models.SmallIntegerField(choices=merchantstatus_choice, default=1, verbose_name="Status")  # 商户状态
    systemstatus = models.SmallIntegerField(choices=systemstatus_choice, default=1, verbose_name="System Status")  # 系统状态
    merchantintro = models.TextField(verbose_name="Introduction", blank=True, null=True)  # 商户简介
    other1 = models.CharField(max_length=200, verbose_name='预留字段1', blank=True, null=True)       # 预留
    other2 = models.CharField(max_length=200, verbose_name='预留字段2', blank=True, null=True)       # 预留
    other3 = models.CharField(max_length=200, verbose_name='预留字段3', blank=True, null=True)       # 预留
    other4 = models.CharField(max_length=200, verbose_name='预留字段4', blank=True, null=True)       # 预留
    other5 = models.CharField(max_length=200, verbose_name='预留字段5', blank=True, null=True)       # 预留

    def __str__(self):
        return self.companyname+' :   '+self.contactperson
    class Meta:
        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchant'
        ordering = ['merchantid']
        # indexes = [
        #     models.Index(fields=['memberid'], name='memberid_idx', ),
        # ]
        indexes = [
            models.Index(fields=['fullname'], name='fullname_idx', ),
        ]
        indexes = [
            models.Index(fields=['regdate'], name='regdate_idx', ),
        ]


# 用户
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"