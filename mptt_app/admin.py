from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin 

from .models import Folder

admin.site.register(Folder, DraggableMPTTAdmin)