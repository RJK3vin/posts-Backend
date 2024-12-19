from django.db import models

class Post(models.Model):
    comment = models.CharField(max_length = 300, blank = False, default = '')
