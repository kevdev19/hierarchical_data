from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Folder

admin.site.register(Folder, MPTTModelAdmin)