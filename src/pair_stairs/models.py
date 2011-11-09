from django.db import models

# Create your models here.

class Programmer(models.Model):
    name = models.TextField()


class PairStairs(models.Model):
    first = models.TextField()
    second = models.TextField()
    times = models.IntegerField()

def get_pair_times(first, second):
    pairs = PairStairs.objects.filter(first=first, second=second)
    if pairs:
        return pairs[0].times
    
def increase_pair_times(first ,second):
    pairs = PairStairs.objects.filter(first=first, second=second)
    if pairs:
        pairs[0].times += 1
        pairs[0].save()