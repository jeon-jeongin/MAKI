from django.db import models

from .choices import (
  get_choices, 
  options, 
  mediums, 
  content_ratings, 
  genres, 
  tags, 
  productions
)


class Series(models.Model):
  '''
  시리즈 모델
  '''
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Animation(models.Model):
  """
  애니메이션 모델
  """
  name = models.CharField(max_length=100)
  notice = models.TextField(default='', null=True)
  content = models.TextField(default='', null=True)
  medium = models.CharField(max_length=10, choices=get_choices(mediums))
  content_rating = models.CharField(max_length=10, choices=get_choices(content_ratings))
  is_ending = models.BooleanField(default=False)
  production = models.CharField(max_length=50, null=True, choices=get_choices(productions))
  is_dubbed = models.BooleanField(default=False)
  is_uncensored = models.BooleanField(default=False)
  series_id = models.ForeignKey(to=Series, on_delete=models.SET_NULL, null=True, related_name='series')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return self.name


class Image(models.Model):
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='images')
  x = models.IntegerField()
  y = models.IntegerField()
  width = models.IntegerField()
  height = models.IntegerField()
  img_url = models.CharField(max_length=1024)
  option_name = models.CharField(max_length=20, choices=get_choices(options))
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('animation', 'option_name',)

  def __str__(self):
    return self.option_name


class Award(models.Model):
  name = models.CharField(max_length=100)
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='awards')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('animation', 'name',)
  
  def __str__(self):
    return self.name


class Genre(models.Model):
  name = models.CharField(max_length=50, choices=get_choices(genres))
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='genres')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('animation', 'name',)

  def __str__(self):
    return self.name


class Tag(models.Model):
  name = models.CharField(max_length=50, choices=get_choices(tags))
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='tags')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('animation', 'name',)

  def __str__(self):
    return self.name


class Air(models.Model):
  year = models.IntegerField()
  quarter = models.IntegerField(null=True)
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='air_year_quaters')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('animation', 'year', 'quarter',)

  def __str__(self):
    air_year = f'{self.year}년'
    if self.quarter: 
      return air_year + f' {self.quarter}분기'
    return air_year


class Author(models.Model):
  name = models.CharField(max_length=50)
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='authors')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('animation', 'name',)

  def __str__(self):
    return self.name


class Illustrator(models.Model):
  name = models.CharField(max_length=50)
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='illustrators')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('animation', 'name',)

  def __str__(self):
    return self.name
