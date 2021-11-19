from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length = 100 , null=True)
    email = models.CharField(max_length = 100 , null=True)
    tele = models.CharField(max_length = 50 , null=True)
    age = models.CharField( max_length=2 , null=True)
    date_created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 100 , null=True)
    
    def __str__(self):
        return self.name


class book(models.Model):
    STATUS= (
        ('comidy','comidy'),
        ('Fantasy','Fantasy'),
        ('Horror','Horror')
    )
    name = models.CharField(max_length = 100 , null=True)
    statu = models.CharField(max_length = 50 , null=True , choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    ville = models.CharField(max_length = 100 , null=True)

    client = models.ForeignKey(Client , null=True ,on_delete=models.SET_NULL )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name




class Order(models.Model):
    STATU = (
        ('arrived ','arrived '),
        ('lost ','lost '),
        ('did_not_arrive ','did_not_arrive ')
    )
    client = models.ForeignKey(Client , null=True , on_delete=models.SET_NULL)
    books = models.ForeignKey(book , null=True , on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    status = models.CharField(max_length = 50 , null=True , choices=STATU)
    
    