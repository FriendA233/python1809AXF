from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


def home(request):     #首页
    #轮播图数据
    wheels = Wheel.objects.all()

    #导航数据
    navs = Nav.objects.all()

    #每日必购
    mustbuys = Mustbuy.objects.all()

    #商品部分
    shoplist = Shop.objects.all()
    shophead = shoplist[0]
    shoptab = shoplist[1:3]
    shopclass = shoplist[3:7]
    shopcommend = shoplist[7:11]

    #商品主体
    mianshows = MainShow.objects.all()
    data = {
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead':shophead,
        'shoptab':shoptab,
        'shopclass':shopclass,
        'shopcommend':shopcommend,
        'mianshows':mianshows
    }
    return render(request,'home/home.html',context=data)

# categoryid 分类id
# childid 子类id
#sortid 排序id
def market(request,categoryid,childid,sortid):    #闪购超市

    #分类信息
    foodtypes = Foodtypes.objects.all()

    #分类  点击  下标 >>> 分类ID
    typeIndex = int(request.COOKIES.get('typeIndex','0'))

    #子类信息
    childtypenames = foodtypes.get(typeid=categoryid).childtypenames
    childTypeList = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        dir = {
            'childname':arr[0],
            'childid':arr[1]
        }
        childTypeList.append(dir)
    #根据分类下标，获取 对应 分类ID
    categoryid = foodtypes[typeIndex].typeid
    # goodslist = Goods.objects.all()[0:5]
    #商品信息-根据分类ID获取对应信息
    if childid == '0':
        goodslist = Goods.objects.filter(categoryid=categoryid)
    else:
        goodslist = Goods.objects.filter(categoryid=categoryid,childcid=childid)


    # 排序
    if sortid == '1':  #销量排序
        goodslist = goodslist.order_by('-productnum')
    elif sortid == '2':  #价格最低
        goodslist = goodslist.order_by('price')
    elif sortid =='3':  #价格最高
        goodslist = goodslist.order_by('-price')
    data = {
        'foodtypes':foodtypes,#分类信息
         'goodslist':goodslist,#商品信息
        'childTypeList':childTypeList,#子类信息
        'categoryid':categoryid,#分类id
        'childid':childid
    }
    return render(request,'market/market.html',context=data)


def cart(request):     #购物车
    return render(request,'cart/cart.html')


def mine(request):      #我的
    return render(request,'mine/mine.html')


def register(request):
    return render(request,'mine/register.html')


def login(request):
    return render(request,'mine/login.html')