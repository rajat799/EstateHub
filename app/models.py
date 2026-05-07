from django.db import models
import datetime

# =============================================================================
# EstateHub — Database Models
# =============================================================================
# SECURITY NOTE: Password fields use max_length=256 to store hashed passwords.
# Django's make_password() produces strings ~128 chars long.
# =============================================================================


class AdminMaster(models.Model):
    """Admin user accounts with full system access."""
    ad_id = models.AutoField(primary_key=True)
    ad_name = models.CharField(max_length=100)
    ad_mobile = models.CharField(max_length=100)
    ad_email = models.CharField(max_length=100, unique=True)  # SECURITY: prevent duplicate admin emails
    ad_password = models.CharField(max_length=256)  # SECURITY: increased for hashed passwords
    ad_role = models.CharField(max_length=100, default="")
    ad_status = models.IntegerField(default=0)
    ad_created_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ad_name} ({self.ad_email})"

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"


class AdminBooking(models.Model):
    """Legacy booking records managed by admins."""
    b_id = models.AutoField(primary_key=True)
    b_property_name = models.CharField(max_length=100)
    b_purchaser_name = models.CharField(max_length=100)
    b_place = models.CharField(max_length=100)
    b_amount = models.CharField(max_length=100)
    b_date = models.CharField(max_length=100)
    b_status = models.IntegerField(default=0)
    b_created_by = models.CharField(max_length=100)

    def __str__(self):
        return f"Booking: {self.b_purchaser_name} - {self.b_property_name}"

    class Meta:
        verbose_name = "Admin Booking"
        verbose_name_plural = "Admin Bookings"


class AdminSeller(models.Model):
    """Seller accounts who list properties and products."""
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100)
    s_mobile = models.CharField(max_length=100)
    s_email = models.CharField(max_length=100, unique=True)  # SECURITY: prevent duplicate seller emails
    s_password = models.CharField(max_length=256, default="")  # SECURITY: increased for hashed passwords
    s_role = models.CharField(max_length=100, default="")
    s_address = models.CharField(max_length=200, default="")
    s_status = models.IntegerField(default=0)
    s_created_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.s_name} ({self.s_email})"

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"


class Category(models.Model):
    """Product/Property categories managed by sellers."""
    ca_id = models.AutoField(primary_key=True)
    ca_name = models.CharField(max_length=100)
    ca_status = models.IntegerField(default=0)
    ca_created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.ca_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Booking(models.Model):
    """Property booking records from users."""
    bk_id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f"Booking #{self.bk_id}: {self.bk_user_name} (Property {self.bk_property_id})"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


class Properties(models.Model):
    """Real estate property listings."""
    pr_id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f"{self.pr_name or 'Property'} - {self.pr_place} (₹{self.pr_fee})"

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class Register(models.Model):
    """Registered website users (buyers)."""
    us_id = models.AutoField(primary_key=True)
    us_name = models.CharField(max_length=100, default="")
    us_email = models.CharField(max_length=100, unique=True)  # SECURITY: prevent duplicate user emails
    us_mobile = models.CharField(max_length=100, default="")
    us_password = models.CharField(max_length=256)  # SECURITY: increased for hashed passwords
    us_status = models.IntegerField(default=0)
    us_created_by = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.us_name} ({self.us_email})"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Products(models.Model):
    """Interior furniture/product listings."""
    pd_id = models.AutoField(primary_key=True)
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

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Cart(models.Model):
    """Shopping cart items (temporary, per-user)."""
    ct_id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f"Cart: {self.ct_name} x{self.ct_qty} ({self.ct_user_email})"

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"


class Order(models.Model):
    """Completed purchase orders."""
    or_id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f"Order #{self.or_id}: {self.or_name} - ₹{self.or_total_amount}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class PurchasedProducts(models.Model):
    """Individual products within an order."""
    pp_id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f"{self.pp_name} x{self.pp_qty} (Order #{self.pp_or_id})"

    class Meta:
        verbose_name = "Purchased Product"
        verbose_name_plural = "Purchased Products"
