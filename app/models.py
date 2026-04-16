from django.db import models
import datetime

# Create your models here.


class AdminMaster(models.Model):
    ad_id = models.AutoField(primary_key=True, unique=True)
    ad_name = models.CharField(max_length=100)
    ad_mobile = models.CharField(max_length=100)
    ad_email = models.CharField(max_length=100)
    ad_password = models.CharField(max_length=100)
    ad_role = models.CharField(max_length=100, default="")
    ad_status = models.IntegerField(default=0)
    ad_created_by = models.CharField(max_length=100)


class AdminBooking(models.Model):
    b_id = models.AutoField(primary_key=True, unique=True)
    b_property_name = models.CharField(max_length=100)
    b_purchaser_name = models.CharField(max_length=100)
    b_place = models.CharField(max_length=100)
    b_amount = models.CharField(max_length=100)
    b_date = models.CharField(max_length=100)
    b_status = models.IntegerField(default=0)
    b_created_by = models.CharField(max_length=100)


class AdminSeller(models.Model):
    s_id = models.AutoField(primary_key=True, unique=True)
    s_name = models.CharField(max_length=100)
    s_mobile = models.CharField(max_length=100)
    s_email = models.CharField(max_length=100)
    s_password = models.CharField(max_length=100, default="")
    s_role = models.CharField(max_length=100, default="")
    s_address = models.CharField(max_length=200, default="")
    s_status = models.IntegerField(default=0)
    s_created_by = models.CharField(max_length=100)


class Category(models.Model):
    ca_id = models.AutoField(primary_key=True, unique=True)
    ca_name = models.CharField(max_length=100)
    ca_status = models.IntegerField(default=0)
    ca_created_by = models.CharField(max_length=100)


class Booking(models.Model):
    bk_id = models.AutoField(primary_key=True, unique=True)
    bk_user_name = models.CharField(max_length=100)
    bk_user_email = models.CharField(max_length=100)
    bk_user_phone = models.CharField(max_length=100, default="")
    bk_seller_name = models.CharField(max_length=100)
    bk_seller_email = models.CharField(max_length=100)
    bk_user_address = models.CharField(max_length=100, default="")
    bk_property_id = models.CharField(max_length=100)
    bk_amount = models.CharField(max_length=100)
    bk_status = models.CharField(max_length=100, default=0)
    bk_created_by = models.CharField(max_length=100)
    bk_created_date = models.DateField(default=datetime.date.today)


class Properties(models.Model):
    pr_id = models.AutoField(primary_key=True, unique=True)
    pr_image = models.ImageField(upload_to="property/", default="")
    pr_image1 = models.ImageField(upload_to="property/", default="")
    pr_name = models.CharField(max_length=100, default="")
    pr_seller_name = models.CharField(max_length=100)
    pr_category = models.CharField(max_length=100, default="")
    pr_property_type = models.CharField(max_length=100)
    pr_place = models.CharField(max_length=100)
    pr_location = models.CharField(max_length=100, default="")
    pr_fee = models.CharField(max_length=100, default="")
    pr_desc = models.CharField(max_length=500, default="")
    pr_date = models.CharField(max_length=100)
    pr_mobile_no = models.CharField(max_length=100)
    pr_status = models.IntegerField(default=0)
    pr_sold = models.CharField(max_length=100, default="NO")
    pr_created_by = models.CharField(max_length=100)


class Register(models.Model):
    us_id = models.AutoField(primary_key=True, unique=True)
    us_name = models.CharField(max_length=100, default="")
    us_email = models.CharField(max_length=100)
    us_mobile = models.CharField(max_length=100, default="")
    us_password = models.CharField(max_length=100)
    us_status = models.IntegerField(default=0)
    us_created_by = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.us_name} ({self.us_email})"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Products(models.Model):
    pd_id = models.AutoField(primary_key=True, unique=True)
    pd_image = models.ImageField(upload_to="product/", default="")
    pd_name = models.CharField(max_length=100, default="")
    pd_category = models.CharField(max_length=100, default="")
    pd_price = models.CharField(max_length=100, default="")
    pd_desc = models.CharField(max_length=2000, default="")
    pd_date = models.CharField(max_length=100)
    pd_status = models.IntegerField(default=0)
    pd_created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.pd_name


class Cart(models.Model):
    ct_id = models.AutoField(primary_key=True, unique=True)
    ct_image = models.CharField(max_length=200, default="")
    ct_name = models.CharField(max_length=100, default="")
    ct_category = models.CharField(max_length=100, default="")
    ct_price = models.CharField(max_length=100, default="")
    ct_desc = models.CharField(max_length=500, default="")
    ct_qty = models.CharField(max_length=100, default="")
    ct_total_amount = models.CharField(max_length=100, default="")
    ct_user_email = models.CharField(max_length=100, default="")
    ct_status = models.IntegerField(default=0)
    ct_created_by = models.CharField(max_length=100)

class Order(models.Model):
    or_id = models.AutoField(primary_key=True, unique=True)
    or_name = models.CharField(max_length=100, default="")
    or_date = models.CharField(max_length=100, default="")
    or_transaction_id = models.CharField(max_length=100, default="")
    or_mobile = models.CharField(max_length=100, default="")
    or_email = models.CharField(max_length=100, default="")
    or_address = models.CharField(max_length=500, default="")
    or_total_amount = models.CharField(max_length=100, default="")
    or_user_email = models.CharField(max_length=100, default="")
    or_status = models.CharField(max_length=100, default="")
    or_created_by = models.CharField(max_length=100)

class PurchasedProducts(models.Model):
    pp_id = models.AutoField(primary_key=True, unique=True)
    pp_or_id = models.CharField(max_length=200, default="")
    pp_image = models.CharField(max_length=200, default="")
    pp_name = models.CharField(max_length=100, default="")
    pp_category = models.CharField(max_length=100, default="")
    pp_price = models.CharField(max_length=100, default="")
    pp_desc = models.CharField(max_length=500, default="")
    pp_qty = models.CharField(max_length=100, default="")
    pp_total_amount = models.CharField(max_length=100, default="")
    pp_user_email = models.CharField(max_length=100, default="")
    pp_status = models.IntegerField(default=0)
    pp_created_by = models.CharField(max_length=100, default="")
