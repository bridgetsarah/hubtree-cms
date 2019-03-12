from django.conf import settings
from django.db import models
from django.utils import timezone
from hubplatform.apps.dash import views
from OpenGL.WGL.EXT import display_color_table

# Level 0  [Defining Variables temp] -----------------------------------------------------------------------------------------------------

admin_dash = ('admin_dash')
baseproject = ('base_project')
basebilling = ('base_billing')
baseusers = ('baseusers')



# Level 1 [Base Level]---------------------------------------------------------------------------------------------------------------------
class base_dashboard(models.Model):
    views (admin_dash),                                                    # View Admin dashboard [page]
    views (baseproject),                                                   # View Projects [Page]
    views (basebilling),                                                   # View Billing [Page]
    views (baseusers),                                                     # View Users [page]
    
# Base Project
class baseproject(models.Model):                                            # Base Project Level 1
    Create_Project = models.ForeignKey                                      # Assigned Unique project ID Number
    Create_Project_name = models.TextField()                                # Assigned Project Name
    Create_Project_domain = models.TextField()                              # Assigned Project Domain etc (www.hubtree.com)
    Created_date = models.DateTimeField(default=timezone.now)               # Assigned Project creation date

# Base Billing
class basebilling(models.Model):
    create_order_po = models.ForeignKey                                     # Creates Unique purchase order number
    assign_client = models.TextField()                                      # Assigns order to "client" e.g Jane Doe
    Project_name = models.TextField()                                       # Assigns to project name e.g Batmans Project
    
# Base users
class baseusers(models.Model):
    Create_firstname = models.TextField                                     # Assigned Unique project ID Number
    Create_last_name = models.TextField()                                   # Assigned Project Name
    Create_Project_domain = models.TextField()                              # Assigned Project Domain etc (www.hubtree.com)
    Created_date = models.DateTimeField(default=timezone.now)               # Assigned Project creation date


# Level 2  [User input] -------------------------------------------------------------------------------------------------------------------
class project(models.Model):
    Project_name = models.TextField()
    Project_timeline = models.TextField()
    Project_status = models.TextField()
    Project_domain= models.TextField()
    project_email = models.CharField()
    Project_client = models.TextField()


class user(models.Model):
#?  display_color_table 
    first_name = models.TextField()
    last_name = models.TextField()
    email_address = models.CharField()


# Level 3 [       ] -------------------------------------------------------------------------------------------------------------------------

