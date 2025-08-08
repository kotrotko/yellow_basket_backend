from django.db import models

# Flower model: Represents individual flowers
class Flower(models.Model):
    sort = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.sort} ({self.color})"