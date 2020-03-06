from django.contrib import admin
from django.db import models

from apps.notifications import admin as notification_admin

from .models import Idea
from .models.sections.applicant_section import ApplicantSection
from .models.sections.finances_section import FinancesSection
from .models.sections.idea_section import IdeaSection
from .models.sections.local_dimension_section import LocalDimensionSection
from .models.sections.network_community_section import NetworkSection
from .models.sections.partners_section import PartnersSection
from .models.sections.road_to_impact_section import RoadToImpactSection


def set_is_on_shortlist_true(modeladmin, request, queryset):
    queryset.update(is_on_shortlist=True)


set_is_on_shortlist_true.short_description = 'add to shortlist'


def set_is_on_shortlist_false(modeladmin, request, queryset):
    queryset.update(is_on_shortlist=False)


set_is_on_shortlist_false.short_description = 'remove from shortlist'


def set_community_award_winner_true(modeladmin, request, queryset):
    queryset.update(community_award_winner=True)


set_community_award_winner_true.\
    short_description = 'Set to community award winner'


def set_community_award_winner_false(modeladmin, request, queryset):
    queryset.update(community_award_winner=False)


set_community_award_winner_false.\
    short_description = 'Unset community award winner'


def set_is_winner_true(modeladmin, request, queryset):
    queryset.update(is_winner=True)


set_is_winner_true.short_description = 'Set to winner'


def set_is_winner_false(modeladmin, request, queryset):
    queryset.update(is_winner=False)


set_is_winner_false.short_description = 'Unset winner'


class IdeaAdmin(notification_admin.NotifyMixin, admin.ModelAdmin):
    exclude = ['module']
    raw_id_fields = ('creator', 'co_workers')
    search_fields = ('title',)
    list_filter = (
        'module__project__name',
        'is_winner',
        'is_on_shortlist',
        'community_award_winner',
    )

    formfield_overrides = {
        models.TextField: {'max_length': None,
                           'help_text': None},
    }

    list_display = ['title', 'is_on_shortlist',
                    'community_award_winner', 'is_winner',
                    'created', 'modified']
    ordering = ['-created', 'title']
    actions = [
        set_is_on_shortlist_true,
        set_is_on_shortlist_false,
        set_community_award_winner_true,
        set_community_award_winner_false,
        set_is_winner_true,
        set_is_winner_false,
    ]
    fieldsets = (
        ('Jury Section', {
            'fields': ('jury_statement',
                       'budget_granted',
                       ('is_on_shortlist',
                        'community_award_winner',
                        'is_winner')
                       )
        }),
        ('Creator and Co-workers', {
            'classes': ('collapse',),
            'fields': ('creator',)
        }),
        ('Applicant Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in ApplicantSection._meta.get_fields()]),
        }),
        ('Partner Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in PartnersSection._meta.get_fields()]),
        }),
        ('Idea Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in IdeaSection._meta.get_fields()]),
        }),
        ('Local Dimension', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in LocalDimensionSection._meta.get_fields()]),
        }),
        ('Road to impact & motivation', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in RoadToImpactSection._meta.get_fields()]),
        }),
        ('Finances', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in FinancesSection._meta.get_fields()]),
        }),
        ('Network & Community', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in NetworkSection._meta.get_fields()]),
        }),
    )


admin.site.register(Idea, IdeaAdmin)
