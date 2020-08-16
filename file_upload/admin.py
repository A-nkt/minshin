from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import File

# Register your models here.
class FileAdmin(ModelAdmin):#wagtailを経由せずに、modelを定義し、管理ページに反映させる
    model = File#modelのクラス
    menu_label = "アップロードファイル"#モデルのlabel
    menu_icon = "download"#icon
    menu_order=290#1~999の整数、メニューの場所を返す。100より小さい場合トップに表示
    add_to_settings_menu=False#menuのサブに入れる場合は、True
    exclude_from_explorer=False#検索に入れる場合、True
    list_display=("title","subtitle","subfield","year","file","date")#表示するフィールド
    search_fields=("title","subtitle","file","date")#検索結果を返すフィールド

modeladmin_register(FileAdmin)#登録してるclassを返す
