from wagtail.core import blocks

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
