from django.db import models


# コンテンツモデルと投稿モデルを別個に定義してみる
class Comment(models.Model):
    CONFIDENCE = (
        (0, '値を選択してください'),
        (1, '合ってる(8割)'),
        (2, '概ね合ってる（6割）'),
        (3, 'あまり合っていない（４割）'),
        (4, '合ってない(４割以下)'),
        (5, 'その他・コメント')
    )

    # 投稿者の名前
    name = models.CharField(blank=True, null=True, max_length=100, help_text="name")
    # コメント
    message = models.TextField(max_length=300)
    # 日時
    date = models.DateField(verbose_name='打刻日', blank=True, null=True)
    # 正答率
    rate = models.IntegerField(verbose_name='正答率', choices=CONFIDENCE, default=None)
    # 大学名
    univ = models.CharField(blank=True, null=True, max_length=100)
    # 教科と試験年
    subject_year = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        template = '{0.name} ' + ',' + '{0.univ}' + ',' + '{0.subject_year}'
        return template.format(self)


class Image(models.Model):
    answer = models.ImageField(upload_to='upload/')
    univ = models.CharField(blank=True, null=True, max_length=100)
    subject_year = models.CharField(blank=True, null=True, max_length=100)
    post = models.ForeignKey(Comment, verbose_name='投稿', on_delete=models.CASCADE, blank=True, null=True)
