from django.db import models
from django.utils import timezone

# Create your models here.
class File(models.Model):
    date= models.DateTimeField(default=timezone.now)
    title = models.CharField(verbose_name='大学名',max_length=200)
    subtitle = models.CharField(verbose_name='研究科名', max_length=100,null=True)
    subfield = models.CharField(verbose_name='専攻以下', max_length=100,null=True)
    year=models.IntegerField(verbose_name='年度',default=2019)
    file = models.FileField(verbose_name='過去問',upload_to='past/')


    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name="Upload Page"
        verbose_name_plural="Upload Pages"
