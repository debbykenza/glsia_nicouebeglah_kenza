from django.db import models

class Utilisateur(models.Model):
    login = models.CharField(max_length=100)
    motdepasse = models.CharField(max_length=100)
    actif = models.BooleanField(default=True)

class Personne(models.Model):
    code = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    datenaissance = models.DateField()
    civilite = models.CharField(max_length=20)

class Patient(Personne):
    dateenreg = models.DateField()

class Medecin(Personne):
    titre_medecin = models.CharField(max_length=100)

class Specialite(models.Model):
    code = models.CharField(max_length=50, unique=True)
    libelle = models.CharField(max_length=100)

class AffecterSpecialite(models.Model):
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    dateaffectation = models.DateField()
    actif = models.BooleanField(default=True)

class TypeActe(models.Model):
    code = models.IntegerField(primary_key=True)
    libelle = models.CharField(max_length=100)

class Acte(models.Model):
    code_acte = models.CharField(max_length=50, unique=True)
    libelle_acte = models.CharField(max_length=100)
    montant_acte = models.IntegerField()
    type_acte = models.ForeignKey(TypeActe, on_delete=models.SET_NULL, null=True)

class Consultation(models.Model):
    codeconsultation = models.CharField(max_length=50, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    dateconsultation = models.DateField()
    datefinvaliditeconsultation = models.DateField(null=True, blank=True)

class Facture(models.Model):
    code_facture = models.CharField(max_length=50, unique=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    typefacture = models.CharField(max_length=100)
    dateenreg_facture = models.DateField()
    datepaiement_facture = models.DateField(null=True, blank=True)
    montant_facture = models.IntegerField()
    montant_payefacture = models.IntegerField()

class FactureDetail(models.Model):
    code_detailfacture = models.CharField(max_length=50, unique=True)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    acte = models.ForeignKey(Acte, on_delete=models.CASCADE)
    montant_facturedetail = models.IntegerField()

class Medicament(models.Model):
    code_medicament = models.CharField(max_length=50, unique=True)
    libelle_medicament = models.CharField(max_length=100)

class Ordonnance(models.Model):
    code_ordonnance = models.CharField(max_length=50, unique=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    date_ordonnance = models.DateField()

class OrdonnanceDetail(models.Model):
    code_ordonnancedetail = models.CharField(max_length=50, unique=True)
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    posologie_medicament = models.TextField()
