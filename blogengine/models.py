from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)

    def __unicode__(self):
        return self.title
