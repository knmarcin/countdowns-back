from django.db import models


class Countdown(models.Model):
    title = models.CharField(max_length=64,
                             blank=True,
                             null=True,
                             default='Event',
                             help_text="Insert your countdown Title!")
    date = models.DateField(help_text="Select the date!")
