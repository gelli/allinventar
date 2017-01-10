from django.contrib import admin

from .models import MaterialGroup
from .models import Material
from .models import Inventory
# Register your models here.

admin.site.register(MaterialGroup)
admin.site.register(Material)
admin.site.register(Inventory)
