import random

from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         ObjectList, StreamFieldPanel,
                                         TabbedInterface)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from . import blocks as custom_blocks


class HomePage(Page):
    block_types = [
        ('columns', custom_blocks.ThreeColumnTextBlock()),
        ('call_to_action', custom_blocks.CallToActionBlock()),
        ('idea_carousel', custom_blocks.ProposalCarouselBlock()),
        ('blogs', custom_blocks.ThreeBlogEntriesBlock()),
        ('three_images_block', custom_blocks.ThreeImagesBlock())
    ]

    translated_title = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")

    description = models.TextField(blank=True)

    body = StreamField(block_types, null=True)

    # shared fields
    image_1 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 1",
        help_text="The Image that is shown on top of the page"
    )

    image_2 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 2",
        help_text="The Image that is shown on top of the page"
    )

    image_3 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 3",
        help_text="The Image that is shown on top of the page"
    )

    image_4 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 4",
        help_text="The Image that is shown on top of the page"
    )

    image_5 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 5",
        help_text="The Image that is shown on top of the page"
    )

    videoplayer_url = models.URLField(blank=True, verbose_name='Video URL')
    video_button_text = models.CharField(
        default='Play Video', blank=True, max_length=100)

    website = models.URLField(blank=True, verbose_name='Website')
    website_link_text = models.CharField(
        default='more', blank=True, max_length=100)

    subpage_types = ['cms_blog.BlogIndexPage',
                     'cms_home.SimplePage',
                     'cms_home.StructuredTextPage']

    @property
    def random_image(self):
        image_numbers = [i for i in range(1, 6)
                         if getattr(self, 'image_{}'.format(i))]
        if image_numbers:
            return getattr(self,
                           'image_{}'.format(random.choice(image_numbers)))

    content_panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('image_1'),
                ImageChooserPanel('image_2'),
                ImageChooserPanel('image_3'),
                ImageChooserPanel('image_4'),
                ImageChooserPanel('image_5'),
            ],
            heading="Images",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('videoplayer_url'),
                FieldPanel('video_button_text')
            ],
            heading="Video",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('website'),
                FieldPanel('website_link_text')
            ],
            heading="Link",
            classname="collapsible"
        )
    ]

    en_panels = [
        FieldPanel('translated_title'),
        FieldPanel('description'),
        StreamFieldPanel('body')
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_panels, heading='English'),
        ObjectList(content_panels, heading='Header'),
        ObjectList(Page.promote_panels, heading='Promote')
    ])


class SimplePage(Page):
    block_types = [
        ('text', blocks.RichTextBlock()),
        ('FAQs', custom_blocks.FAQBlock())
    ]

    # translated fields
    translated_title = models.CharField(
        max_length=255, verbose_name="Title")

    body = StreamField(block_types, null=True)

    en_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body')
    ]

    Page.promote_panels[0].children.insert(0,
                                           FieldPanel('title')
                                           )

    edit_handler = TabbedInterface([
        ObjectList(en_panels, heading='English'),
        ObjectList(Page.promote_panels, heading='Promote')
    ])


class StructuredTextPage(Page):
    block_types = [
        ('section', custom_blocks.SectionBlock())
    ]

    # translated fields
    translated_title = models.CharField(
        max_length=255, verbose_name="Title")

    body = StreamField(block_types, null=True)

    en_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body')
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_panels, heading='English'),
        ObjectList(Page.promote_panels, heading='Promote')
    ])
