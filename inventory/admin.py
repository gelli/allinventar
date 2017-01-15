from django.contrib import admin

from .models import MaterialGroup
from .models import MaterialStatus
from .models import Material
from .models import InventoryItem
# Register your models here.

admin.site.register(MaterialGroup)
admin.site.register(Material)
admin.site.register(InventoryItem)
admin.site.register(MaterialStatus)
