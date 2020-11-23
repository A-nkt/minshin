from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import ugettext_lazy as _

class TitleAndTextBlock(blocks.StructBlock):
    title=blocks.CharBlock(required=True,help_text="Add your title")
    #text=blocks.RichTextBlock()

    class Meta:
        template="streams/title_and_text_block.html"
        icon="edit"
        label="Title & Text"

class RichtextBlock(blocks.RichTextBlock):
    subtext=blocks.RichTextBlock()
    class Meta:
        template="streams/richtext_block.html"
        icon="edit"
        label="Full RichText"

class TitleAndTextBlockAns(blocks.StructBlock):
    title=blocks.CharBlock(required=True,help_text="Add your title")
    #text=blocks.RichTextBlock()

    class Meta:
        template="streams/title_and_text_block_ans.html"
        icon="edit"
        label="見出し"

class RichtextBlockAns(blocks.StructBlock):
    subject=blocks.RichTextBlock()
    links=blocks.CharBlock(max_length=100,blank=True,null=True,help_text="Add about title")
    class Meta:
        template="streams/richtext_block_ans.html"
        icon="edit"
        label="教科リンク"

class NewsTitleBlock(blocks.StructBlock):
    title=blocks.CharBlock(max_length=100,blank=True,null=True,help_text="Add news title")
    link=blocks.CharBlock(max_length=100,blank=True,null=True,help_text="Add news link")
    class Meta:
        template="streams/news.html"
        icon="edit"
        label="Title"

class AboutTitleBlock(blocks.StructBlock):
    title=blocks.CharBlock(max_length=100,blank=True,null=True,help_text="Add about title")
    text=blocks.RichTextBlock(max_length=1000,blank=True,null=True,help_text="Add about content")
    class Meta:
        template="streams/about.html"
        icon="edit"
        label="Title"

class RuleTitleBlock(blocks.StructBlock):
    title=blocks.RichTextBlock(max_length=100,blank=True,null=True,help_text="Add about title")
    text=blocks.RichTextBlock(max_length=1000,blank=True,null=True,help_text="Add about content")
    class Meta:
        template="streams/rule.html"
        icon="edit"
        label="Title"

class RuleDate(blocks.StructBlock):
    date=blocks.RichTextBlock(max_length=1000,blank=True,null=True,help_text="Add your Date")
    class Meta:
        template="streams/rule_date.html"
        icon="edit"
        label="Date"

class MintoUniversity(blocks.StructBlock):
    name = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="大学名")
    sub = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="区分/地名")
    link = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="大学名のリンク")
    text = blocks.TextBlock(require=True)
    images = ImageChooserBlock(label=_("Image"))

    class Meta:
        template = "streams/MintoUniversity.html"
        icon = "edit"
        label = "Univ"

class MintoUnivResearch(blocks.StructBlock):
    name = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="研究科名")
    link = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="研究科名のリンク")
    class Meta:
        template = "streams/MintoUnivResearch.html"
        icon = "edit"
        label = "研究科名"

class MintoContentIndex(blocks.StructBlock):
    name = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="大学名")
    link = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="大学名のリンク")

    class Meta:
        template = "streams/MintoContentIndex.html"
        icon = "edit"
        label = "INDEX"

class MintoContentValue(blocks.StructBlock):
    research_name = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="研究科名")
    IDname = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="IDname")
    RinkID = blocks.CharBlock(max_length=100,blank=True,null=True,help_text="RinkID")
    int1 = blocks.IntegerBlock(blank=True,null=True,help_text="500~600点")
    int2 = blocks.IntegerBlock(blank=True,null=True,help_text="600~700点")
    int3 = blocks.IntegerBlock(blank=True,null=True,help_text="700~800点")
    int4 = blocks.IntegerBlock(blank=True,null=True,help_text="800~900点")
    int5 = blocks.IntegerBlock(blank=True,null=True,help_text="900点以上")

    class Meta:
        template = "streams/MintoContentValue.html"
        icon = "edit"
        label = "INDEX"
