# Generated by Django 2.2.17 on 2020-12-23 15:40

import cms.home.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0008_create_richtext_col_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('columns', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('externlink', wagtail.core.blocks.URLBlock(help_text='The external link overwrites the link to a local page. It also requires a link text.', label='External Link', required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, the title of the linked page will be used.', required=False))], required=True)), ('col2', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('externlink', wagtail.core.blocks.URLBlock(help_text='The external link overwrites the link to a local page. It also requires a link text.', label='External Link', required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, the title of the linked page will be used.', required=False))], required=True)), ('col3', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('externlink', wagtail.core.blocks.URLBlock(help_text='The external link overwrites the link to a local page. It also requires a link text.', label='External Link', required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, the title of the linked page will be used.', required=False))], required=True))])), ('call_to_action', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))], required=True)), ('text', wagtail.core.blocks.TextBlock(required=True))])), ('idea_carousel', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(required=False)), ('year', cms.home.blocks.ProjectChooserBlock(required=False)), ('field_of_action', wagtail.core.blocks.ChoiceBlock(choices=[('CD', 'Community development'), ('SI', 'Social inclusion'), ('ES', 'Environment and sustainability'), ('AC', 'Arts and cultural activities'), ('HR', 'Human rights'), ('YP', 'Youth participation and empowerment'), ('JL', 'Journalism'), ('SE', '(Social) Entrepreneurship'), ('OT', 'Other')], required=False)), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('newest', 'Most recent'), ('comments', 'Most comments'), ('support', 'Most support'), ('title', 'Alphabetical')], required=False)), ('status', wagtail.core.blocks.ChoiceBlock(choices=[('community_award', 'Community Award Winner'), ('shortlist', 'Shortlist'), ('winner', 'Winner')], required=False))])), ('blogs', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Heading to show above the blog entries', required=False)), ('link', wagtail.core.blocks.PageChooserBlock(help_text='Link to blog overview', required=False))])), ('three_images_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image_left', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.core.blocks.URLBlock(required=False))], required=False)), ('image_middle', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.core.blocks.URLBlock(required=False))], required=False)), ('image_right', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.core.blocks.URLBlock(required=False))], required=False))])), ('richtext_columns', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('columns_count', wagtail.core.blocks.ChoiceBlock(choices=[(1, 'One column'), (2, 'Two columns'), (3, 'Three columns')])), ('columns', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))], required=True)))]))], null=True),
        ),
    ]
