from django.db import models

# Create your models here.

class GrandParent(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Parents(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent = models.OneToOneField(GrandParent, related_name="parents", on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Siblings(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    

    def __str__(self):
        return self.name
        

class Children(models.Model):
    child = models.ForeignKey(Parents, related_name="parents", on_delete=models.CASCADE)
    grandparent_name = models.ForeignKey(GrandParent, related_name="grandparents", on_delete=models.CASCADE)
    sibling = models.ManyToManyField(Siblings)
    
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name