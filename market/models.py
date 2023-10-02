from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    have_access = models.ManyToManyField(
        User,
        through='UserProductRelation',
        related_name='access',
    )

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.CharField(max_length=600)
    duration_in_seconds = models.IntegerField()
    product = models.ManyToManyField(Product, related_name='course')
    user_action = models.ManyToManyField(
        User,
        through='UserLessonRelation',
        related_name='user_action'
    )

    def __str__(self):
        return self.title


class UserProductRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    access = models.BooleanField(default=False)

    def __str__(self):
        return (
            f'{self.user} '
            f'{"has access to the" if self.access is True else "doesn’t have access to the"} '
            f'{self.product}'
        )


class UserLessonRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewing_time_in_seconds = models.IntegerField()
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return (
            f'{self.user} '
            f'{"watched" if self.viewed is True else "didn’t watch"} '
            f'{self.lesson}'
        )
