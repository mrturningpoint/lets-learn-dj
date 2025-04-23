from django.contrib import admin
from .models import chaivariety,chaireview,store,chaicert
# Register your models here.
class Chaireviewinline(admin.TabularInline):
    model=chaireview
    extra=2

class Chaivarietyadmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[Chaireviewinline]

class Storeadmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varietiess',)

class Chaicertadmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')    
admin.site.register(chaivariety,Chaivarietyadmin)
admin.site.register(store,Storeadmin)
admin.site.register(chaicert,Chaicertadmin)