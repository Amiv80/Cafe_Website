from django.db import models

class Member(models.Model):
    title = models.CharField(max_length=50)
    vip_member = models.BooleanField(verbose_name=('VIP Members'), default=False)
    date_add = models.DateField(auto_now_add=True)

    
    class Meta:
        ordering = ["title"]
        db_table = 'Member'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.title