from django.db import models

class Recruiter(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Requisition(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ActiveStatus(models.Model):
    name = models.CharField(max_length=100)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    active_status = models.ForeignKey(ActiveStatus, on_delete=models.CASCADE)
    candidate_source = models.CharField(max_length=200)
    application_received = models.DateField(auto_now=False)
    application_status = models.CharField(max_length=200)
    license_status = models.CharField(max_length=200)
    screen_date = models.DateField(auto_now=False)
    agreement_sent = models.DateField(auto_now=False)
    agreement_signed = models.DateField(auto_now=False)
    candidate_notes = models.TextField(max_length=500, blank=True)
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

