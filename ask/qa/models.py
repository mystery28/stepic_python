from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=70)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)
	class  Meta:
		db_table = 'question'
	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question = models.OneToOneField(Question)
	author = models.ForeignKey(User)
	class  Meta:
		db_table = 'answer'
