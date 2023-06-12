from django.contrib import admin
from .models import Item, Image, File, Theme, Commentary

# Register your models here.


admin.site.register(Item)
admin.site.register(Image)
admin.site.register(File)
admin.site.register(Theme)
admin.site.register(Commentary)