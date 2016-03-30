from django.db import models
from django.core.urlresolvers  import reverse
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=70)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField(null=True)
	author = models.ForeignKey(User, null=True, related_name='author_set')
	likes = models.ManyToManyField(User, null=True, related_name='likes_set')
	def __unicode__(self):
		return self.title
	def  get_url(self):
		return reverse('question', kwargs={'id': self.id})
	class  Meta:
		db_table = 'question'
	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True)
	def __unicode__(self):
		return self.text
	class  Meta:
		db_table = 'answer'
