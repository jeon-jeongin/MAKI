from django.contrib import admin

from .models import (
  Series,
  Animation,
  Image,
  Award,
  Genre,
  Tag,
  Air,
  Author,
  Illustrator,
)

class SeriesAdmin(admin.ModelAdmin):
  list_display = ('id',)

class AnimationAdmin(admin.ModelAdmin):
  list_display = ('name',)
  ordering = ('name',)
  search_fields = ('name',)

class ImageAdmin(admin.ModelAdmin):
  list_display = ('animation', 'img_url', 'option_name',)
  ordering = ('animation', 'img_url', 'option_name',)
  search_fields = ('img_url', 'option_name',)

class AwardAdmin(admin.ModelAdmin):
  list_display = ('animation', 'name',)
  ordering = ('animation', 'name',)
  search_fields = ('name',)

class GenreAdmin(admin.ModelAdmin):
  list_display = ('animation', 'name',)
  ordering = ('animation', 'name',)
  search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
  list_display = ('animation', 'name',)
  ordering = ('animation', 'name',)
  search_fields = ('name',)

class AirAdmin(admin.ModelAdmin):
  list_display = ('animation', 'year', 'quarter',)
  ordering = ('animation', 'year', 'quarter',)
  search_fields = ('year', 'quarter',)

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('animation', 'name',)
  ordering = ('animation', 'name',)
  search_fields = ('name',)

class IllustratorAdmin(admin.ModelAdmin):
  list_display = ('animation', 'name',)
  ordering = ('animation', 'name',)
  search_fields = ('name',)

admin.site.register(Series, SeriesAdmin)
admin.site.register(Animation, AnimationAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Air, AirAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Illustrator, IllustratorAdmin)