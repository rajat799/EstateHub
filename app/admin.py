from django.contrib import admin
from app.models import (
    AdminMaster, AdminSeller, Category, Properties, Products,
    Booking, Register, Cart, Order, PurchasedProducts, AdminBooking
)

# Register your models here.

class AdminMasterAdmin(admin.ModelAdmin):
    list_display = ('ad_id', 'ad_name', 'ad_email', 'ad_mobile', 'ad_role', 'ad_status', 'ad_created_by')
    list_filter = ('ad_status', 'ad_role')
    search_fields = ('ad_name', 'ad_email', 'ad_mobile')
    ordering = ('-ad_id',)
    list_editable = ('ad_status',)

class AdminSellerAdmin(admin.ModelAdmin):
    list_display = ('s_id', 's_name', 's_email', 's_mobile', 's_role', 's_status', 's_created_by')
    list_filter = ('s_status', 's_role')
    search_fields = ('s_name', 's_email', 's_mobile')
    ordering = ('-s_id',)
    list_editable = ('s_status',)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('us_id', 'us_name', 'us_email', 'us_mobile', 'us_status', 'us_created_by')
    list_filter = ('us_status',)
    search_fields = ('us_name', 'us_email', 'us_mobile')
    ordering = ('-us_id',)
    list_editable = ('us_status',)
    readonly_fields = ('us_password',)
    fieldsets = (
        ('User Information', {
            'fields': ('us_name', 'us_email', 'us_mobile')
        }),
        ('Account', {
            'fields': ('us_password', 'us_status')
        }),
        ('System', {
            'fields': ('us_created_by',)
        }),
    )

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pd_id', 'pd_name', 'pd_category', 'pd_price', 'pd_status', 'pd_created_by')
    list_filter = ('pd_category', 'pd_status')
    search_fields = ('pd_name', 'pd_category')
    ordering = ('-pd_id',)
    list_editable = ('pd_status',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('ca_id', 'ca_name', 'ca_status')
    list_filter = ('ca_status',)
    search_fields = ('ca_name',)
    list_editable = ('ca_status',)

class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('pr_id', 'pr_name', 'pr_category', 'pr_property_type', 'pr_place', 'pr_fee', 'pr_status', 'pr_sold')
    list_filter = ('pr_property_type', 'pr_status', 'pr_sold', 'pr_category')
    search_fields = ('pr_name', 'pr_place', 'pr_category')
    ordering = ('-pr_id',)
    list_editable = ('pr_status', 'pr_sold')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('bk_id', 'bk_user_name', 'bk_property_id', 'bk_amount', 'bk_status', 'bk_created_date')
    list_filter = ('bk_status', 'bk_created_date')
    search_fields = ('bk_user_name', 'bk_user_email', 'bk_property_id')
    ordering = ('-bk_id',)
    list_editable = ('bk_status',)

class AdminBookingAdmin(admin.ModelAdmin):
    list_display = ('b_id', 'b_purchaser_name', 'b_property_name', 'b_amount', 'b_status', 'b_date')
    list_filter = ('b_status',)
    search_fields = ('b_purchaser_name', 'b_property_name')
    ordering = ('-b_id',)
    list_editable = ('b_status',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('ct_id', 'ct_name', 'ct_category', 'ct_price', 'ct_qty', 'ct_user_email', 'ct_status')
    list_filter = ('ct_status', 'ct_category')
    search_fields = ('ct_name', 'ct_user_email')
    ordering = ('-ct_id',)
    list_editable = ('ct_status',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('or_id', 'or_name', 'or_email', 'or_transaction_id', 'or_total_amount', 'or_status', 'or_date')
    list_filter = ('or_status', 'or_date')
    search_fields = ('or_name', 'or_email', 'or_transaction_id')
    ordering = ('-or_id',)
    list_editable = ('or_status',)
    readonly_fields = ('or_transaction_id',)

class PurchasedProductsAdmin(admin.ModelAdmin):
    list_display = ('pp_id', 'pp_name', 'pp_category', 'pp_price', 'pp_qty', 'pp_user_email', 'pp_status')
    list_filter = ('pp_status', 'pp_category')
    search_fields = ('pp_name', 'pp_user_email')
    ordering = ('-pp_id',)
    list_editable = ('pp_status',)

# Register all models with custom admin classes
admin.site.register(AdminMaster, AdminMasterAdmin)
admin.site.register(AdminSeller, AdminSellerAdmin)
admin.site.register(Register, RegisterAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Properties, PropertiesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(AdminBooking, AdminBookingAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PurchasedProducts, PurchasedProductsAdmin)
