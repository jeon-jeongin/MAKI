from django.db import models

class Production(models.Model):
  """
  제작사
  """
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class ContentRating(models.Model):
  """
  등급
  """
  name = models.CharField(max_length=20)
  description = models.TextField()

  def __str__(self):
    return self.name

class Animation(models.Model):
  """
  애니메이션 모델
  """
  name = models.CharField(max_length=100)
  content = models.TextField(default="")
  img = models.ImageField(default=".", max_length=1024)
  content_rating = models.ForeignKey(to=ContentRating, on_delete=models.CASCADE)
  production = models.ForeignKey(to=Production, on_delete=models.CASCADE)
  published_at = models.DateField()

class Award(models.Model):
  """
  Award 모델
  """
  name = models.CharField(max_length=100)
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='awards')

  def __str__(self):
    return self.name
