from django.contrib import admin
from catalog.models import Shelter, Pets

# Register your models here.
@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    pass

@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    pass
