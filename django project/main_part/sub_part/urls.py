
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('about',views.about,name='about'),
    path('orders',views.orders,name='orders'),
    path('bestselling',views.bestselling,name='bestselling'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    
    path('userlogin',views.userlogin,name='userlogin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('adminindex',views.adminindex,name='adminindex'),
    path(' admin user management view',views.adminusermanagementview,name='admin user management view'),
    path('admin user management add',views.adminusermanagementadd,name='admin user management add'),
    path('admin category list',views.admincategorylist,name='admin category list'),
    path('admincategoryadd',views.admincategoryadd,name='admincategoryadd'),
    path('admin_unit list',views.admin_unitlist,name='admin_unit list'),
    path('admin unit add',views.adminunitadd,name='admin unit add'),
    path('admin_tax list',views.admintaxlist,name='admin_tax list'),
    path('admin_tax add',views.admintaxadd,name='admin_tax add'),
    path('admin_product list',views.adminproductlist,name='admin_product list'),
    path('admin_product add',views.adminproductadd,name='admin_product add'),
    path('admin quotations list',views.adminquotationslist,name='admin quotations list'),
    path('admin_quotations add',views.adminquotationsadd,name='admin_quotations add'),
    path('admin_purchase list',views.adminpurchaselist,name='admin_purchase list'),
    path('admin_purchase add',views.adminpurchaseadd,name='admin_purchase add'),
    path('admin_stock transfer list',views.adminstocktransferlist,name='admin_stock transfer list'),
    path('admin_stock transfer add',views.adminstocktransferadd,name='admin_stock transfer add'),
    path('admin_sales list',views.adminsaleslist,name='admin_sales list'),
    path('admin_return product',views.adminreturnproduct,name='admin_return product'),
    path('admin_reg_form_new',views.admin_reg_form_new,name='admin_reg_form_new'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    
    



]