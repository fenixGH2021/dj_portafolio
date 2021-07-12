from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio

# Register your models here.
admin.site.site_header = "Panel de administración"
admin.site.site_title = "Area de administración"
admin.site.index_title = "Bienvenido"

# Home
admin.site.register(Home)

# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]

# Portfolio
admin.site.register(Portfolio)