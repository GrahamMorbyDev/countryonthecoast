from django.contrib import admin
from .models import Post, Artist, Partner

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'created_on')
    list_filter = ("name",)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'created_on')
    list_filter = ('name',)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Partner, PartnerAdmin)