from django.db import models

# Client User model 
class client_user(models.Model):
    first_name = models.CharField(max_lenght=30)
    last_name = models.CharField(max_lenght=30)
    email_address = models.CharField(max_lenght=30)
    password = models.CharField(max_lenght=30)
    Phone_number = models.CharField(max_lenght=30)
    mobile_number = models.CharField(max_lenght=30)
    account = models.CharField(max_lenght=30)
    
# Admin User Model 
class admin_user(models.Models):
    first_name = models.CharField(max_lenght=30)
    last_name = models.CharField(max_lenght=30)
    email_address = models.CharField(max_lenght=30)
    Phone_number = models.CharField(max_lenght=30)
    mobile_number = models.CharField(max_lenght=30)
    account = models.CharField(max_lenght=30)

class account(models.Models):
    account_number = models.AutoField(primary_key=True)           # Primary Key linked 
    account_name = models.CharField(max_lenght=30)
    website_name = models.CharField(max_lenght=30)
    Phone_number = models.CharField(max_lenght=30)
    webste_address = models.CharField(max_lenght=30)
    account = models.CharField(max_lenght=30)                     # Should link to Hubtree Account as a tree