from django.shortcuts import render

# Create your views here.
from axf.models import Wheel


def home(request):     #首页
    #轮播图数据
    wheels = Wheel.objects.all()

    return render(request,'home/home.html',context={'wheels':wheels})


def market(request):    #超市
    return render(request,'market/market.html')


def cart(request):     #购物车
    return render(request,'cart/cart.html')


def mine(request):      #我的
    return render(request,'mine/mine.html')