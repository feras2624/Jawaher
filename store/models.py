from django.db import models


class Catagory(models.Model):
    name=models.CharField(max_length=128)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name=models.CharField(max_length=128)
    desc=models.CharField(max_length=256)
    image=models.ImageField(null=True,blank=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    

class Galary(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name
    


class Galaryphoto(models.Model):
    image=models.ImageField(null=True,blank=True)
    galary=models.ForeignKey(Galary,on_delete=models.CASCADE)

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class MSG(models.Model):
    fname=models.CharField(max_length=128)
    lname=models.CharField(max_length=128)
    email=models.EmailField()
    msg=models.TextField(max_length=1024)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fname