from django.db import models

class MangoExport(models.Model):
    order_id = models.AutoField(primary_key=True)
    variety = models.CharField(max_length=100, unique=True)  # Ensure variety names are unique
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.variety

    class Meta:
        # You can define a custom ordering if you want
        ordering = ['order_id']
