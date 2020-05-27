from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('orderbook_bias', views.orderbook_bias, name = 'orderbook_bias'),
    path('trader_bias', views.trader_bias, name = 'trader_bias'),
    path('reddit_posts', views.reddit_inst, name = 'reddit_posts'),



]