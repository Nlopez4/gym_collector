from django.db import models

# Create your models here.


class gyms(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    classes = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# location model
# class location(models.Model):
#     address = models.CharField(max_length=150)
#     gym = models.ForeignKey(
#         gyms, on_delete=models.CASCADE, related_name="locations")

#     def __str__(self):
#         return self.title


# one to many model
class Techniques(models.Model):
    type = models.CharField(max_length=150)
    description = models.CharField(max_length=450)
    gym = models.ForeignKey(
        gyms, on_delete=models.CASCADE, related_name="technique")

    def __str__(self):
        return self.type
