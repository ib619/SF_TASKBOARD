from django.db import models


class Member(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.EmailField()

    def __str__(self):
        return self.Name
