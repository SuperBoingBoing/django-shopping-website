from django.contrib import admin
from .models import Phone, Snack, Movie, Cart

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

admin.site.register(Phone, ProductAdmin)
admin.site.register(Snack, SnackAdmin)
admin.site.register(Movie, MovieAdmin)
