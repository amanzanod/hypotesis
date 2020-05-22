from django.contrib import admin

from .models import Context, Role, PermissionRole, Permission, User


# User Admin.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')
    exclude = ('token',)


# Role Admin.
class RoleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')


# Permission Admin.
class PermissionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')


# Context Admin.
class ContextAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


# Permission Admin.
class PermissionRoleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'active_at')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Context, ContextAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(PermissionRole, PermissionRoleAdmin)
