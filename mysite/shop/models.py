from django.db import models


class Category(models.Model):
    title_category = models.CharField(max_length=100)

    def __str__(self):
        return self.title_category


class Clothes(models.Model):
    title_clothes = models.CharField(max_length=100, verbose_name="модель")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_clothes


class Color(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    title_product = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    CHOICES_SIZE = (
        ("38 XXS", "40 XS"),
        ("42 S", "44 M"),
        ("46 M", "48 L"),
        ("50 L", "52 XL"),
        ("54-56 XXL", "58 XXXL"),
        ("60-64 4XL", "66-70 5XL")
    )
    size = models.CharField(verbose_name='размер', max_length=16, choices=CHOICES_SIZE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(verbose_name='описание')
    color = models.CharField(verbose_name='цвет', max_length=16)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                default=1, verbose_name="Оценка")
    data = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title_product


class ProductPhoto(models.Model):
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя")
    email = models.EmailField()
    phone = models.CharField(max_length=10, verbose_name="Номер телефона")
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Basket(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_favorite', default=1)
    count = models.PositiveIntegerField(verbose_name='количество товара', default=1)
    summ_products = models.IntegerField(verbose_name="общая сумма")


class Order(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    products = models.ManyToManyField(Basket)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class News(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.ImageField(upload_to="images/news/", blank=True, null=True)
    data = models.DateField(auto_now=True,blank=True, null=True)
