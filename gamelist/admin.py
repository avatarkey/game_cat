from django.contrib import admin

# Register your models here.
from .models import Game, Developer, Genre, UserProfile

class gameAdmin(admin.ModelAdmin):
	class Meta:
		model = Game

class devAdmin(admin.ModelAdmin):
	class Meta:
		model = Developer

class genAdmin(admin.ModelAdmin):
	ordering = ('name',)
	class Meta:
		model = Genre


admin.site.register(Game, gameAdmin)
admin.site.register(Developer, devAdmin)
admin.site.register(Genre, genAdmin)
admin.site.register(UserProfile)