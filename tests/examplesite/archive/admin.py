from examplesite.archive.models import Image,Album
from django.contrib import admin

from django.contrib.admin.widgets import AdminFileWidget
from picasa import  PicasaField,  PicasaAdminImageWidget

class ImageAdmin(admin.ModelAdmin):     
        formfield_overrides = {PicasaField: {'widget': PicasaAdminImageWidget},}
admin.site.register(Image, ImageAdmin)
admin.site.register(Album)