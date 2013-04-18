from django.contrib import admin
from models import Architect, Classification, Project

class ArchitectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('English', { 'fields': ('firstname_e', 'lastname_e') }),
        ('Hebrew', { 'fields': ('firstname_h', 'lastname_h') }),
        ('Common', { 'fields': ('email', 'portrait') }),
    )

class ClassificationAdmin(admin.ModelAdmin):
    pass 

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('English', { 'fields': ('title_e', 'address_e', 'description_e') }),
        ('Hebrew', { 'fields': ('title_h', 'address_h', 'description_h') }),
        ('Common', { 'fields': ('year', 'architect', 'status', 'plot_area', 'built_area') }),
    )

admin.site.register(Architect, ArchitectAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Project, ProjectAdmin)

