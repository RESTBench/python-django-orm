from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        db_table = 'contact'
