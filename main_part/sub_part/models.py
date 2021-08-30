from django.db import models

# Create your models here.
class admin_reg_form_new(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    repeat_password=models.CharField(max_length=100)
    email_id=models.EmailField()

    def __str__(self):
        return self.user_name

class contact_reg(models.Model):

    user_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    subject=models.CharField(max_length=100)
    messages=models.TextField()

class usermanagement_add_database_new(models.Model):
    email_id=models.EmailField()
    password=models.CharField(max_length=100)
    user_management_add_file=models.FileField(upload_to='documents',null=True)
    confirm_password=models.CharField(max_length=100)
    selectstate1=models.CharField(max_length=100)
    selectstate2=models.CharField(max_length=100)

    def __str__(self):
        return self.email_id

class category_add_database_new(models.Model):
    name=models.CharField(max_length=100)
    categoryadd_file=models.FileField(upload_to='documents',null=True)
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class unit_add_database_new(models.Model):
    product_code=models.CharField(max_length=100)
    sparepart_name=models.CharField(max_length=100)

    def __str__(self):
        return self.product_code

class taxadd_database_new(models.Model):
    tax_name=models.CharField(max_length=100)
    Item_name=models.CharField(max_length=100)
    tax=models.CharField(max_length=100)

    def __str__(self):
        return self.Item_name  

class productadd_database_new(models.Model):
    category=models.CharField(max_length=100)
    select_brand=models.CharField(max_length=100)  
    select_unit=models.CharField(max_length=100) 
    enter_barcode=models.CharField(max_length=100) 
    product_cost=models.CharField(max_length=100) 
    sales_price=models.CharField(max_length=100) 
    quantatity=models.CharField(max_length=100) 
    tax_type=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)             

    def __str__(self):
        return self.category
        

class quotations_database_new(models.Model):
    from_warehouse=models.CharField(max_length=100)
    to_warehouse=models.CharField(max_length=100)
    shipping_cost=models.CharField(max_length=100)
    select_state=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    quantatity=models.CharField(max_length=100)
    
     

    def __str__(self):
        return self.select_state 


class purchase_database_new(models.Model):
    Destination=models.CharField(max_length=100)
    Supplier=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Total_Amount=models.CharField(max_length=100)
    Paid_Amount=models.CharField(max_length=100)
    Due=models.CharField(max_length=100)

    def __str__(self):
        return self.Supplier 

class stocktransfer_database_new(models.Model):
    Source=models.CharField(max_length=100)
    Destination=models.CharField(max_length=100) 
    Description=models.CharField(max_length=100)
    Product_Name=models.CharField(max_length=100)
    stocks_info=models.CharField(max_length=100)
    Shipping_Cost=models.CharField(max_length=100)
    Total_Amount=models.CharField(max_length=100)

    def __str__(self):
        return self.Product_Name






            


    

    
