from django.db import models

# Create your models here.
class admin_reg_form(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    repeat_password=models.CharField(max_length=100)
    mail_id=models.EmailField()

    def __str__(self):
        return self.user_name




            


    

    
