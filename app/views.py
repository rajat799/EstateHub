from django.shortcuts import render, redirect
from app.models import AdminMaster
from app.models import AdminSeller
from app.models import Category
from app.models import Properties
from app.models import Products
from app.models import Order
from app.models import PurchasedProducts
from app.models import Cart
from app.models import Booking
from app.models import Register
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from datetime import date
from django.db.models import Q
from datetime import date, timedelta


# Create your views here.
# Web Page


def webIndex(request):
    countApartment = Properties.objects.filter(pr_category="Apartment").count()
    countVilla = Properties.objects.filter(pr_category="Villa").count()
    countHome = Properties.objects.filter(pr_category="Home").count()
    countOffice = Properties.objects.filter(pr_category="Office").count()
    countBuilding = Properties.objects.filter(pr_category="Building").count()
    countTownhouse = Properties.objects.filter(pr_category="Townhouse").count()
    countShop = Properties.objects.filter(pr_category="Shop").count()
    countGarage = Properties.objects.filter(pr_category="Garage").count()

    context = {
        "countApartment": countApartment,
        "countVilla": countVilla,
        "countHome": countHome,
        "countOffice": countOffice,
        "countBuilding": countBuilding,
        "countTownhouse": countTownhouse,
        "countShop": countShop,
        "countGarage": countGarage,
    }
    return render(request, "web/index.html", context)


def webAbout(request):
    return render(request, "web/about.html")


def webContact(request):
    return render(request, "web/contact.html")


def webProperty(request):
    return render(request, "web/property.html")


def webPropertylist(request):
    return render(request, "web/propertylist.html")
    
def webProductlist(request):
    return render(request, "web/productlist.html")



def webPropertytype(request):
    return render(request, "web/propertytype.html")


def webTestimonial(request):
    return render(request, "web/testimonial.html")


def webRegister(request):
    return render(request, "web/register.html")


def webLogin(request):
    return render(request, "web/web_login.html")


