#core/apps.py
#Here, we created a new AdminConfig,
# which loads our CustomAdminSite instead of Django's default one.
#Replace the default AdminConfig with the new one in core/settings.py:
from django.contrib.admin.apps import  AdminConfig

class CustomAdminConfig(AdminConfig):
    default_site = 'core.admin.CustomAdminSite'