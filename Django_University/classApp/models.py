from django.db import models  # import models that allows us to use for app


class DjangoClasses(models.Model):  # our model DjangoClasses
    Title = models.CharField(max_length=200)  # char field must include max length
    CourseNumber = models.IntegerField(blank=True, null=True)  # course number
    Instructor = models.CharField(max_length=200)   # instructor with char
    Duration = models.FloatField(max_length=10)     # duration with float field











