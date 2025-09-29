from django.contrib import admin
from .models import Job, Character, Personal_skill, Weapon, WeaponCategory, Item,Skill
from django.utils.html import format_html
# Register your models here.
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name','jobs','avatar')
class JobAdmin(admin.ModelAdmin):
    list_display = ('title',)
class Personal_skillsAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)
class WeaponCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Job, JobAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Personal_skill, Personal_skillsAdmin)
admin.site.register(Weapon,WeaponAdmin)
admin.site.register(WeaponCategory,WeaponCategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Skill, SkillAdmin)