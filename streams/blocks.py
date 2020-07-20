from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    title=blocks.CharBlock(required=True,help_text="Add your title")
    text=blocks.RichTextBlock()

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

#class SubTitleBlock(blocks.RichTextBlock):
#    class Meta:
#        template="streams/Subtitle_block.html"
#        icon="edit"
#        label="SubtitleText"
