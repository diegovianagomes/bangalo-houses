from django.db import models

class Supplier(models.Model):
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='supplier'
    )
    company_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    
class Architect(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class House(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    architect = models.ForeignKey(
        Architect,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='houses'
    )
    dimensions = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    #price = models.DecimalField(max_digits=12, decimal_places=2, help_text='Price in USD' )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='houses'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class HouseImages(models.Model):

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='house_images/'
    )
    caption = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"Image of {self.house.title}"

