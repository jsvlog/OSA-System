from django.db import models

# Create your models here.
class ToRegion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date_received = models.DateField(blank=True, null=True)
    received_from =  models.CharField(max_length=50, blank=True, null=True)
    document_type =  models.CharField(max_length=100, blank=True, null=True)
    document_date = models.DateField(blank=True, null=True)
    particulars =  models.TextField(blank=True, null=True)
    copies =  models.TextField(blank=True, null=True)
    date_signed_sa =  models.DateField(blank=True, null=True)
    transmittal_number =  models.CharField(max_length=50, blank=True, null=True)
    date_sent_out =  models.DateField(blank=True, null=True)
    date_received_from_region =  models.DateField(blank=True, null=True)
    date_received_by_region =  models.DateField(blank=True, null=True)
    location_stored =  models.TextField(blank=True, null=True)
    date_sent_to_teams = models.DateField(blank=True, null=True)
    received_by_team = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)


    def __str__(self):
        return(f"{self.document_type} {self.particulars}")
    
class FromRegion(models.Model):
    type_of_doccument = models.CharField(max_length=100)
    addressee = models.CharField(max_length=200)
    document_date = models.DateField()
    subject = models.TextField()
    details = models.CharField(max_length=200)
    reference_number = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    barangay = models.CharField(max_length=100)
    date_received = models.DateField()
    received_from = models.CharField(max_length=100)
    date_sentout_from_osa = models.DateField()
    team_receiver = models.CharField(max_length=100)
    location_stored = models.CharField(max_length=200)
    remarks = models.TextField()