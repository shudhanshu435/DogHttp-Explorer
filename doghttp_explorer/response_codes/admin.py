from django.contrib import admin
from .models import ResponseCodeList
# Register your models here.

@admin.register(ResponseCodeList)
class ResponseCodeListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'response_codes_display')
    search_fields = ('name', 'user__username', 'response_codes')
    list_filter = ('created_at',)

    def response_codes_display(self, obj):
        return ', '.join(obj.response_codes.split(','))[:50] + '...' if len(obj.response_codes) > 50 else obj.response_codes

    response_codes_display.short_description = "Response Codes"