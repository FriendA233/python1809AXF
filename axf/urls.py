from django.conf.urls import url

from axf import views

urlpatterns = [
    url('^$',views.home,name='index'), #首页
    url('^home/$',views.home,name='home'),
    url('^market/(\d+)/(\d+)/(\d+)/$',views.market,name='market'),#超市
    url('^cart/$',views.cart,name='cart'),#购物车
    url('^mine/$',views.mine,name='mine'),#我的
    url('^register2/$',views.register2,name='register2'),
    url('^login/$',views.login,name='login'),
    url('^checkaccount/$',views.checkaccount,name='checkaccount'),#账号验证
    url('^logout/$',views.logout,name='logout'),
    url('^addcart/$',views.addcart,name='addcart'), #添加购物车操作
    url('^subcart/$',views.subcart,name='subcart') #购物车减操作
]