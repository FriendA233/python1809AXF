import hashlib
import os
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods, User
from pyton1809AXF import settings


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
    # 获取用户信息
    token = request.session.get('token')
    responseData = {}
    if token:
        user = User.objects.get(token=token)
        responseData['name'] = user.name
        responseData['rank'] = user.rank
        responseData['img'] = '/static/mine/upfile/'+user.img
        responseData['islogin'] = 1
    else:
        responseData['name'] = '未登录'
        responseData['rank'] = '暂无等级'
        responseData['img'] = '/static/mine/upfile/axf.png'
    return render(request,'mine/mine.html',context=responseData)


def genarate_password(param):
    sha = hashlib.sha3_256()
    sha.update(param.encode('utf-8'))
    return sha.hexdigest()


def register2(request):
    if request.method == 'GET':
        return render(request,'mine/register2.html')
    elif request.method == 'POST':
        try:
            user = User()
            user.account = request.POST.get('account')
            user.password = genarate_password(request.POST.get('password'))
            user.name = request.POST.get('name')
            user.phone = request.POST.get('phone')
            user.addr = request.POST.get('addr')
            imgName = user.account + ".png"
            imgPath = os.path.join(settings.MDEIA_ROOT, imgName)
            file = request.FILES.get('icon')
            with open(imgPath, 'wb') as fp:
                for data in file.chunks():
                    fp.write(data)
                user.img = imgName
            user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
            user.save()
            #状态保持
            request.session['token'] = user.token
            #重定向
            return redirect('axf:mine')
        except:
            return HttpResponse('注册失败')
def login(request):
    if request.method == 'GET':
        return render(request,'mine/login.html')
    elif request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        try:
            user = User.objects.get(account=account)
            if user.password == genarate_password(password):#登陆成功
                user.token = str(uuid.uuid5(uuid.uuid4(),'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('axf:mine')
            else:#登陆失败
                return render(request, 'mine/login.html', context={'Passworderr': '密码不存在'})
        except:
            return render(request,'mine/login.html',context={'Accounterr':'账号不存在'})



def checkaccount(request):
    account = request.GET.get('account')

    responseDate = {
        'msg':'账号可用',
        'status':1
    }
    try:
        user = User.objects.get(account=account)
        responseDate['msg'] = '账号已被占用'
        responseDate['status'] = -1
        return JsonResponse(responseDate)
    except:
        return JsonResponse(responseDate)


def logout(request):
    request.session.flush()
    return redirect('axf:mine')


def addcart(request):
    return JsonResponse('添加购物车成功')