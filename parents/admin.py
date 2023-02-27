from django.contrib import admin

# Register your models here.
from parents.models import Parents, Children, GrandParent, Siblings

@admin.register(GrandParent)
class GrandParentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

@admin.register(Parents)
class ParentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = (
        "name",    
    )

@admin.register(Siblings)
class SiblingsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )