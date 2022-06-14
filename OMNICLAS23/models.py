from django.db import models

# Create your models here.
class OmniClass23(models.Model):
    idOmc23 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23')
    numMat = models.IntegerField(null=False)
    Codigo = models.CharField(max_length=18, null=False)
    descriEng = models.CharField(max_length=120, blank=True, null=True)
    descriSpa = models.CharField(max_length=120, blank=True, null=True)
    Nivel = models.IntegerField(null=False)
    regFinal = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omniclass23"



class OMC23Nivel1(models.Model):
    idOmc23N1 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc23N1')
    Codigo = models.CharField(max_length=10, null=False)
    descriEng = models.CharField(max_length=100, null= False)
    descriSpa = models.CharField(max_length=100, null= False)
    definicionEng = models.CharField(max_length=300, blank= True, null= True)
    definicionSpa = models.CharField(max_length=470, blank= True, null= True)
    ejemploEng = models.CharField(max_length=300, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=400, blank= True, null= True)
    fk_EnvOmc = models.IntegerField(blank= True,null=True)

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel1"

class OMC23Nivel2(models.Model):
    idOmc23N2 = models.BigAutoField(auto_created=True, primary_key= True, serialize=False, verbose_name='idOmc23N2')
    numMat = models.IntegerField(blank= True, null= True)
    Codigo = models.CharField(max_length=10, null= False)
    descriEng = models.CharField(max_length=100, null= False)
    descriSpa = models.CharField(max_length=110, blank= True, null= True)
    definicionEng = models.CharField(max_length=300, blank= True, null= True)
    definicionSpa = models.CharField(max_length=470, blank= True, null= True)
    ejemploEng = models.CharField(max_length=300, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=400, blank= True, null= True)
    regFinal = models.BooleanField(null= False)
    fk_Omc23N1 = models.ForeignKey(OMC23Nivel1, on_delete=models.CASCADE, db_column='fk_Omc23N1', verbose_name='Nivel 1')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel2"

class OMC23Nivel3(models.Model):
    idOmc23N3 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N3')
    numMat = models.IntegerField(blank= True, null= True)
    Codigo = models.CharField(max_length=10, null=False)
    descriEng = models.CharField(max_length=100, null=False)
    descriSpa = models.CharField(max_length=110, blank= True, null=True)
    definicionEng = models.CharField(max_length=150, blank= True, null= True)
    definicionSpa = models.CharField(max_length=200, blank= True, null= True)
    ejemploEng = models.CharField(max_length=300, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=400, blank= True, null= True)
    regFinal = models.BooleanField(null= False)
    fk_Omc23N2 = models.ForeignKey(OMC23Nivel2, on_delete=models.CASCADE, db_column='fk_Omc23N2', verbose_name='Nivel 2')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'
    
    class Meta:
        db_table = "Omc23Nivel3"

class OMC23Nivel4(models.Model):
    idOmc23N4 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N4')
    numMat = models.IntegerField(blank= True, null= True)
    Codigo = models.CharField(max_length=15, null = False)
    descriEng = models.CharField(max_length=100, null = False)
    descriSpa = models.CharField(max_length=110, blank= True, null= True)
    definicionEng = models.CharField(max_length=150, blank= True, null= True)
    definicionSpa = models.CharField(max_length=200, blank= True, null= True)
    ejemploEng = models.CharField(max_length=300, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=400, blank= True, null= True)
    regFinal = models.BooleanField(null= False)
    fk_Omc23N3 = models.ForeignKey(OMC23Nivel3, on_delete=models.CASCADE, db_column='fk_Omc23N3', verbose_name='Nivel 3')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel4"

class OMC23Nivel5(models.Model):
    idOmc23N5 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N5')
    numMat = models.IntegerField(blank= True, null= True)
    Codigo = models.CharField(max_length=15, null=False)
    descriEng = models.CharField(max_length=120, null=False)
    descriSpa = models.CharField(max_length=120, blank= True, null=True)
    definicionEng = models.CharField(max_length=150, blank= True, null= True)
    definicionSpa = models.CharField(max_length=200, blank= True, null= True)
    ejemploEng = models.CharField(max_length=400, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=300, blank= True, null= True)
    regFinal = models.BooleanField(null= False)
    fk_Omc23N4 = models.ForeignKey(OMC23Nivel4, on_delete=models.CASCADE, db_column='fk_Omc23N4', verbose_name='Nivel 4')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = 'Omc23Nivel5'

class OMC23Nivel6(models.Model):
    idOmc23N6 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N6')
    numMat = models.IntegerField(blank= True, null= True)
    Codigo = models.CharField(max_length=18, null=False)
    descriEng = models.CharField(max_length=100, null= False)
    descriSpa = models.CharField(max_length=100, blank= True, null= True)
    definicionEng = models.CharField(max_length=150, blank= True, null= True)
    definicionSpa = models.CharField(max_length=200, blank= True, null= True)
    ejemploEng = models.CharField(max_length=300, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=400, blank= True, null= True)
    regFinal = models.BooleanField(null= False)
    fk_Omc23N5 = models.ForeignKey(OMC23Nivel5, on_delete=models.CASCADE, db_column='fk_Omc23N5', verbose_name='Nivel 5')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel6"