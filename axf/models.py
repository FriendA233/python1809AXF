from django.db import models

# Create your models here.

#基础类
class Base(models.Model):
    #图片
    img = models.CharField(max_length=100)
    #名称
    name = models.CharField(max_length=100)
    #商品编号
    trackid = models.CharField(max_length=10)


    class Meta:
        abstract = True


#轮播图
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'


#导航
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'


#每日必购
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'


#商品布冯
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'


#商品主体
 #axf_mainshow(trackid,name,img,categoryid,brandname,
# img1,childcid1,productid1,longname1,price1,marketprice1,
# img2,childcid2,productid2,longname2,price2,marketprice2,
# img3,childcid3,productid3,longname3,price3,marketprice3)


class MainShow(models.Model):
    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=100)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=100)
    productid1 = models.CharField(max_length=100)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=100)
    productid2 = models.CharField(max_length=100)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=100)
    productid3 = models.CharField(max_length=100)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'


#品牌分类
#insert into axf_foodtypes(typeid,typename,childtypenames,typesort) values("104749","热销榜","全部分类:0",1)
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=100)#子类名称
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()#显示的先后顺序
    class Meta:
        db_table = 'axf_foodtypes'



#商品信息
#insert into axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum) values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);

class Goods(models.Model):
    productid = models.CharField(max_length=100)#商品ID
    productimg = models.CharField(max_length=256)#商品图片
    productname = models.CharField(max_length=100)#商品名称
    productlongname = models.CharField(max_length=100)#商品长名称
    isxf = models.BooleanField(default=False) #是否精选
    pmdesc = models.BooleanField(default=False) #买一送一
    specifics = models.CharField(max_length=100)#规格
    price = models.DecimalField(max_digits=7,decimal_places=2)#价格
    marketprice = models.DecimalField(max_digits=7,decimal_places=2)#超市价格
    categoryid = models.IntegerField()#分类ID
    childcid = models.IntegerField()#子类ID
    childcidname = models.CharField(max_length=100)#子类名称
    dealerid = models.CharField(max_length=100)#详情ID
    storenums = models.IntegerField()#库存
    productnum = models.IntegerField()#销量

    class Meta:
        db_table = 'axf_goods'



# 用户注册表
class User(models.Model):
    # 账号
    account = models.CharField(max_length=80,unique=True)
    # 密码
    password = models.CharField(max_length=256)
    #名字
    name = models.CharField(max_length=100)
    #手机号
    phone = models.CharField(max_length=100,unique=True)
    #地址
    addr = models.CharField(max_length=256)
    #头像
    img = models.CharField(max_length=100)
    #等级
    rank = models.IntegerField(default=1)
    #token
    token = models.CharField(max_length=256)

    class Meta:
        db_table='axf_user'



#购物车
class Cart(models.Model):
    #用户
    user = models.ForeignKey(User)
    #商品
    goods = models.ForeignKey(Goods)
    #商品数量
    number = models.IntegerField()
    #是否选中
    isselect= models.BooleanField(default=True)

    class Meta:
        db_table = 'axf_cart'










