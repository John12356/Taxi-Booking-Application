from django.db import models

class ALL_TAXIES(models.Model):
    taxino=models.IntegerField(primary_key=True)
    cur_loc=models.CharField(max_length=1)
    drop_time=models.IntegerField()
    short_dis=models.IntegerField()
    prev_loc=models.CharField(max_length=1)
    pick_time=models.IntegerField()
    pick_loc=models.CharField(max_length=1)
    
class SCHEDULED_TAXIES(models.Model):
    taxi_id=models.IntegerField()
    pick_loc=models.CharField(max_length=1)
    drop_loc=models.CharField(max_length=1)
    pick_time=models.IntegerField()
    drop_time=models.IntegerField()
    
class TAXI_DETAILS(models.Model):
    taxino=models.IntegerField()
    pick_loc=models.CharField(max_length=1)
    drop_loc=models.CharField(max_length=1)
    pick_time=models.IntegerField()
    drop_time=models.IntegerField()
    cus_id=models.IntegerField()
    
class TAXI_INCOME(models.Model):
    taxino=models.IntegerField(primary_key=True)
    amount=models.IntegerField()