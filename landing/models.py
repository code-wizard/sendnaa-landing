from django.db import models

# Create your models here.


class SAJoinList(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    from_country = models.CharField(max_length=2)
    to_country = models.CharField(max_length=2)
    transfer_amount = models.PositiveIntegerField()
    sell_amount = models.PositiveIntegerField()

    class Meta:
        db_table = "sa_join_list"
        verbose_name = "Join list"
