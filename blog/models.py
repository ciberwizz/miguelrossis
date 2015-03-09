from django.db import models

class Post(models.Model):
	
	title = models.CharField(max_length = 128, blank = False, default ='title')
	owner = models.CharField(max_length = 128, blank = False, default ='title')
	post = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)

