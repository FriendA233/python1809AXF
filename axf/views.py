from django.shortcuts import render

# Create your views here.
def home(request):     #首页
    return render(request,'home/home.html')


def market(request):    #超市
    return None


def cart(request):     #购物车
    return None


def mine(request):      #我的
    return None