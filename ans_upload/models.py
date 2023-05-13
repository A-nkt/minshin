from django.db import models
from django.utils import timezone


# みんなの過去問、解答アップロードフォームページ
class File(models.Model):
    date = models.DateTimeField(default=timezone.now)  # 投稿日
    title = models.CharField(verbose_name='大学名', help_text='<p></p>', max_length=200)  # 大学名
    subtitle = models.CharField(verbose_name='研究科名', help_text='<p></p>', max_length=100, null=True)  # 研究科名
    subfield = models.CharField(verbose_name='専攻以下', help_text='<p>できるだけ正確に記入してください</p>', max_length=100, null=True)  # 専攻
    subject = models.CharField(verbose_name='教科等', help_text='<p></p>', max_length=100, null=True)  # 教科
    year = models.IntegerField(verbose_name='年度', help_text='<p>解答した年を入力してください<br>(例)2020年入学者用問題→2019年</p>', default=2019)  # 過去問年度
    file = models.FileField(verbose_name='過去問解答', upload_to='past/', blank=True)  # 解答データ
    file2 = models.FileField(verbose_name='', upload_to='past/', blank=True)
    file3 = models.FileField(verbose_name='', upload_to='past/', blank=True)
    file4 = models.FileField(verbose_name='', upload_to='past/', blank=True)
    file5 = models.FileField(verbose_name='', upload_to='past/', blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Ans_Upload Page"
        verbose_name_plural = "Ans_Upload Pages"
