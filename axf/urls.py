from django.conf.urls import url

from axf import views

urlpatterns = [
    url('^$',views.home,name='index'), #首页
    url('^home/$',views.home,name='home'),
    url('^market/(\d+)/(\d+)/(\d+)/$',views.market,name='market'),#超市
    url('^cart/$',views.cart,name='cart'),#购物车
    url('^mine/$',views.mine,name='mine'),#我的
    url('^register/$',views.register,name='register'),
    url('^login/$',views.login,name='login')

]