from django.db import models

# Create your models here.
class ToRegion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date_received = models.DateField()
    received_from =  models.CharField(max_length=50)
    document_type =  models.CharField(max_length=100)
    document_date = models.DateField()
    particulars =  models.TextField()
    copies =  models.TextField()
    date_signed_sa =  models.DateField()
    transmittal_number =  models.CharField(max_length=50)
    date_sent_out =  models.DateField()
    date_received_from_region =  models.DateField()
    date_received_by_region =  models.DateField()
    location_stored =  models.TextField()
    date_sent_to_teams = models.DateField()
    received_by_team = models.CharField(max_length=50)


    def __str__(self):
        return(f"{self.document_type} {self.particulars}")