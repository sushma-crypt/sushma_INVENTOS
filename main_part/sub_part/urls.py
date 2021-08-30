
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
    path('admin user management view',views.adminusermanagementview,name='admin user management view'),
    

    path('admin user management add',views.adminusermanagementadd,name='admin user management add'),
    path('adminusermanagementadd_sub',views.adminusermanagementadd_sub,name='adminusermanagementadd_sub'),

    path('edit_usermanagement_add/<int:id>',views.edit_usermanagement_add,name='edit_usermanagement_add'),
    path('edit_usermanagement_add_update_form_sub/<int:id>',views.edit_usermanagement_add_update_form_sub,name='edit_usermanagement_add_update_form_sub'),
    path('edit_usermanagement_delete/<int:id>',views.edit_usermanagement_delete,name='edit_usermanagement_delete'),


    path('admin category list',views.admincategorylist,name='admin category list'),
    path('admincategoryadd',views.admincategoryadd,name='admincategoryadd'),
    path('admincategoryadd_form_sub',views.admincategoryadd_form_sub,name='admincategoryadd_form_sub'),
    path('edit_category_add/<int:id>',views.edit_category_add,name='edit_category_add'),
    path('edit_category_add_update_form_sub/<int:id>',views.edit_category_add_update_form_sub,name='edit_category_add_update_form_sub'),
    path('edit_category_delete/<int:id>',views.edit_category_delete,name='edit_category_delete'),




    path('admin_unit list',views.admin_unitlist,name='admin_unit list'),
    path('admin unit add',views.adminunitadd,name='admin unit add'),
    path('adminunitadd_form_sub',views.adminunitadd_form_sub,name='adminunitadd_form_sub'),
    path('edit_unitadd/<int:id>',views.edit_unitadd,name='edit_unitadd'),
    path('edit_unitadd_update_form_sub/<int:id>',views.edit_unitadd_update_form_sub,name='edit_unitadd_update_form_sub'),
    path('edit_unitadd_delete/<int:id>',views.edit_unitadd_delete,name='edit_unitadd_delete'),

    path('admin_tax list',views.admintaxlist,name='admin_tax list'),
    path('admin_tax add',views.admintaxadd,name='admin_tax add'),
    path('admintaxadd_form_sub',views.admintaxadd_form_sub,name='admintaxadd_form_sub'),
    path('edit_taxlist/<int:id>',views.edit_taxlist,name='edit_taxlist'),
    path('edit_taxlist_update_form_sub/<int:id>',views.edit_taxlist_update_form_sub,name='edit_taxlist_update_form_sub'),
    path('edit_taxlist_delete/<int:id>',views.edit_taxlist_delete,name='edit_taxlist_delete'),

    path('admin_product list',views.adminproductlist,name='admin_product list'),
    path('admin_product add',views.adminproductadd,name='admin_product add'),
    path('adminproductadd_form_sub',views.adminproductadd_form_sub,name='adminproductadd_form_sub'),
    path('edit_product/<int:id>',views.edit_product,name='edit_product'),
    path('edit_product_update_form_sub/<int:id>',views.edit_product_update_form_sub,name='edit_product_update_form_sub'),
    path('edit_product_delete/<int:id>',views.edit_product_delete,name='edit_product_delete'),

    path('admin quotations list',views.adminquotationslist,name='admin quotations list'),
    path('admin_quotations add',views.adminquotationsadd,name='admin_quotations add'),
    path('adminquotationsadd_form_sub',views.adminquotationsadd_form_sub,name='adminquotationsadd_form_sub'),
    path('edit_quotation/<int:id>',views.edit_quotation,name='edit_quotation'),
    path('edit_quotation_update_form_sub/<int:id>',views.edit_quotation_update_form_sub,name='edit_quotation_update_form_sub'),
    path('edit_quotation_delete/<int:id>',views.edit_quotation_delete,name='edit_quotation_delete'),

    path('admin_purchase list',views.adminpurchaselist,name='admin_purchase list'),
    path('admin_purchase add',views.adminpurchaseadd,name='admin_purchase add'),
    path('admin_purchase_form_sub',views.admin_purchase_form_sub,name='admin_purchase_form_sub'),
    path('edit_purchase_list/<int:id>',views.edit_purchase_list,name='edit_purchase_list'),
    path('edit_purchase_list_update_form/<int:id>',views.edit_purchase_list_update_form,name='edit_purchase_list_update_form'),
    path('edit_purchase_list_delete/<int:id>',views.edit_purchase_list_delete,name='edit_purchase_list_delete'),

    path('admin_stock transfer list',views.adminstocktransferlist,name='admin_stock transfer list'),
    path('admin_stock transfer add',views.adminstocktransferadd,name='admin_stock transfer add'),
    path('stocktransfer_form_sub',views.stocktransfer_form_sub,name='stocktransfer_form_sub'),
    path('edit_stocktransfer/<int:id>',views.edit_stocktransfer,name='edit_stocktransfer'),
    path('edit_stocktransfer_update_form/<int:id>',views.edit_stocktransfer_update_form,name='edit_stocktransfer_update_form'),
    path('edit_stocktransfer_delete/<int:id>',views.edit_stocktransfer_delete,name='edit_stocktransfer_delete'),


    path('admin_sales list',views.adminsaleslist,name='admin_sales list'),
    path('admin_return product',views.adminreturnproduct,name='admin_return product'),
    path('admin_reg',views.admin_reg,name='admin_reg'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('contact_reg_sub',views.contact_reg_sub,name='contact_reg_sub'),
    
    



]