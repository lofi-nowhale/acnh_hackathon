from django.db import models

class Island(models.Model):
    name = models.CharField(max_length=200)
    rank = models.IntegerField()
    full = models.BooleanField()

class Villager(models.Model):
    name = models.CharField(max_length=200)
    personality = models.CharField(max_length=200)
    friendship_level = models.IntegerField()
    dream_home = models.BooleanField(max_length=200)

class IslandVillagers(models.Model):
    island = models.ForeignKey(Island, on_delete=models.CASCADE, null=False)
    villager = models.ForeignKey(Villager, on_delete=models.CASCADE, null=False)