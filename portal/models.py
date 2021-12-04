# Create your models here.
from django.db import models
from django.core.validators import RegexValidator


# pd_drugs √
class Drugs(models.Model):
    drugname = models.CharField(max_length=30)
    isopioid = models.CharField(max_length=5)

    def __str__(self):
        return (self.drugname)


# pd_statedata √
class State(models.Model):
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(max_length=2, primary_key=True)  # (PK)
    population = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)

    def __str__(self):
        return (self.stateabbrev)


# pd_credentials √
class Credentials(models.Model):
    credentials = models.CharField(max_length=20)

    def __str__(self):
        return (self.credentials)


# pd_prescriber √
class Prescribers(models.Model):
    npi = models.IntegerField(primary_key=True, validators=[RegexValidator(
        regex='^.{10}$', message='Length has to be 10', code='nomatch')])  # (PK)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField(default=0)
    credentials = models.ManyToManyField(
        Credentials)  # many to many with credentials
    state = models.ForeignKey(State, null=True,
                              blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (self.npi)

    def save(self):
        super(Prescribers, self).save()


# pd_triple
class Triple(models.Model):
    id = models.IntegerField(primary_key=True, validators=[RegexValidator(
        regex='^.{6}$', message='Length has to be 6', code='nomatch')])  # (PK)
    qty = models.IntegerField(default=0)
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    prescriberid = models.ForeignKey(Prescribers, on_delete=models.CASCADE)

    def __str__(self):
        return (self.qty)
