from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self) -> str:
        return self.name
    
    
    
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    otp=models.IntegerField(null=True)
    image=models.ImageField(upload_to="media", default="https://bootdey.com/img/Content/avatar/avatar7.png")
    
    def __str__(self) -> str:
        return self.name
    


class price(models.Model):
    name=models.CharField(max_length=50)  
    
    def __str__(self):
        return self.name
 
 
class size(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class color(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name   
      
class Main_category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    
class Sub_category(models.Model):
    main_category=models.ForeignKey(Main_category,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
    
ch=(("Black","Black"),("White","White"),("Red","Red"),("Blue","Blue"),("Green","Green"))
chh=(("0 - 500" , "0 - 500"),("500 - 3000" , "500 - 3000"),("3000 - 10000" , "3000 - 10000"),("10000 - 40000" , "10000 - 40000"),("40000 - 60000","40000 - 60000"))
class product(models.Model):
    main_category=models.ForeignKey(Main_category,on_delete=models.CASCADE,blank=True,null=True)
    sub_category=models.ForeignKey(Sub_category,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="media")
    name=models.CharField(max_length=50)
    quantity=models.IntegerField(default=1)
    # price1=models.ForeignKey(price,on_delete=models.CASCADE,null=True,blank=True)
    price1=models.CharField(choices=chh,blank=True,null=True,max_length=50)
    size1=models.ManyToManyField(size,null=True,blank=True)
    star=models.IntegerField()
    color=models.ManyToManyField(color,blank=True,null=True,max_length=50)
    price=models.IntegerField()
    
        
    def __str__(self):
        return self.name
    
    

    
class Add_to_cart(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to="media")
    name=models.CharField(max_length=50,null=True,blank=True)
    size=models.CharField(max_length=40,null=True,blank=True)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField()
    
        
    def __str__(self):
        return self.name
    
    
ch=(("India","India"),("Pakistan","Pakistan"),("Ameriaca","America"),("Afghanistan","Afghanistan"),("London","London"),("Canada","Canada")) 
class Address(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    country=models.CharField(choices=ch,max_length=50,blank=True,null=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    

    def __str__(self):
        return self.first_name


        
    
class Order(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    order_id=models.CharField(max_length=30,blank=True,null=True)
    image=models.ImageField(upload_to="media")
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()
    total_price=models.IntegerField()
    datetime=models.DateTimeField(auto_now=True,blank=True,null=True)
    def __str__(self):
        return self.name
    
    
    
    
class Add_to_whishlist(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to="media")
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    
    
    
    def __str__(self):
        return self.name
    
    

class Rating(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)  
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True,null=True)  
    comment=models.TextField()
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    date=models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
                                        
        return self.name
    
    
    
    
class coupon_code(models.Model):
    code=models.CharField(max_length=10)
    discount=models.IntegerField()
    
    def __str__(self):
        return self.code