from django.db import models

# Create your models here.
class Students(models.Model):
    full_name = models.CharField(
        max_length=155,
        verbose_name = "ФИО"
    )
    age = models.IntegerField(
        default=0,
        verbose_name = "Возраст"
    )
    hobby = models.TextField(
        blank=True, null=True,
        verbose_name = "Хобби"
    )

    def __str__(self):
        # return f"студент - {self.full_name}"
        return self.full_name
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"