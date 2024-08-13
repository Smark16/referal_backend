from django.contrib import admin
from .models import BackgroundInformation, Business, Modules, Services

@admin.register(BackgroundInformation)
class BackgroundInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'FullName', 'TelephoneNumber', 'Age', 'Gender', 'MaritalStatus', 'EmailAddress', 'Nationality')
    search_fields = ('FullName', 'TelephoneNumber', 'EmailAddress')

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('user', 'name_of_bussiness', 'year_of_establishment', 'type_of_bussiness', 'Business_location')
    search_fields = ('name_of_bussiness', 'Business_location')

@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ('id', 'module')
    search_fields = ('module',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('user', 'reason_for_additional_services', 'confirmation')
    search_fields = ('reason_for_additional_services',)
   