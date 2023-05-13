from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import File


# Register your models here.
# wagtailを経由せずに、modelを定義し、管理ページに反映させる
class FileAdmin(ModelAdmin):
    model = File  # modelのクラス
    menu_label = "提供された解答"  # モデルのlabel
    menu_icon = "download"  # icon
    menu_order = 290  # 1~999の整数、メニューの場所を返す。100より小さい場合トップに表示
    add_to_settings_menu = False  # menuのサブに入れる場合は、True
    exclude_from_explorer = False  # 検索に入れる場合、True
    list_display = ("title", "subtitle", "subfield", "subject", "year", "file", "file2", "file3", "file4", "file5", "date")  # 表示するフィールド
    search_fields = ("title", "subtitle", "file", "date")  # 検索結果を返すフィールド


# 登録してるclassを返す
modeladmin_register(FileAdmin)
