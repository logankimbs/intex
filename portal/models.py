from django.db import models


class State(models.Model):
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(max_length=2)  # (PK)
    population = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)

    def __str__(self):
        return (self.stateabbrev)
