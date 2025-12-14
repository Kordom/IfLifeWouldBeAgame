from django.contrib import admin
from .models import *


class PlayerStatsInline(admin.StackedInline):
    model = PlayerStats
    can_delete = False

class PhysicalAttributesInline(admin.StackedInline):
    model  = PhysicalAttributes
    can_delete = False

class PersonalAttributesInline(admin.StackedInline):
    model  = PersonalAttributes
    can_delete = False

class MentalAttributesInline(admin.StackedInline):
    model  = MentalAttributes
    can_delete = False

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
    list_display = [
        "user__username",
        "max_hp",
        "hp",
        "energy",
        "max_energy",
        "xp",
    ]
    list_editable = [
        "max_hp",
        "hp",
        "energy",
        "max_energy",
        "xp",
    ]

    inlines = (PlayerStatsInline, PhysicalAttributesInline, PersonalAttributesInline, MentalAttributesInline)

@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = (
        "player__user__username",
        "strength",
        "dexterity",
        "vitality",
        "intelligence",
        "charisma",
    )

    list_editable = [
        "strength",
        "dexterity",
        "vitality",
        "intelligence",
        "charisma",
    ]

@admin.register(PhysicalAttributes)
class PhysicalAttributesAdmin(admin.ModelAdmin):
    list_display = [
        "player__user__username",
        "daily_steps",
        "sleep_hours",
        "exercise_per_week",
        "water_intake",
    ]
    list_editable = [
        "daily_steps",
        "sleep_hours",
        "exercise_per_week",
        "water_intake",
    ]

@admin.register(PersonalAttributes)
class PersonalAttributesAdmin(admin.ModelAdmin):
    list_display = [
        "player__user__username",
        "age",
        "height",
        "weight",
        "gender",
    ]
    list_editable = [
        "age",
        "height",
        "weight",
        "gender",
    ]

@admin.register(MentalAttributes)
class MentalAttributesAdmin(admin.ModelAdmin):
    list_display = [
        "player__user__username",
        "reading_time",
        "meditation_time",
    ]

    list_editable = [
        "reading_time",
        "meditation_time",
    ]

