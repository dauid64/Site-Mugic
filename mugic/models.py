from django.db import models

class Projeto(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)
    cover = models.ImageField(upload_to='projetos/covers/%Y/%m/%d/')
    cover_2 = models.ImageField(upload_to='projetos/covers/%Y/%m/%d/', blank=True)
    cover_3 = models.ImageField(upload_to='projetos/covers/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)
    video_url = models.CharField(max_length=255, blank=True, default='')
    video_download = models.FileField(upload_to='projetos/covers/%Y/%m/%d/', blank=True)
    have_video = models.BooleanField(default=False)


    def __str__(self):
        return self.title