def user(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/user.html")

def faq(request):
    return render(request, "web/faq.html")

def help(request):
    return render(request, "web/help.html")


#  Admin Pages


def adminAdmin(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/admin.html")


def openLogin(request):
    return render(request, "admin_login.html")


def adminProfile(request):
    if "email" not in request.session:
        return redirect("/admin_login/")
    if request.session.get("role") == "Admin":
        return render(request, "admin/profile.html")
    else:
        return render(request, "seller/profile.html")


def adminPilot(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/pilot.html")


def adminBooking(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/booking.html")


def adminProperties(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/properties.html")

def adminProducts(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/products.html")

def adminOrders(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/orders.html")


def adminSeller(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return redirect("/admin_login/")
    return render(request, "admin/seller.html")


def cart(request):
    return render(request, "web/cart.html")

def propertyTypes(request):
    return render(request, "web/property_types.html")

def latestProperties(request):
    return render(request, "web/latest_properties.html")

def checkout(request):
    return render(request, "web/checkout.html")



# ////////////////// Admin Backend ///////////////////////////


def checkAdminLogin(request):
    if request.POST["selRole"] == "Admin":
        if AdminMaster.objects.filter(
            ad_email=request.POST["txtEmail"],
            ad_password=request.POST["txtPassword"],
            ad_status="0",
        ).exists():
            admin_json = AdminMaster.objects.filter(
                ad_email=request.POST["txtEmail"]
            ).values()
            data = list(admin_json)
            dictValue = data[0]
            request.session["email"] = dictValue["ad_email"]
            request.session["role"] = dictValue["ad_role"]
            request.session["name"] = dictValue["ad_name"]
            return HttpResponse(dictValue["ad_role"])
        else:
            return HttpResponse("0")
    else:
        if AdminSeller.objects.filter(
            s_email=request.POST["txtEmail"],
            s_password=request.POST["txtPassword"],
            s_status="0",
        ).exists():
            admin_json = AdminSeller.objects.filter(
                s_email=request.POST["txtEmail"]
            ).values()
            data = list(admin_json)
            dictValue = data[0]
            request.session["email"] = dictValue["s_email"]
            request.session["role"] = dictValue["s_role"]
            request.session["name"] = dictValue["s_name"]
            return HttpResponse(dictValue["s_role"])
        else:
            return HttpResponse("0")


def logout(request):
    request.session.delete()
    return render(request, "admin_login.html", {})


# logoutWeb is defined below with proper session cleanup


# AdminMaster
def adminDetails(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return JsonResponse({"error": "Unauthorized"}, status=401)
    
    if request.POST["action"] == "add":
        AdminMaster.objects.create(
            ad_name=request.POST["txtName"],
            ad_email=request.POST["txtEmail"],
            ad_mobile=request.POST["txtMobileNo"],
            ad_password=request.POST["txtPassword"],
            ad_role=request.POST["selRole"],
        )

    elif request.POST["action"] == "getData":
        data = AdminMaster.objects.filter(ad_status=0).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = AdminMaster.objects.filter(
            ad_created_by=request.session["email"], ad_id=request.POST["id"]
        ).update(
            ad_name=request.POST["txtName1"],
            ad_email=request.POST["txtEmail1"],
            ad_mobile=request.POST["txtMobileNo1"],
            ad_role=request.POST["selRole1"],
        )

    elif request.POST["action"] == "delete":
        data = AdminMaster.objects.filter(ad_id=request.POST["id"]).update(ad_status=1)

    return HttpResponse()

    # //////////////////////////Seller


def adminSellerDetails(request):
    if "email" not in request.session or request.session.get("role") != "Admin":
        return JsonResponse({"error": "Unauthorized"}, status=401)
    
    if request.POST["action"] == "add":
        AdminSeller.objects.create(
            s_name=request.POST["txtName"],
            s_email=request.POST["txtEmail"],
            s_mobile=request.POST["txtMobileNo"],
            s_password=request.POST["txtPassword"],
            s_role=request.POST["selRole"],
            s_address=request.POST["txtAddress"],
        )

    elif request.POST["action"] == "getData":
        data = AdminSeller.objects.filter(s_status=0).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = AdminSeller.objects.filter(s_id=request.POST["id"]).update(
            s_name=request.POST["txtName1"],
            s_email=request.POST["txtEmail1"],
            s_mobile=request.POST["txtMobileNo1"],
            s_address=request.POST["txtAddress1"],
            s_role=request.POST["selRole1"],
        )

    elif request.POST["action"] == "delete":
        data = AdminSeller.objects.filter(s_id=request.POST["id"]).update(s_status=1)

    return HttpResponse()


#
# seller
def sellerPurchaser(request):
    if "email" not in request.session or request.session.get("role") != "Seller":
        return redirect("/admin_login/")
    return render(request, "seller/seller_booking.html")


def category(request):
    if "email" not in request.session or request.session.get("role") != "Seller":
        return redirect("/admin_login/")
    return render(request, "seller/category.html")


def sellerPropertiess(request):
    if "email" not in request.session or request.session.get("role") != "Seller":
        return redirect("/admin_login/")
    return render(request, "seller/propertiess.html")


def sellerProducts(request):
    if "email" not in request.session or request.session.get("role") != "Seller":
        return redirect("/admin_login/")
    return render(request, "seller/seller_products.html")


    # /////////////////////Seller Backend////////////////////////


def categoryDetails(request):
    if "email" not in request.session or request.session.get("role") != "Seller":
        return JsonResponse({"error": "Unauthorized"}, status=401)
    
    if request.POST["action"] == "add":
        Category.objects.create(
            ca_name=request.POST["txtName"],
            ca_created_by=request.session["email"],
        )

    elif request.POST["action"] == "getData":
        data = Category.objects.filter(
            ca_created_by=request.session["email"], ca_status=0
        ).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = Category.objects.filter(ca_id=request.POST["id"]).update(
            ca_name=request.POST["txtName1"],
            ca_created_by=request.session["email"],
        )

    elif request.POST["action"] == "delete":
        data = Category.objects.filter(ca_id=request.POST["id"]).update(ca_status=1)

    return HttpResponse()


def webCategory(request):
    data = Category.objects.filter(ca_status=0).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


# /////////////////////Seller Backend////////////////////////


def sellerPropertiesDetails(request):
    if "email" not in request.session or request.session.get("role") != "Seller":
        return JsonResponse({"error": "Unauthorized"}, status=401)
    
    if request.POST["action"] == "add":
        Properties.objects.create(
            pr_image=request.FILES["filePhoto"],
            pr_image1=request.FILES["filePhoto1"],
            pr_seller_name=request.POST["txtName"],
            pr_category=request.POST["selCategory"],
            pr_property_type=request.POST["txtProperty"],
            pr_place=request.POST["txtPlace"],
            pr_location=request.POST["selCity"],
            pr_fee=request.POST["txtFee"],
            pr_desc=request.POST["txtDesc"],
            pr_date=request.POST["txtDate"],
            pr_mobile_no=request.POST["txtMobileNo"],
            pr_created_by=request.session["email"],
        )

    elif request.POST["action"] == "getData":
        data = Properties.objects.filter(
            pr_created_by=request.session["email"], pr_status=0
        ).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = Properties.objects.filter(pr_id=request.POST["id"]).update(
            pr_seller_name=request.POST["txtName1"],
            pr_category=request.POST["selCategory1"],
            pr_property_type=request.POST["txtProperty1"],
            pr_place=request.POST["txtPlace1"],
            pr_location=request.POST["selCity1"],
            pr_fee=request.POST["txtFee1"],
            pr_desc=request.POST["txtDesc1"],
            pr_date=request.POST["txtDate1"],
            pr_mobile_no=request.POST["txtMobileNo1"],
            pr_created_by=request.session["email"],
        )

    elif request.POST["action"] == "delete":
        data = Properties.objects.filter(pr_id=request.POST["id"]).update(pr_status=1)

    return HttpResponse()

def adminProductDetails(request):
    try:
        # Check if user is logged in as admin
        if "email" not in request.session or request.session.get("role") != "Admin":
            return JsonResponse({"error": "Unauthorized"}, status=401)
        
        if request.POST["action"] == "add":
            Products.objects.create(
                pd_image=request.FILES["filePhoto"],
                pd_name=request.POST["txtName"],
                pd_category=request.POST["selCategory"],
                pd_price=request.POST["txtPrice"],
                pd_desc=request.POST["txtDesc"],
                pd_date=request.POST["txtDate"],
                pd_created_by=request.session["email"],
            )

        elif request.POST["action"] == "getData":
            # Admin sees ALL products (not filtered by creator)
            data = Products.objects.filter(pd_status=0).values()
            data = list(data)
            return JsonResponse(data, safe=False)

        elif request.POST["action"] == "update":
            data = Products.objects.filter(pd_id=request.POST["id"]).update(
                pd_name=request.POST["txtName1"],
                pd_category=request.POST["selCategory1"],
                pd_price=request.POST["txtPrice1"],
                pd_desc=request.POST["txtDesc1"],
                pd_date=request.POST["txtDate1"],
            )

        elif request.POST["action"] == "delete":
            data = Products.objects.filter(pd_id=request.POST["id"]).update(pd_status=1)

        return HttpResponse()
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def sellerProductsDetails(request):
    try:
        if "email" not in request.session:
            return JsonResponse({"error": "Unauthorized"}, status=401)
        
        if request.POST["action"] == "add":
            Products.objects.create(
                pd_image=request.FILES.get("filePhoto", ""),
                pd_name=request.POST["txtName"],
                pd_category=request.POST["selCategory"],
                pd_price=request.POST["txtPrice"],
                pd_desc=request.POST["txtDesc"],
                pd_date=request.POST["txtDate"],
                pd_created_by=request.session["email"],
            )

        elif request.POST["action"] == "getData":
            data = Products.objects.filter(
                pd_created_by=request.session["email"], pd_status=0
            ).values()
            data = list(data)
            for i in range(len(data)):
                # Filter by name AND (created_by OR empty/null) for backwards compatibility
                user_count = PurchasedProducts.objects.filter(
                    Q(pp_name=data[i]["pd_name"]),
                    Q(pp_created_by=request.session["email"]) | Q(pp_created_by="") | Q(pp_created_by__isnull=True)
                ).values("pp_user_email").distinct().count()
                data[i]["user_count"] = user_count
            return JsonResponse(data, safe=False)

        elif request.POST["action"] == "update":
            data = Products.objects.filter(pd_id=request.POST["id"]).update(
                pd_name=request.POST["txtName1"],
                pd_category=request.POST["selCategory1"],
                pd_price=request.POST["txtPrice1"],
                pd_desc=request.POST["txtDesc1"],
                pd_date=request.POST["txtDate1"],
                pd_created_by=request.session["email"],
            )

        return HttpResponse()
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def sellerViewOrderDetails(request):
    try:
        if "email" not in request.session or request.session.get("role") != "Seller":
            return JsonResponse({"error": "Unauthorized"}, status=401)
        
        product_name = request.POST.get("pd_name")
        seller_email = request.session["email"]
        
        # Get all purchases for this specific product and seller
        # Include empty/null pp_created_by for backwards compatibility with old orders
        purchases = PurchasedProducts.objects.filter(
            Q(pp_name=product_name),
            Q(pp_created_by=seller_email) | Q(pp_created_by="") | Q(pp_created_by__isnull=True)
        ).values()
        
        purchase_list = list(purchases)
        
        # We also want to join with Order info to get Address and Mobile
        for item in purchase_list:
            order_info = Order.objects.filter(or_id=item["pp_or_id"]).values(
                "or_name", "or_mobile", "or_address", "or_email", "or_date"
            ).first()
            if order_info:
                item.update(order_info)
                
        return JsonResponse(purchase_list, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def adminPropertiesDetails(request):
    try:
        if request.POST and request.POST.get("action"):
            if "email" not in request.session or request.session.get("role") != "Admin":
                return JsonResponse({"error": "Unauthorized"}, status=401)
            
            if request.POST.get("action") == "add":
                Properties.objects.create(
                    pr_image=request.FILES.get("filePhoto", ""),
                    pr_image1=request.FILES.get("filePhoto1", ""),
                    pr_seller_name=request.POST["txtName"],
                    pr_category=request.POST["selCategory"],
                    pr_property_type=request.POST["txtProperty"],
                    pr_place=request.POST["txtPlace"],
                    pr_location=request.POST.get("selCity", ""),
                    pr_fee=request.POST["txtFee"],
                    pr_desc=request.POST["txtDesc"],
                    pr_date=request.POST["txtDate"],
                    pr_mobile_no=request.POST["txtMobileNo"],
                    pr_created_by=request.session["email"],
                )
                return HttpResponse()

            elif request.POST.get("action") == "update":
                Properties.objects.filter(pr_id=request.POST["id"]).update(
                    pr_seller_name=request.POST["txtName1"],
                    pr_category=request.POST["selCategory1"],
                    pr_property_type=request.POST["txtProperty1"],
                    pr_place=request.POST["txtPlace1"],
                    pr_location=request.POST.get("selCity1", ""),
                    pr_fee=request.POST["txtFee1"],
                    pr_desc=request.POST["txtDesc1"],
                    pr_date=request.POST["txtDate1"],
                    pr_mobile_no=request.POST["txtMobileNo1"],
                )
                return HttpResponse()

            elif request.POST.get("action") == "delete":
                Properties.objects.filter(pr_id=request.POST["id"]).update(pr_status=1)
                return HttpResponse()

            elif request.POST.get("action") == "getData":
                data = Properties.objects.filter(pr_status=0).values()
                data = list(data)
                return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
        
    data = Properties.objects.filter(pr_status=0).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def webSellerProperties(request):
    yesterday = date.today() - timedelta(days=7)
    print(" Todays Date ", yesterday)

    # Auto-expire bookings older than 7 days
    updateProperty = Booking.objects.filter(Q(bk_created_date__lte=yesterday)).values()
    updatePropertyData = list(updateProperty)

    for value in updatePropertyData:
        try:
            property_id = value["bk_property_id"]
            Properties.objects.filter(pr_id=property_id).update(pr_sold="NO")

            booking_id = value["bk_id"]
            Booking.objects.filter(bk_id=booking_id).update(bk_status="Cancelled")
        except:
            pass

    # Also reset properties whose bookings were already cancelled
    # This prevents properties from being stuck as "sold" after cancellation
    cancelledBookings = Booking.objects.filter(bk_status="Cancelled").values("bk_property_id")
    for cb in cancelledBookings:
        try:
            Properties.objects.filter(pr_id=cb["bk_property_id"], pr_sold="YES").update(pr_sold="NO")
        except:
            pass

    data = Properties.objects.filter(pr_status=0).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values

def webSellerProducts(request):
    data = Products.objects.filter(pd_status=0).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def getWebSearchProperties(request):
    search_name = request.POST.get("txtSearch", "").strip()
    price_from = request.POST.get("txtPriceRangeFrom", 0)
    price_to = request.POST.get("txtPriceRangeTo", 0)
    property_type = request.POST.get("selProperty", "").strip()
    place = request.POST.get("selPlace", "").strip()
    
    data = Properties.objects.filter(
        pr_status=0,
        pr_seller_name__icontains=search_name,
        pr_fee__range=(price_from, price_to),
        pr_property_type=property_type,
        pr_location=place
    ).values()
    
    data = list(data)
    return JsonResponse(data, safe=False)

    
def getWebSearchProducts(request):
    data = Products.objects.filter(
        pd_status=0,
        pd_property_type=request.POST["selProduct"],
        pd_place=request.POST["selPlace"],
    ).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values   


def getWebPlaces(request):
    data = Properties.objects.filter(pr_status=0).values("pr_place").distinct()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def profileDetails(request):
    if "email" not in request.session:
        return JsonResponse({"error": "Unauthorized"}, status=401)
    
    if request.POST["action"] == "getData":
        if request.session["role"] == "Admin":
            data = AdminMaster.objects.filter(
                ad_email=request.session["email"]
            ).values()
            data = list(data)
            values = JsonResponse(data, safe=False)
            return values
        else:
            data = AdminSeller.objects.filter(s_email=request.session["email"]).values()
            data = list(data)
            values = JsonResponse(data, safe=False)
            return values

    if request.POST["action"] == "update":
        if request.session["role"] == "Admin":
            AdminMaster.objects.filter(ad_id=request.POST["id"]).update(
                ad_name=request.POST["txtName"],
                ad_email=request.POST["txtEmail"],
                ad_mobile=request.POST["txtMobileNo"],
                ad_password=request.POST["txtPassword"],
            )
        else:
            AdminSeller.objects.filter(s_id=request.POST["id"]).update(
                s_name=request.POST["txtName"],
                s_email=request.POST["txtEmail"],
                s_mobile=request.POST["txtMobileNo"],
                s_password=request.POST["txtPassword"],
            )

    return HttpResponse()


def userUpdateProfileDetails(request):
    Register.objects.filter(us_id=request.POST["id"]).update(
        us_name=request.POST["txtName"],
        us_email=request.POST["txtEmail"],
        us_mobile=request.POST["txtMobileNo"],
    )

    return HttpResponse()


def getWebProfile(request):
    if "web_email" in request.session:
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def userProfileDetails(request):
    data = Register.objects.filter(us_email=request.session["web_email"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


# def getBookings(request):
# 	if request.session['role'] == "Admin":
# 		data = Booking.objects.filter().values()
# 		data = list(data)
# 		values = JsonResponse(data, safe=False)
# 		return values;

# 	else:
# 		data = Booking.objects.filter(bk_created_by=request.session['email']).values()
# 		data = list(data)
# 		values = JsonResponse(data, safe=False)
# 		return values;


def openSingleProperty(request):
    if "web_email" in request.session:
        return render(request, "web/single_property.html")
    else:
        return render(request, "web/web_login.html")

def openSingleProduct(request):
    if "web_email" in request.session:
        return render(request, "web/single_product.html")
    else:
        return render(request, "web/web_login.html")



def getSingleItem(request):
    data = Properties.objects.filter(pr_id=request.POST["txtID"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values

def getSingleProductItem(request):
    data = Products.objects.filter(pd_id=request.POST["txtID"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def bookProperty(request):
    if "web_email" in request.session:
        if Booking.objects.filter(
            bk_user_email=request.POST["txtName"], bk_status="0"
        ).exists():
            return HttpResponse("1")
        else:
            products_json = Properties.objects.filter(
                pr_id=request.POST["id"], pr_status="0"
            ).values()
            data = list(products_json)
            dictValue = data[0]

            Booking.objects.create(
                bk_seller_name=dictValue["pr_seller_name"],
                bk_seller_email=dictValue["pr_created_by"],
                bk_property_id=dictValue["pr_id"],
                bk_user_name=request.POST["txtName"],
                bk_user_email=request.session["web_email"],
                bk_user_address=request.POST["txtAddress"],
                bk_user_phone=request.POST["txtPhone"],
                bk_amount=request.POST["txtFees"],
                bk_status="Success",
                bk_created_by=dictValue["pr_created_by"],
            )

            try:
                send_mail(
                    "Booking Confirmation",
                    "Thank you for Booking Property, Please check my bookings for more information",
                    settings.EMAIL_HOST_USER,
                    [request.session["web_email"]],
                    fail_silently=True,
                )
            except Exception:
                pass  # Email sending is optional, don't block the booking

        return HttpResponse("success")
    else:
        return HttpResponse("signin")


def placeOrder(request):
    if "web_email" in request.session:
        Order.objects.create(
            or_name=request.POST["txtName"],
            or_date=request.POST["txtDate"],
            or_transaction_id=request.POST["transaction_id"],
            or_mobile=request.POST["txtPhone"],
            or_email=request.POST["txtEmail"],
            or_address=request.POST["txtAddress"],
            or_total_amount=request.POST["totalAmount"],
            or_user_email=request.session["web_email"],
            or_status="Success",
            or_created_by=request.session["web_email"]
        )

        latest_order = Order.objects.latest('or_id')
        orderID = latest_order.or_id

        jsonData = Cart.objects.filter(ct_user_email=request.session["web_email"]).values()
        data = list(jsonData)

        for dataValue in data:
            PurchasedProducts.objects.create(
                pp_or_id = orderID,
                pp_image = dataValue['ct_image'],
                pp_name = dataValue['ct_name'],
                pp_category = dataValue['ct_category'],
                pp_price = dataValue['ct_price'],
                pp_desc = dataValue['ct_desc'],
                pp_qty = dataValue['ct_qty'],
                pp_total_amount = dataValue['ct_total_amount'],
                pp_user_email = dataValue['ct_user_email'],
                pp_created_by = dataValue['ct_created_by'], # Link to the seller
            )

        try:
            send_mail(
                "Order Confirmation",
                "Thank you for Order, Please check my orders for more information",
                settings.EMAIL_HOST_USER,
                [request.session["web_email"]],
                fail_silently=True,
            )
        except Exception:
            pass  # Email sending is optional, don't block the order

        Cart.objects.filter(ct_user_email=request.session["web_email"]).delete()
        return HttpResponse("1")
    else:
        return HttpResponse("signin")

def addToCart(request):
    if "web_email" not in request.session:
        return HttpResponse("signin")

    jsonData = Products.objects.filter(pd_id=request.POST["id"]).values()
    data = list(jsonData)
    dictValue = data[0]
    
    # Sanitize price: remove symbol and comma
    clean_price = str(dictValue["pd_price"]).replace('₹', '').replace(',', '').strip()
    try:
        price_val = int(float(clean_price))
    except:
        price_val = 0
        
    totalAmount = int(request.POST["selQTY"]) * price_val
    
    Cart.objects.create(
        ct_image=dictValue["pd_image"],
        ct_name=dictValue["pd_name"],
        ct_category=dictValue["pd_category"],
        ct_price=dictValue["pd_price"],
        ct_desc=dictValue["pd_desc"],
        ct_qty=request.POST["selQTY"],
        ct_total_amount=totalAmount,
        ct_user_email=request.session["web_email"],
        ct_created_by=dictValue["pd_created_by"], # Store the seller email
    )

    return HttpResponse("1")


# ===== USER REGISTRATION & LOGIN =====

def userRegister(request):
    """Handle user registration"""
    if request.method == "POST":
        us_name = request.POST.get("txtName", "").strip()
        us_email = request.POST.get("txtEmail", "").strip()
        us_mobile = request.POST.get("txtMobile", "").strip()
        us_password = request.POST.get("txtPassword", "").strip()
        
        if not all([us_name, us_email, us_mobile, us_password]):
            return JsonResponse({"status": "error", "message": "All fields are required"})
        
        if Register.objects.filter(us_email=us_email).exists():
            return JsonResponse({"status": "error", "message": "Email already registered"})
        
        try:
            Register.objects.create(
                us_name=us_name,
                us_email=us_email,
                us_mobile=us_mobile,
                us_password=us_password,
                us_status=0,
                us_created_by="user"
            )
            
            send_mail(
                "Registration Successful",
                f"Welcome {us_name}! Your account has been created. Email: {us_email}",
                settings.EMAIL_HOST_USER,
                [us_email],
                fail_silently=True,
            )
            
            return JsonResponse({"status": "success", "message": "Registration successful! Please login."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    
    return render(request, "web/register.html")


def sellerRegisterPage(request):
    """Render the seller registration page"""
    return render(request, "web/seller_register.html")

def sellerRegister(request):
    """Handle seller registration"""
    if request.method == "POST":
        s_name = request.POST.get("txtName", "").strip()
        s_email = request.POST.get("txtEmail", "").strip()
        s_mobile = request.POST.get("txtMobile", "").strip()
        s_password = request.POST.get("txtPassword", "").strip()
        
        # Validate inputs
        if not all([s_name, s_email, s_mobile, s_password]):
            return JsonResponse({"status": "error", "message": "All fields are required"})
        
        # Check if email already exists in users or sellers
        if Register.objects.filter(us_email=s_email).exists() or AdminSeller.objects.filter(s_email=s_email).exists():
            return JsonResponse({"status": "error", "message": "Email already registered"})
        
        try:
            AdminSeller.objects.create(
                s_name=s_name,
                s_email=s_email,
                s_mobile=s_mobile,
                s_password=s_password,
                s_role="Seller",
                s_address="N/A",  # Default address
                s_status=0,
                s_created_by="Self"
            )
            return JsonResponse({"status": "success", "message": "Seller registered successfully! Please login."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def userLoginValidate(request):
    """Handle user login"""
    if request.method == "POST":
        us_email = request.POST.get("txtEmail", "").strip()
        us_password = request.POST.get("txtPassword", "").strip()
        
        if not us_email or not us_password:
            return JsonResponse({"status": "error", "message": "Email and password are required"})
        
        try:
            user = Register.objects.get(us_email=us_email, us_password=us_password)
            request.session["web_email"] = us_email
            request.session["web_name"] = user.us_name
            request.session["web_id"] = user.us_id
            return JsonResponse({"status": "success", "message": "Login successful", "redirect": "/"})
        except Register.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Invalid email or password"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    
    return render(request, "web/web_login.html")


def logoutWeb(request):
    """Handle user logout"""
    try:
        if "web_email" in request.session:
            del request.session["web_email"]
        if "web_name" in request.session:
            del request.session["web_name"]
        if "web_id" in request.session:
            del request.session["web_id"]
    except:
        pass
    return redirect("/")


def webOrder(request):
    """View user orders"""
    if "web_email" in request.session:
        return render(request, "web/my_orders.html")
    else:
        return redirect("/web_login/")



# Old duplicate userRegister removed - using the JSON-returning version above (line ~739)


def webForgotPassword(request):
    return render(request, "web/web_forgot_password.html")


def webUpdatePassword(request):
    return render(request, "web/web_update_password.html")


def checkEmail(request):
    if Register.objects.filter(
        us_email=request.POST["txtEmail"], us_status="0"
    ).count():
        request.session["forgot_email"] = request.POST["txtEmail"]
        request.session["forgot_role"] = "User"
        return HttpResponse("1")
    elif AdminSeller.objects.filter(
        s_email=request.POST["txtEmail"], s_status=0
    ).count():
        request.session["forgot_email"] = request.POST["txtEmail"]
        request.session["forgot_role"] = "Seller"
        return HttpResponse("1")
    else:
        return HttpResponse("10")


def updatePassword(request):
    role = request.session.get("forgot_role", "User")
    if role == "Seller":
        AdminSeller.objects.filter(s_email=request.session["forgot_email"]).update(
            s_password=request.POST["txtPassword"]
        )
        return HttpResponse("seller")
    else:
        Register.objects.filter(us_email=request.session["forgot_email"]).update(
            us_password=request.POST["txtPassword"]
        )
        return HttpResponse("1")


# Old duplicate userLoginValidate removed - using the JSON-returning version above (line ~778)


def bookingDetails(request):
    data = Booking.objects.filter(bk_created_by=request.session["email"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def bookingDetailsAdmin(request):
    data = Booking.objects.filter().values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def myBookings(request):
    data = Booking.objects.filter(
        bk_user_email=request.session["web_email"], bk_status="Success"
    ).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values

def myCart(request):
    data = Cart.objects.filter(
        ct_user_email=request.session["web_email"]
    ).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values

def myOrders(request):
    data = Order.objects.filter(or_user_email=request.session["web_email"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values

def myOrdersAdmin(request):
    data = Order.objects.filter().values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values

def viewProducts(request):
    try:
        data = PurchasedProducts.objects.filter(pp_or_id=request.POST["orderID"]).values()
        data = list(data)
        
        # Add seller name to each product
        for item in data:
            seller_info = AdminSeller.objects.filter(s_email=item["pp_created_by"]).first()
            if seller_info:
                item["seller_name"] = seller_info.s_name
            else:
                item["seller_name"] = item["pp_created_by"] # Fallback to email
                
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def my_bookings(request):
    return render(request, "web/my_bookings.html")


# else:
# return render(request, 'web/web_login');


def userProfile(request):
    if "web_email" in request.session:
        return render(request, "web/user_profile.html")
    else:
        return render(request, "web/web_login")


def cancelBooking(request):
    Properties.objects.filter(pr_id=request.POST["propertyID"]).update(pr_sold="NO")

    Booking.objects.filter(bk_id=request.POST["bookingID"]).update(
        bk_status="Cancelled"
    )

    return HttpResponse()

def removeCart(request):
    Cart.objects.filter(ct_id=request.POST["cartID"]).delete()
    return HttpResponse()


def userDetails(request):
    data = Register.objects.filter().values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


# ============= WEB-BASED SELLER PROFILE =============

def sellerWebProfile(request):
    """Web-based seller profile where sellers can manage their products"""
    if "email" not in request.session or request.session.get("role") != "Seller":
        return redirect("/admin_login/")
    return render(request, "web/seller_profile.html")


def sellerWebProducts(request):
    """Redirect to seller web profile"""
    return redirect("/seller_web_profile/")


def sellerWebProductsDetails(request):
    """Handle seller product operations from web interface"""
    try:
        if "email" not in request.session or request.session.get("role") != "Seller":
            return JsonResponse({"error": "Unauthorized"}, status=401)
        
        if request.POST["action"] == "add":
            Products.objects.create(
                pd_image=request.FILES.get("filePhoto", ""),
                pd_name=request.POST["txtName"],
                pd_category=request.POST["selCategory"],
                pd_price=request.POST["txtPrice"],
                pd_desc=request.POST["txtDesc"],
                pd_date=request.POST["txtDate"],
                pd_created_by=request.session["email"],
            )

        elif request.POST["action"] == "getData":
            data = Products.objects.filter(
                pd_created_by=request.session["email"], pd_status=0
            ).values()
            data = list(data)
            return JsonResponse(data, safe=False)

        elif request.POST["action"] == "update":
            data = Products.objects.filter(pd_id=request.POST["id"]).update(
                pd_name=request.POST["txtName1"],
                pd_category=request.POST["selCategory1"],
                pd_price=request.POST["txtPrice1"],
                pd_desc=request.POST["txtDesc1"],
                pd_date=request.POST["txtDate1"],
            )

        elif request.POST["action"] == "delete":
            data = Products.objects.filter(pd_id=request.POST["id"]).update(pd_status=1)

        return HttpResponse()
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
