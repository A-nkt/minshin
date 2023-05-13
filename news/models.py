import datetime

from django.db import models
from django.shortcuts import render
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.utils.translation import ugettext_lazy as _


# ニュース一覧ページ

class NewsPage(RoutablePageMixin, Page):
    template = "news/news.html"
    subpage_types = [
        'ArticlePage',
    ]
    # コンテンツの定義
    main_title = models.CharField(max_length=100, blank=True, null=True, default='')
    content_panels = Page.content_panels + [
        FieldPanel("main_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts = ArticlePage.objects.live().public().order_by('-first_published_at')
        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_posts = all_posts.filter(tags__name=tags)
        else:
            tags = ""

        paginator = Paginator(all_posts, 10)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context["posts"] = posts
        context["tags"] = tags
        return context

    @route(r'^year/(\d+)/$')
    def news_by_year(self, request, year):
        context = self.get_context(request, year)
        context["posts"] = ArticlePage.objects.live().public().order_by('-first_published_at').filter(year=year)
        context = {
            'context': context,
            "year": year,
        }
        return render(request, "news/related.html", context)


class PageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ArticlePage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class ArticlePage(NewsPage):
    template = "news/article.html"
    main_text = RichTextField(_('メインコンテンツ'), max_length=10000, blank=True, null=True)
    ヘッダー画像 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    date = models.DateField(null=True, default=datetime.date.today)
    year = models.IntegerField(default=datetime.datetime.now().year)
    tags = ClusterTaggableManager(through=PageTag, blank=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel("ヘッダー画像"),
        FieldPanel("main_text"),
        FieldPanel("tags"),
    ]
