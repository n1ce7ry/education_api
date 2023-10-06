from django.contrib.auth.models import User
from django.db import models

from catalog.models import Product


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.CharField(max_length=600)
    duration_in_seconds = models.IntegerField()
    product = models.ManyToManyField(Product)
    
    def __str__(self):
        return self.title


class LessonInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='views')
    viewing_time_in_seconds = models.IntegerField()
    viewed =models.BooleanField(default=False)

    def __str__(self):
        return (
            f'{self.user} '
            f'{"watched" if self.viewed is True else "didn’t watch"} '
            f'{self.lesson}'
        )
    
    
    class Meta:
        unique_together = ('user', 'lesson')
