from django.db import models
from django.core.validators import RegexValidator


# pd_drugs √
class pd_drugs(models.Model):
    drugid = models.IntegerField(default=0, primary_key=True)
    drugname = models.CharField(max_length=30)  # (PK)
    isopioid = models.CharField(max_length=5)

    def __str__(self):
        return (self.drugname)


# pd_prescriber √
class pd_prescriber(models.Model):
    npi = models.IntegerField(primary_key=True, validators=[RegexValidator(
        regex='^.{10}$', message='Length has to be 10', code='nomatch')])  # (PK)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.ForeignKey(
        'pd_statedata', null=True, blank=True, on_delete=models.SET_NULL)  # (FK)
    credentials = models.CharField(max_length=20)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField(default=0)

    def __str__(self):
        return (self.fname + ' ' + self.lname)

    def save(self):
        super(pd_prescriber, self).save()


# pd_statedata √
class pd_statedata(models.Model):
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(max_length=2)  # (PK)
    population = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)

    def __str__(self):
        return (self.stateabbrev)
