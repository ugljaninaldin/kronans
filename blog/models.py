from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    content_file = models.FileField(upload_to='blog_content/', blank=True, null=True)
    content_text = models.TextField()

    def __str__(self):
        return self.title
