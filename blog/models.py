from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	description1 = models.CharField(max_length = 1000)
	description2 = models.CharField(max_length = 1000, blank = True, null = True)
	description3 = models.CharField(max_length = 1000, blank = True, null = True)
	description4 = models.CharField(max_length = 1000, blank = True, null = True)
	description5 = models.CharField(max_length = 1000, blank = True, null = True)
	description6 = models.CharField(max_length = 1000, blank = True, null = True)
	description7 = models.CharField(max_length = 1000, blank = True, null = True)
	description8 = models.CharField(max_length = 1000, blank = True, null = True)
	description9 = models.CharField(max_length = 1000, blank = True, null = True)
	description0 = models.CharField(max_length = 1000, blank = True, null = True)
	date = models.DateField()
	image1 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image2 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image3 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image4 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image5 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image6 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image7 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image8 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image9 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	image0 = models.ImageField(upload_to = 'blog/images/', blank = True, null = True)
	slug = models.SlugField(max_length=40)

	def __str__(self):
		return self.title

