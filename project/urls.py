"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Web
    path("", views.webIndex),
    path("index/", views.webIndex),
    path("about/", views.webAbout),
    path("contact/", views.webContact),
    path("property/", views.webProperty),
    path("propertylist/", views.webPropertylist),
    path("productlist/", views.webProductlist),

    path("propertytype/", views.webPropertytype),
    path("testimonial/", views.webTestimonial),
    path("check_admin_login/", views.checkAdminLogin, name="login"),
    path("admin_login/", views.openLogin, name="login"),
    path("logout/", views.logout, name="login"),
    path("logout_web/", views.logoutWeb, name="login"),
    path("web_forgot_password/", views.webForgotPassword, name="web_forgot_password"),
    path("web_update_password/", views.webUpdatePassword, name="web_forgot_password"),
    path("user_check_email/", views.checkEmail, name="user_check_email"),
    path("update_password/", views.updatePassword, name="update_password"),
    path("booking/", views.adminBooking),
    path("admin/", views.adminAdmin),
    path("pilot/", views.adminPilot),
    path("profile/", views.adminProfile),
    path("properties/", views.adminProperties),
    path("products/", views.adminProducts),
    path("orders/", views.adminOrders),

    path("seller/", views.adminSeller),
    # path('get_bookings/', views.getBookings),
    path("user_profile/", views.userProfile),
    path("user_profile_details/", views.userProfileDetails),
    path("update_user_profile_details/", views.userUpdateProfileDetails),
    # Admin Backend
    path("admin_details/", views.adminDetails),
    path("admin_seller/", views.adminSellerDetails),
    path("web_get_profile/", views.getWebProfile),
    # Seller
    path("seller_booking/", views.sellerPurchaser),
    path("category/", views.category),
    path("category_details/", views.categoryDetails),
    path("web_category/", views.webCategory),
    path("propertiess/", views.sellerPropertiess),
    path("seller_products/", views.sellerProducts),
    # Seller backend
    path("seller_properties/", views.sellerPropertiesDetails),
    path("seller_products_details/", views.sellerProductsDetails),
    path("seller_product_orders/", views.sellerViewOrderDetails),
    path("product_details/", views.adminProductDetails),

    path("admin_properties/", views.adminPropertiesDetails),
    path("web_seller_properties/", views.webSellerProperties),
    path("web_seller_products/", views.webSellerProducts),

    path("get_web_search_properties/", views.getWebSearchProperties),
    path("get_web_search_products/", views.getWebSearchProducts),

    path("web_place/", views.getWebPlaces),
    path("profile_details/", views.profileDetails),
    path("single_property/", views.openSingleProperty),
    path("single_product/", views.openSingleProduct),

    path("get_single_item/", views.getSingleItem),
    path("get_single_product_item/", views.getSingleProductItem),

    path("book_property/", views.bookProperty),
    path("place_order/", views.placeOrder),
    path("my_orders/", views.webOrder),
    path("add_to_cart/", views.addToCart),
    path("cart/", views.cart),
    path("checkout/", views.checkout),
    path("register/", views.webRegister),
    path("seller_register_page/", views.sellerRegisterPage),
    path("seller_register/", views.sellerRegister),
    path("web_login/", views.webLogin),
    path("user_register/", views.userRegister),
    path("user_login_validate/", views.userLoginValidate),
    path("booking_details/", views.bookingDetails),
    path("booking_details_admin/", views.bookingDetailsAdmin),
    path("my_bookings/", views.my_bookings),
    path("my_bookings_list/", views.myBookings),
    path("my_cart_list/", views.myCart),
    path("my_order_list/", views.myOrders),
    path("orders_details_admin/", views.myOrdersAdmin),
    path("view_products/", views.viewProducts),
    path("cancel_booking/", views.cancelBooking),
    path("property_types/", views.propertyTypes),
    path("latest_properties/", views.latestProperties),
    path("remove_cart/", views.removeCart),
     path("user/", views.user),
    path("faq/", views.faq),
    path("help/", views.help),
    path("seller_web_profile/", views.sellerWebProfile),
    path("seller_web_products/", views.sellerWebProducts),
    path("seller_web_products_details/", views.sellerWebProductsDetails),
    path("user_details/", views.userDetails),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
