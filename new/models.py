from django.db import models


class Data(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)
    user_id = models.IntegerField(primary_key=True)

    def _str_(self):
        return self.name


