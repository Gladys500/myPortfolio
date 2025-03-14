from django.contrib import admin
from .models import AboutInfo, ContactRequest, Testimonials 

# Register your models here.
@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ('name', 'address', 'email')
    
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_submitted')
    search_fields = ('name', 'email')
    list_filter = ['date_submitted']
    
@admin.register(Testimonials)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'date')
    search_fields = ['name']
    list_filter = ('rating', 'date')
    