from django.db import models


# home .

class CategoryProductsModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

   


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'names'


class ProductsModel(models.Model):
    category = models.ForeignKey(CategoryProductsModel, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=255)
    price = models.TextField()

        


    def __str__(self):
        return self.name
    




# table and booking
class CategoryTableModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    
    

    def __str__(self):
        return self.name



class TableModel(models.Model):
    objects = object
    category = models.ForeignKey(CategoryTableModel, on_delete=models.CASCADE)
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.table_number


class Booking(models.Model):
    table = models.ForeignKey(TableModel, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.guest_name} - {self.table.table_number} ({self.check_in_date} to {self.check_out_date})"


class AboutModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
