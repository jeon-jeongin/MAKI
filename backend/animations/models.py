import uuid

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
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100)
  content = models.TextField(default="")
  img = models.ImageField(default=".", max_length=1024)
  content_rating = models.ForeignKey(to=ContentRating, on_delete=models.CASCADE)
  production = models.ForeignKey(to=Production, on_delete=models.CASCADE)
  published_at = models.DateField()
  is_ending = models.BooleanField(default=False)
  is_dubbed = models.BooleanField(default=False)


class Award(models.Model):
  """
  Award 모델
  """
  name = models.CharField(max_length=100)
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='awards')

  def __str__(self):
    return self.name

class Tag(models.Model):
  """
  Award 모델
  """
  name = models.CharField(max_length=100)
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='tags')

  def __str__(self):
    return self.name

class ContentChoices(models.TextChoices):
  PREJUDICE = "P"         # 편견
  SEXUAL_SITUATION = "S"  # 선정성
  VIOLENCE = "V"          # 폭력
  LANGUAGE = "L"          # 대사
  HORROR = "H"            # 공포
  SUBSTANCE_ABUSE = "D"   # 약물
  IMIATION_RISK = "I"     # 모방위험

class ContentElement(models.Model):
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='content_elements')
  element = models.CharField(choices=ContentChoices.choices, max_length=5)

class GenreChoices(models.TextChoices):
  SF = "SF"
  FANTASY = "Fantasy"
  ACTION = "Action"
  HORROR = "Horror"
  GORE = "Gore"
  DOCUMENTARY = "Documentary"
  ROMANCE = "Romance"
  THRILLER = "Thriller"
  MECHANIC = "Mechanic"
  MYSTERY = "Mystery"
  SPORTS = "Sports"
  THREE_DIMENSIONAL = "3D"
  RESCUE = "Rescue"
  GANGSTER = "Gangster"
  RACING = "Racing"
  MAGIC = "Magic"
  Maid = "Maid"
  ADVENTURE = "Adventure"
  CRIME = "Crime"
  ERA = "Era"
  CHILD = "Child"
  BIOGRAPHY = "Biography"
  WAR = "War"
  CLAYMATION = "Claymation"
  TRANSFORMATION = "Transformation"
  ROBOT = "robot"

class Genre(models.Model):
  animation = models.ForeignKey(to=Animation, on_delete=models.CASCADE, related_name='genres')
  element = models.CharField(choices=ContentChoices.choices, max_length=30)