# 🏘️ EstateHub - Property Management Project Overview

This document provides a comprehensive A-to-Z explanation of the **EstateHub** project to help you understand the architecture and explain it confidently to your teachers.

---

## 1. Project Introduction
**EstateHub** is a dynamic, full-stack property management and interior product marketplace. It serves as a bridge between **Sellers** (who list properties or furniture) and **Users** (who want to buy or rent them). 

### Key Stakeholders:
- **Sellers**: Can register, log in, and manage their own listings (Properties and Interior Products).
- **Users**: Can browse listings, view detailed info (including 360° views), and book properties.
- **Admin**: Has global control over users, categories, and all listings.

---

## 2. Technology Stack (The "How It Works")
- **Backend Framework**: Django (Python) - Handles all the logic, routing, and data processing.
- **Database**: SQLite3 - A lightweight, file-based SQL database that stores all project data.
- **Frontend**: HTML5, CSS3 (Bootstrap), and JavaScript (jQuery) - Provides the responsive UI.
- **Image Handling**: `Pillow` library for processing uploads.
- **Deployment**: Hosted live on **PythonAnywhere** via Git.

---

## 3. Core Features & "Wow" Factors
- **Dynamic Forms**: The "Add Property" form automatically adapts. If you select "Rent," the price field changes to "Monthly Rent."
- **360° Virtual Tours**: Properties feature a custom panoramic viewer allowing users to rotate images for a better view.
- **Dual Marketplace**: Not just properties, but also high-end "Interior Products" (Furniture/Decor).
- **Seller Dashboard**: A complete mini-system where sellers can track their orders and manage their inventory.
- **Role-Based Access**: Secure login systems for different types of users.

---

## 4. Technical Architecture (MVC Pattern)
Django uses the **Model-View-Template (MVT)** architecture:

- **Models (`models.py`)**: Defines the "Structure" of the data. 
    - *Example*: The `Property` model defines that every house must have a price, a city, and an image. 
- **Views (`views.py`)**: The "Brain" of the project. 
    - It fetches data from the database and sends it to the frontend.
- **Templates (`.html` files)**: The "Face" of the project. 
    - Uses Django Template Language to dynamically display data.
- **JavaScript (`jsProperties.js`, etc.)**: Handles real-time UI updates (like the Rent/Sell label toggle) without reloading the page.

---

## 5. Important Deployment Steps (The "Professional" Setup)
During development, we implemented several professional-grade solutions:
1. **Media Storage**: Configured `MEDIA_URL` and `MEDIA_ROOT` so that uploaded images are served from a dedicated folder, separate from static code.
2. **Migrations**: Used Django Migrations as "blueprints" to keep the database structure in sync between your computer and the server.
3. **Environment Security**: Handled secret keys and separate local/production environments carefully.

---

## 6. Sample Quiz/Viva Questions & Answers
**Q: Why did you use Django for this?**
*A: Django is a "batteries-included" framework that provides built-in security, an admin panel, and powerful database management, which speed up development.*

**Q: Where are the images stored?**
*A: Images are uploaded to the `media/` directory. The database stores the "path" (the filename), which the frontend uses to build a link to the actual image file.*

**Q: How do you handle different types of deals (Buy vs. Rent)?**
*A: We used custom JavaScript logic on the "Add Property" form to dynamically change labels, and we ensure the data is categorized in the database so the frontend can filter them.*

---

## 7. Conclusion
**EstateHub** is a production-ready application that demonstrates the use of dynamic data binding, professional path handling, and secure user authentication. It is fully hosted and accessible via a live URL.

---
*Created by Antigravity AI for EstateHub Project.*
