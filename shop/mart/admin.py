from django.contrib import admin
from .models import products,Order
# Register your models here.

admin.site.site_header ="E-commerce site"
admin.site.site_title = "Market app"
admin.site.index_title = "MANAGE MY MARKET"

class ProductDetail(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category = 'default')

    change_category_to_default.short_description ='change to default'
    list_display = ('title' , 'price' , 'discount_price' , 'category' ,'desc',)
    search_fields = ('title', 'price' ,)
    actions = ('change_category_to_default',)
    fields =('price', 'title',)
    list_editable =('price' , 'category',)
admin.site.register(products , ProductDetail)
admin.site.register(Order)

