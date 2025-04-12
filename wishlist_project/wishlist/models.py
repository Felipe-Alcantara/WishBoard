from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.BooleanField(default=False)  # False = não concluído, True = concluído
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name