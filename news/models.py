from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel,MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from streams import blocks
import datetime


#from streams import blocks

# Create your models here.
class NewsPage(RoutablePageMixin,Page):
    template="news/news.html"#対応するhtmlファイルを指定

    subpage_types=[
    'ArticlePage',
    ]

    main_title=models.CharField(max_length=100,blank=True,null=True,default='')

    content_panels=Page.content_panels + [
        FieldPanel("main_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts=ArticlePage.objects.live().public().order_by('-first_published_at')
        paginator=Paginator(all_posts,5)

        page = request.GET.get("page")
        try:
            posts=paginator.page(page)
        except PageNotAnInteger:
            posts=paginator.page(1)
        except EmptyPage:
            posts=paginator.page(paginator.num_pages)
        context["posts"] =posts
        context["categories"] =ArticlePage.objects.all()


        return context

    @route(r"^year/(\d+)/$") #,name=news_by_year)
    def news_by_year(self,request,year):
        context = self.get_context(request,year)
        context["posts"] =ArticlePage.objects.live().public().order_by('-first_published_at').filter(year=year)
        context = {
            'context': context,
            "year": year,
        }

        return render(request,"news/related.html",context)


class ArticlePage(NewsPage):
    template="news/article.html"#対応するhtmlファイルを指定

    main_text=RichTextField(_('メインコンテンツ'), max_length=300,blank=True,null=True)
    ヘッダー画像=models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    date=models.DateField(null=True,default=datetime.date.today)
    year=models.IntegerField(default=datetime.datetime.now().year)


    content_panels=Page.content_panels + [
        ImageChooserPanel("ヘッダー画像"),
        FieldPanel("main_text"),
        #FieldPanel("date"),
        #FieldPanel("year"),
    ]
