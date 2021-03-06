from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
	image = models.ImageField(upload_to='media/')

	def __str__(self):
		return self.title