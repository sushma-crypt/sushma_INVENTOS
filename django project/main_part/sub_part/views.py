from django.shortcuts import redirect, render
from . models import admin_reg_form
from django.contrib import messages

import easygui
# Create your views here.
def index(request):
    return render(request,'index.html')
def category(request):
    return render(request,'category.html')
def about(request):
    return render(request,'about.html')
def orders(request):
    return render(request,'orders.html')  
def bestselling(request):
    return render(request,'bestselling.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
 
def dashboard(request):
    return render(request,'dashboard.html')
def userlogin(request):
    return render(request,'userlogin.html')  
def adminindex(request):
    return render(request,'adminindex.html')
def adminusermanagementview(request):
    return render(request,'admin user management view.html') 
def adminusermanagementadd(request):
    return render(request,'admin user management add.html') 
def admincategorylist(request):
    return render(request,'admin category list.html') 
def admincategoryadd(request):
    return render(request,'admincategoryadd .html') 
def admin_unitlist(request):
    return render(request,'admin_unit list.html')
def adminunitadd(request):
    return render(request,'admin unit add.html') 
def admintaxlist(request):
    return render(request,'admin_tax list.html')
def admintaxadd(request):
    return render(request,'admin_tax add.html') 
def adminproductlist(request):
    return render(request,'admin_product list.html')
def adminproductadd(request):
    return render(request,'admin_product add.html')
def adminquotationslist(request):
    return render(request,'admin quotations list.html')
def adminquotationsadd(request):
    return render(request,'admin_quotations add.html')
def adminpurchaselist(request):
    return render(request,'admin_purchase list.html')
def adminpurchaseadd(request):
    return render(request,'admin_purchase add.html')
def adminstocktransferlist(request):
    return render(request, 'admin_stock transfer list.html')
def adminstocktransferadd(request):
    return render(request,'admin_stock transfer add.html')
def adminsaleslist(request):
    return render(request,'admin_sales list.html') 
def adminreturnproduct(request):
    return render(request,'admin_return product.html')
def admin_reg_form_new(request):
    if request.method=='POST':
        ex1=admin_reg_form(user_name=request.POST['user_name'],
                             password=request.POST['password'],
                             repeat_password=request.POST['repeat_password'],
                             mail_id=request.POST['mail_id'])
        ex1.save() 
        easygui.msgbox('your data has saved successfully') 
        return render(request,'adminlogin.html')
    

   

  
               
def adminlogin(request):
    if request.method=='POST':
        if admin_reg_form.objects.filter(user_name=request.POST['user_name'],password=request.POST['password']).exists():
            ex1=admin_reg_form.objects.get(user_name=request.POST['user_name'],password=request.POST['password'])
            easygui.msgbox('Logged succesfully..!!')
            return render(request,'adminindex.html',{'ex1':ex1})
        else:
            easygui.msgbox('Enter valid username and password..!!')
            return render(request,'adminlogin.html')
    return render(request,'adminlogin.html')
                                                                           
    

         