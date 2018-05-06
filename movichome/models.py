from django.db import models

# Create your models here.
class PageScrape(models.Model):
    text_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length = 10000)
    description_2 = models.CharField(max_length = 10000)
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title