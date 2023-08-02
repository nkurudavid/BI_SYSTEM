from django.contrib import admin
from main.models import *

# Register your models here.

class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    extra = 0

class ProductInline(admin.StackedInline):
    model = Product
    inlines = [ProductDetailInline]
    extra = 0

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','all_products',)
    fieldsets = (
        ('Product Category', {'fields': ('category_name',)}),
    )
    add_fieldsets = (
        ('New Product Category', {'fields': ('category_name',)}),
    )
    search_fields = ('category_name',)
    ordering = ('category_name',)
    list_per_page = 20
    inlines = [
        ProductInline,
    ]
    def all_products(self, obj):
        return obj.products.count()




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category','description','price','all_details',)
    list_filter = ('category',)
    fieldsets = (
        ('Product Info', {'fields': ('category','product_name','description','price',)}),
    )
    add_fieldsets = (
        ('New Product', {'fields': ('category','product_name','description','price',)}),
    )
    search_fields = ('product_name',)
    ordering = ('product_name',)
    list_per_page = 20
    inlines = [
        ProductDetailInline,
    ]
    def all_details(self, obj):
        return obj.details.count()



@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'color', 'quantity', 'image',)
    list_filter = ('product',)
    fieldsets = (
        ('Product Details', {'fields': ('product', 'color', 'quantity', 'picture',)}),
    )
    add_fieldsets = (
        ('Register New Product', {'fields': ('product', 'color', 'quantity', 'picture',)}),
    )
    search_fields = ('product',)
    ordering = ('product',)
    list_per_page = 20



@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product_detail','movement_type','quantity','total_price','processed_by','date_time',)
    list_filter = ('movement_type',)
    fieldsets = (
        ('Stock Movement Info', {'fields': ('product_detail','movement_type','quantity','total_price','processed_by','date_time',)}),
    )
    add_fieldsets = (
        ('New Stock Movement', {'fields': ('product_detail','movement_type','quantity','total_price','processed_by','date_time',)}),
    )
    search_fields = ('product_detail','date_time',)
    ordering = ('date_time',)
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        # make 'status' field read-only
        if request.user:
            return ['date_time',]
        return []



# sorting models
def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        # Retrieve the original list
        app_dict = self._build_app_dict(request, app_label)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models customizable within each app.
        for app in app_list:
            if app['app_label'] == 'MAIN':
                ordering = {
                    'ProductCategory': 1,
                    'Product': 2,
                    'ProductDetail': 3,
                    'StockMovement': 4,
                }
                app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list


admin.AdminSite.get_app_list = get_app_list