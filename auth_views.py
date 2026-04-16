from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from app.models import Register, AdminSeller


def userRegister(request):
    """Handle user registration"""
    if request.method == "POST":
        us_name = request.POST.get("txtName", "").strip()
        us_email = request.POST.get("txtEmail", "").strip()
        us_mobile = request.POST.get("txtMobile", "").strip()
        us_password = request.POST.get("txtPassword", "").strip()
        
        # Validate inputs
        if not all([us_name, us_email, us_mobile, us_password]):
            return JsonResponse({"status": "error", "message": "All fields are required"})
        
        # Check if email already exists
        if Register.objects.filter(us_email=us_email).exists() or AdminSeller.objects.filter(s_email=us_email).exists():
            return JsonResponse({"status": "error", "message": "Email already registered"})
        
        try:
            # Create new user
            Register.objects.create(
                us_name=us_name,
                us_email=us_email,
                us_mobile=us_mobile,
                us_password=us_password,
                us_status=0,
                us_created_by="user"
            )
            
            # Send confirmation email (non-blocking)
            try:
                send_mail(
                    "Registration Successful",
                    f"Welcome {us_name}! Your account has been created successfully.\n\nEmail: {us_email}\n\nYou can now login to your account.",
                    settings.EMAIL_HOST_USER,
                    [us_email],
                    fail_silently=True,
                )
            except Exception:
                pass  # Email is optional, registration still succeeds
            
            return JsonResponse({"status": "success", "message": "Registration successful! Please login."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    
    return render(request, "web/register.html")


def userLoginValidate(request):
    """Handle user login"""
    if request.method == "POST":
        us_email = request.POST.get("txtEmail", "").strip()
        us_password = request.POST.get("txtPassword", "").strip()
        
        # Validate inputs
        if not us_email or not us_password:
            return JsonResponse({"status": "error", "message": "Email and password are required"})
        
        try:
            # Check if user exists
            user = Register.objects.get(us_email=us_email, us_password=us_password)
            
            # Set session
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
        del request.session["web_email"]
        del request.session["web_name"]
        del request.session["web_id"]
    except KeyError:
        pass
    
    return redirect("/")


def webOrder(request):
    """View user orders"""
    if "web_email" in request.session:
        return render(request, "web/my_orders.html")
    else:
        return redirect("/web_login/")
