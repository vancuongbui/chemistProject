from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify   #for slug
from categories.models import Category
# Create your models here.
class Product(models.Model):
    productId = models.IntegerField(primary_key=True,null = False, unique=True)
    name = models.CharField(max_length = 255, unique=True)
    slug = models.SlugField(allow_unicode = True, unique = True)
    savePrice = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    currentPrice = models.DecimalField(max_digits=7, decimal_places=2) 
    imagePath = models.ImageField(default='No_imange_yet')       
    updateDate = models.DateField(default = '2018-1-20')
    category = models.ForeignKey(Category,related_name="product",on_delete=models.CASCADE)
    #priceRecord = models.ForeignKey(PriceRecord, related_name='product',on_delete=models.CASCADE, blank = True)
    #Note that, ralated_name is used to query up in the relationship
    #such as, myCategory = Category.objects.filter(productType__productId=40022)
    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self,**kwargs):
        return reverse('products:detail',kwargs = {'slug':self.slug})

    def discount(self):  #return value as%
        theDiscount = self.savePrice/(self.currentPrice + self.savePrice)
        return theDiscount

    class Meta:
        ordering = ['name'] 

class PriceRecord(models.Model):
    updateDate = models.DateField(default = '2018-1-20')
    savePrice = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    currentPrice = models.DecimalField(max_digits=7, decimal_places=2, default = 0) 
    
    def __str__(self):
        return self.updateDate

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)







