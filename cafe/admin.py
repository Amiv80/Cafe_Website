from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'vip_member', 'date_add']
    list_filter = ['vip_member']