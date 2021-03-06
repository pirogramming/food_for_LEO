from django.contrib import admin
from django.urls import path, include

from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('brand_page/', brand_page, name='brand_page'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('reset_pw', reset_pw, name='reset_pw'),
    path('sign_up', sign_up, name='sign_up'),
    path('account/delete/', delete_account, name='delete_account'),
    path('product/detail/<int:pk>', product_detail, name='product_detail'),
    path('product/likes/', product_like, name="product_like"),
    path('result/', search_result, name="search_result"),
    path('brand/detail/<int:pk>', brand_detail, name='brand_detail'),
    path('brand_page', brand_page, name='brand_page'),
    path('item_house', item_House, name="item_House"),

]
