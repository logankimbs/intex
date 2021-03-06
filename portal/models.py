from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields.related import ForeignKey


# Drugs √
class Drugs(models.Model):
    drugname = models.CharField(max_length=30, primary_key=True)
    isopioid = models.CharField(max_length=5)

    def __str__(self):
        return (self.drugname)


# State √
class State(models.Model):
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(max_length=2, primary_key=True)  # (PK)
    population = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)

    def __str__(self):
        return (self.stateabbrev)


# Credentials √
class Credentials(models.Model):
    credentials = models.CharField(max_length=20)

    def __str__(self):
        return (self.credentials)


# Prescribers √
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
    state = models.ForeignKey(State, null=True, db_constraint=False,
                              blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (
            str(self.npi)
        )

    def save(self):
        super(Prescribers, self).save()


# Triple
class Triple(models.Model):
    id = models.IntegerField(primary_key=True, validators=[RegexValidator(
        regex='^.{6}$', message='Length has to be 6', code='nomatch')])  # (PK)
    qty = models.IntegerField(default=0)
    drug = models.ForeignKey(
        Drugs, on_delete=models.CASCADE, db_constraint=False)
    prescriberid = models.ForeignKey(
        Prescribers, on_delete=models.CASCADE, db_constraint=False)

    def __str__(self):
        return (
            str(self.qty)
        )
