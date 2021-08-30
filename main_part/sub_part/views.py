from django.shortcuts import redirect, render
from . models import admin_reg_form_new,contact_reg,usermanagement_add_database_new,category_add_database_new,unit_add_database_new,taxadd_database_new,productadd_database_new,quotations_database_new,purchase_database_new,stocktransfer_database_new
from django.contrib import messages


#multi user login.
inventos_user_name=''
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
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=usermanagement_add_database_new.objects.all()

    return render(request,'admin user management view.html',{'inventos_data':inventos_data,'view_data':view_data})

def adminusermanagementadd(request):
     inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
     return render(request,'admin user management add.html',{'inventos_data':inventos_data}) 

def edit_usermanagement_add(request,id):
     inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
     view_data=usermanagement_add_database_new.objects.get(id=id)
     return render(request,'edit_usermanagement_add.html',{'inventos_data':inventos_data,'view_data':view_data})

def edit_usermanagement_add_update_form_sub(request,id):
    if request.method=='POST':
        if usermanagement_add_database_new.objects.filter(id=id).exists():
            ex1=usermanagement_add_database_new.objects.filter(id=id).update(email_id=request.POST['email_id'],
                                                                             password=request.POST['password'],
                                                                             
                                                                             confirm_password=request.POST['confirm_password'],
                                                                             selectstate1=request.POST['selectstate1'],
                                                                             selectstate2=request.POST['selectstate2'] )
            messages.error(request,'your data has been updated successfully',extra_tags='reg')
            return redirect(adminusermanagementview)
        else:
            return render(request,'edit_usermanagement_add.html')



def edit_usermanagement_delete(request,id):
    ex1=usermanagement_add_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been deleted successfully',extra_tags='reg')
    return redirect(adminusermanagementview)

       





def adminusermanagementadd_sub(request):
    if request.method=='POST':
        ex1=usermanagement_add_database_new(email_id=request.POST['email_id'],
                                       password=request.POST['password'],
                                       user_management_add_file=request.POST.get('user_management_add_file',False),
                                       confirm_password=request.POST['confirm_password'],
                                       selectstate1=request.POST['selectstate1'],
                                       selectstate2=request.POST['selectstate2'] )
        ex1.save()
        messages.error(request,'your data has saved successfully!...',extra_tags='reg') 
        return redirect(adminusermanagementview) 



    return render(request,'admin user management add.html')    


def admincategorylist(request):
    
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=category_add_database_new.objects.all()
    return render(request,'admin category list.html',{'inventos_data':inventos_data,'view_data':view_data})


