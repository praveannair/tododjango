from django.contrib import admin
from core.models import todo,product

class todoadmin(admin.ModelAdmin):
    list_display=('task',)
                  
class productadmin(admin.ModelAdmin):
    list_display=('name','price','desc','url')

admin.site.register(todo,todoadmin)
admin.site.register(product,productadmin)
