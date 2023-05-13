from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from streams import blocks


# 大学紹介ページ
class MintoPage(Page):
    template = "minto/minto_page.html"
    subpage_types = [
        'ContentsPage',
    ]
    # Blockを使って、要素が可変的なモデルを定義
    UNIV = StreamField(
        [("UNIV", blocks.MintoUniversity())],
        null=True, blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('UNIV'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts = ContentsPage.objects.live().public()
        paginator = Paginator(all_posts, 8)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context["posts"] = posts
        return context


# 研究科ごとのチャート
class ContentsPage(MintoPage):
    template = "minto/contents.html"
    INDEX = StreamField(
        [("INDEX", blocks.MintoContentIndex())],
        null=True,
        blank=True,
    )
    VALUE = StreamField(
        [
            ("INDEX", blocks.MintoContentValue()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel('INDEX'),
        StreamFieldPanel('VALUE'),
    ]
