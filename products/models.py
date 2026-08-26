from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title=models.CharField(_("title"),max_length=50)
    description=models.TextField(_("description"))# It explain about category
    avatar=models.ImageField(_("avatar"),blank=True,upload_to="products/")
    categories=models.ManyToManyField("Category",verbose_name=_("categories"),blank=True)
    is_enable=models.BooleanField(_("is enable"),default=True)
    created_time=models.DateTimeField(("created time"),auto_now_add=True)
    updated_time=models.DateTimeField(_("updated time"),auto_now=True)
    
    class Meta:
        db_table="products"
        verbose_name=_("product")
        verbose_name_plural=_("products")
    
    

class Category(models.Model):
    parent=models.ForeignKey("self",verbose_name=_("parent"),blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(("title"),max_length=50)
    description=models.TextField(_("description"))# It explain about category
    avatar=models.ImageField(_("avatar"),blank=True,upload_to="categories/")
    is_enable=models.BooleanField(_("is enable"),default=True)
    created_time=models.DateTimeField(("created time"),auto_now_add=True)
    updated_time=models.DateTimeField(_("updated time"),auto_now=True)
    
    class Meta:
        db_table="categories"
        verbose_name=_("category")
        verbose_name_plural=_("categories")
        
    
    
class File(models.Model):
    product=models.ForeignKey("Product",verbose_name=_("product"),on_delete=models.CASCADE)
    title=models.CharField(("title"),max_length=50)
    file=models.FileField(("file"),upload_to="files/%Y/%m/%d/")
    is_enable=models.BooleanField(_("is enable"),default=True)
    created_time=models.DateTimeField(("created time"),auto_now_add=True)
    updated_time=models.DateTimeField(_("updated time"),auto_now=True)
    
    class Meta:
            db_table="files"
            verbose_name=_("file")
            verbose_name_plural=_("files")
        
# Create your models here.
