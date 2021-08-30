from django.contrib import admin

# Register your models here.
from . models import admin_reg_form_new,contact_reg,usermanagement_add_database_new,category_add_database_new,unit_add_database_new,taxadd_database_new,productadd_database_new,quotations_database_new, purchase_database_new,stocktransfer_database_new




admin.site.register(admin_reg_form_new)
admin.site.register(contact_reg)
admin.site.register(usermanagement_add_database_new)
admin.site.register(category_add_database_new)
admin.site.register(unit_add_database_new)
admin.site.register(taxadd_database_new)
admin.site.register(productadd_database_new) 
admin.site.register(quotations_database_new)
admin.site.register(purchase_database_new)
admin.site.register(stocktransfer_database_new)