def admincategoryadd(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    return render(request,'admincategoryadd .html',{'inventos_data':inventos_data})


def admincategoryadd_form_sub(request):
    if request.method=='POST':
        ex1=category_add_database_new(name=request.POST['name'],
                                      categoryadd_file=request.POST.get('categoryadd_file',False),
                                      category=request.POST['category'])
        ex1.save()
        messages.error(request,'your data has saved successfully!..',extra_tags='reg')
        return redirect(admincategorylist)
    
    return render(request,'admincategoryadd .html')

def edit_category_add(request,id):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=category_add_database_new.objects.get(id=id)
    return render(request,'edit_category_add.html',{'inventos_data':inventos_data,'view_data':view_data})

def edit_category_add_update_form_sub(request,id):
    if request.method=='POST':


        if category_add_database_new.objects.filter(id=id).exists():
            ex1=category_add_database_new.objects.filter(id=id).update(name=request.POST['name'],
                                                                      categoryadd_file=request.POST['categoryadd_file'],
                                                                      category=request.POST['category'])
            messages.error(request,'your data has updated successfully!!..',extra_tags='reg')
            return redirect(admincategorylist)
        else:
            return render(request,'edit_category_add.html')                                                            

def edit_category_delete(request,id):
    ex1=category_add_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been deleted successfully',extra_tags='reg')
    return redirect(admincategorylist)

    
    


        



def admin_unitlist(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=unit_add_database_new.objects.all()
    return render(request,'admin_unit list.html',{'inventos_data':inventos_data,'view_data':view_data})

def adminunitadd(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    return render(request,'admin unit add.html',{'inventos_data':inventos_data}) 

def adminunitadd_form_sub(request):
    if request.method=='POST':
        ex1=unit_add_database_new(product_code=request.POST['product_code'],
                                   sparepart_name=request.POST['sparepart_name']) 

        ex1.save()
        messages.error(request,'your data has been successfully saved!!!...',extra_tags='reg') 
        return redirect(admin_unitlist) 


    return render(request,'admin unit add.html')   

def edit_unitadd(request,id):
      inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
      view_data=unit_add_database_new.objects.get(id=id)
      return render(request,'edit_unitadd.html',{'inventos_data':inventos_data,'view_data':view_data})

def edit_unitadd_update_form_sub(request,id):
    if request.method=='POST':
        if unit_add_database_new.objects.filter(id=id).exists():
            ex1=unit_add_database_new.objects.filter(id=id).update(product_code=request.POST['product_code'],
                                                                     sparepart_name=request.POST['sparepart_name']   )

            messages.error(request,'Your data has been updated successfully',extra_tags='reg')
            return redirect(admin_unitlist) 

        else:

    
         return render(request,'edit_unitadd.html')

def edit_unitadd_delete(request,id):
    ex1=unit_add_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'Your data has deleted successfully',extra_tags='reg')
    return redirect(admin_unitlist)

   


def admintaxlist(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=taxadd_database_new.objects.all()
    return render(request,'admin_tax list.html',{'inventos_data':inventos_data,'view_data':view_data})

def admintaxadd(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    return render(request,'admin_tax add.html',{'inventos_data':inventos_data}) 

def admintaxadd_form_sub(request):
    if request.method=='POST':
        ex1=taxadd_database_new( tax_name=request.POST['tax_name'],
                                  Item_name=request.POST['Item_name'],
                                  tax=request.POST['tax'] )
        ex1.save()
        messages.error(request,'your data has successfully saved!...',extra_tags='reg') 
        return redirect(admintaxlist)

        return render(request,'admin_tax add.html')


def edit_taxlist(request,id):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=taxadd_database_new.objects.get(id=id)
    return render(request,'edit_taxlist.html',{'inventos_data':inventos_data,'view_data':view_data})

def edit_taxlist_update_form_sub(request,id):
    if request.method=='POST':
        if taxadd_database_new.objects.filter(id=id).exists():
            ex1=taxadd_database_new.objects.filter(id=id).update(tax_name=request.POST['tax_name'],
                                                                 Item_name=request.POST['Item_name'],
                                                                 tax=request.POST['tax'])
            
            
            messages.error(request,'Your data has updated successfully',extra_tags='reg')
            return redirect(admintaxlist)

        else:
             
              return render(request,'edit_tax list.html') 

def edit_taxlist_delete(request,id):
    ex1=taxadd_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'Your data has deleted successfully',extra_tags='reg')
    return redirect(admintaxlist)
                

            

                                               


def adminproductlist(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=productadd_database_new.objects.all()
    return render(request,'admin_product list.html',{'inventos_data':inventos_data,'view_data':view_data})

def adminproductadd(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    return render(request,'admin_product add.html',{'inventos_data':inventos_data})


def adminproductadd_form_sub(request):
    if request.method=='POST':
        ex1=productadd_database_new(category=request.POST['category'],
                                    select_brand=request.POST['select_brand'],
                                    select_unit=request.POST['select_unit'],
                                    enter_barcode=request.POST['enter_barcode'],
                                    product_cost=request.POST['product_cost'],
                                    sales_price=request.POST['sales_price'],
                                    quantatity=request.POST['quantatity'],
                                    tax_type=request.POST['tax_type'],
                                    product_name=request.POST['product_name']  )
        ex1.save()
        messages.error(request,'your data has saved successfully!....',extra_tags='reg')
        return redirect(adminproductlist)

    return render(request,'admin_product list.html')    

def edit_product(request,id):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=productadd_database_new.objects.get(id=id)
    return render(request,'edit_product.html',{'inventos_data':inventos_data,'view_data':view_data}) 

def  edit_product_update_form_sub(request,id):
    if request.method=='POST':
        if productadd_database_new.objects.filter(id=id).exists():
            ex1=productadd_database_new.objects.filter(id=id).update(category=request.POST['category'],
                                                                      select_brand=request.POST['select_brand'],
                                                                      select_unit=request.POST['select_unit'],
                                                                      enter_barcode=request.POST['enter_barcode'],
                                                                      product_cost=request.POST['product_cost'],
                                                                      sales_price=request.POST['sales_price'],
                                                                      quantatity=request.POST['quantatity'],
                                                                      tax_type=request.POST['tax_type'],
                                                                      product_name=request.POST['product_name']  )

            messages.error(request,'Your data has updated successfully',extra_tags='reg')  
            return redirect(adminproductlist) 

    else:                                                       

     return render(request,'edit_product.html')  

def edit_product_delete(request,id):
    ex1=productadd_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'Your data has deleted successfully',extra_tags='reg')
    return redirect(adminproductlist)

    
            


def adminquotationslist(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=quotations_database_new.objects.all()
    return render(request,'admin quotations list.html',{'inventos_data':inventos_data,'view_data':view_data})

def adminquotationsadd(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    return render(request,'admin_quotations add.html',{'inventos_data':inventos_data})

def adminquotationsadd_form_sub(request):
    if request.method=='POST':
        ex1=quotations_database_new(from_warehouse=request.POST['from_warehouse'],
                                     to_warehouse=request.POST['to_warehouse'],
                                     shipping_cost=request.POST['shipping_cost'],
                                      select_state=request.POST['select_state'],
                                      product_name=request.POST['product_name'],
                                      quantatity=request.POST['quantatity'] )
        ex1.save()
        messages.error(request,'Your data has saved successfully',extra_tags='reg')
        return redirect(adminquotationslist)                               

    return render(request,'admin_quotations add.html')  

def edit_quotation(request,id):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=quotations_database_new.objects.get(id=id)
    return render(request,'edit_quotation.html',{'inventos_data':inventos_data,'view_data':view_data})

def edit_quotation_update_form_sub(request,id):
    if request.method=='POST':
        if quotations_database_new.objects.filter(id=id).exists():
            ex1=quotations_database_new.objects.filter(id=id).update(from_warehouse=request.POST['from_warehouse'],
                                                                     to_warehouse=request.POST['to_warehouse'],
                                                                     shipping_cost=request.POST['shipping_cost'],
                                                                     select_state=request.POST['select_state'],
                                                                     product_name=request.POST['product_name'],
                                                                     quantatity=request.POST['quantatity'] )

            messages.error(request,'Your data updated successfully!..',extra_tags='reg') 
            return redirect(adminquotationslist)
    else:
        return render(request,'edit_quotation.html')   


def edit_quotation_delete(request,id):
    ex1=quotations_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'Your data has deleted successfully',extra_tags='reg')
    return redirect(adminquotationslist)

    



     

def adminpurchaselist(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=purchase_database_new.objects.all()
    return render(request,'admin_purchase list.html',{'inventos_data':inventos_data,'view_data':view_data})

def adminpurchaseadd(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    return render(request,'admin_purchase add.html')

def admin_purchase_form_sub(request):
    if request.method=='POST':
        ex1=purchase_database_new(Destination=request.POST['Destination'],
                                   Supplier=request.POST['Supplier'],
                                    Description=request.POST['Description'],
                                    Total_Amount=request.POST['Total_Amount'],
                                    Paid_Amount=request.POST['Paid_Amount'],
                                    Due=request.POST['Due'] )

        ex1.save()
        messages.error(request,'Your data has saved successfully!..',extra_tags='reg')
        return redirect(adminpurchaselist)

def edit_purchase_list(request,id):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=purchase_database_new.objects.get(id=id)
    return render(request,'edit_purchase.html',{'inventos_data':inventos_data,'view_data':view_data})
   

def edit_purchase_list_update_form(request,id):
    if request.method=='POST':
        if purchase_database_new.objects.filter(id=id).exists():
            ex1=purchase_database_new.objects.filter(id=id).update( Destination=request.POST['Destination'],
                                                                    Supplier=request.POST['Supplier'],
                                                                    Description=request.POST['Description'],
                                                                    Total_Amount=request.POST['Total_Amount'],
                                                                    Paid_Amount=request.POST['Paid_Amount'],
                                                                    Due=request.POST['Due']  )

            messages.error(request,'Your data has updated successfully',extra_tags='reg')
            return redirect(adminpurchaselist) 
    else:        

        return render(request,'edit_purchase.html')

def edit_purchase_list_delete(request,id):
    ex1=purchase_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'Your data has deleted successfully!..',extra_tags='reg')
    return redirect(adminpurchaselist)



def adminstocktransferlist(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=stocktransfer_database_new.objects.all()
    return render(request, 'admin_stock transfer list.html',{'inventos_data':inventos_data,'view_data':view_data})

def adminstocktransferadd(request):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    return render(request,'admin_stock transfer add.html')


def stocktransfer_form_sub(request):
    if request.method=='POST':
        ex1=stocktransfer_database_new(Source=request.POST['Source'],
                                        Destination=request.POST['Destination'],
                                        Description=request.POST['Description'],
                                        Product_Name=request.POST['Product_Name'],
                                        stocks_info=request.POST['stocks_info'],
                                        Shipping_Cost=request.POST['Shipping_Cost'],
                                        Total_Amount=request.POST['Total_Amount'])
        ex1.save()
        messages.error(request,'Your data has saved successfully',extra_tags='reg')
        return redirect(adminstocktransferlist)
    
def edit_stocktransfer(request,id):
    inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)
    view_data=stocktransfer_database_new.objects.get(id=id)
    return render(request,'edit_stocktransfer.html',{'inventos_data':inventos_data,'view_data':view_data})
    
def  edit_stocktransfer_update_form(request,id):
    if request.method=='POST':
        if stocktransfer_database_new.objects.filter(id=id).exists():
            ex1=stocktransfer_database_new.objects.filter(id=id).update(Source=request.POST['Source'],
                                                                        Destination=request.POST['Destination'],
                                                                        Description=request.POST['Description'],
                                                                        Product_Name=request.POST['Product_Name'],
                                                                        stocks_info=request.POST['stocks_info'],
                                                                        Shipping_Cost=request.POST['Shipping_Cost'],
                                                                        Total_Amount=request.POST['Total_Amount'] )

            messages.error(request,'Your data has updated successfully',extra_tags='reg')
            return redirect(adminstocktransferlist) 

def edit_stocktransfer_delete(request,id):
    ex1=stocktransfer_database_new.objects.get(id=id)
    ex1.delete()
    messages.error(request,'Your data has deleted successfully',extra_tags='reg')
    return redirect(adminstocktransferlist)            


def adminsaleslist(request):
    return render(request,'admin_sales list.html') 
def adminreturnproduct(request):
    return render(request,'admin_return product.html')
def admin_reg(request):
    if request.method=='POST':

        if admin_reg_form_new.objects.filter(user_name=request.POST['user_name']).exists():
            messages.error(request,'This username  has already taken!!..',extra_tags='login')
        elif admin_reg_form_new.objects.filter(email_id=request.POST['email_id']):
            
            messages.error(request,'This email id has already taken!!..',extra_tags='login')

        else:


         ex1=admin_reg_form_new(user_name=request.POST['user_name'],
                               password=request.POST['password'],
                               repeat_password=request.POST['repeat_password'],
                               email_id=request.POST['email_id'] )

         ex1.save()     
         messages.error(request,'your data has been saved successfully',extra_tags='reg')       
         return render(request,'adminlogin.html')       
                        
        
    return render(request,'adminlogin.html') 

def adminlogin(request):

    if request.method=='POST':
        if admin_reg_form_new.objects.filter(user_name=request.POST['user_name'],password=request.POST['password'],).exists():
           ex1=admin_reg_form_new.objects.get(user_name=request.POST['user_name'],password=request.POST['password'],)


  
           global inventos_user_name

           inventos_user_name=ex1.user_name
           print('check:',inventos_user_name)
           inventos_data=admin_reg_form_new.objects.get(user_name=inventos_user_name)


           return render(request,'adminindex.html',{'inventos_data':inventos_data})
             
        else:

            messages.error(request,'your username or password is incorrect',extra_tags='login')
            return render(request,'adminlogin.html')


    return render(request,'adminlogin.html')
def contact_reg_sub(request):
    if request.method=='POST':
        ex1=contact_reg(user_name=request.POST['user_name'],
                        email_id=request.POST['email_id'],
                        subject=request.POST['Subject'],
                        messages=request.POST['messages'])
        ex1.save()
        messages.error(request,'your contact detail have been saved successfully',extra_tags='contact')
        return render(request,'contact.html')
          
                                                                           
    

         