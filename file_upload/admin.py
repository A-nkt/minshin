from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import File

# Register your models here.
class FileAdmin(ModelAdmin):
    model = File
    menu_label = "アップロードファイル"
    menu_icon = "download"
    menu_order=290
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("title","subtitle","subfield","year","file","date")
    search_fields=("title","subtitle","file","date")

modeladmin_register(FileAdmin)
