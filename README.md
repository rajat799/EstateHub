# 🏘️ EstateHub - Real Estate & Interior Marketplace

![Django](https://img.shields.io/badge/Django-3.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

**EstateHub** is a full-stack, dual-sided marketplace that bridges the gap between property management and interior design. Built with Django, it provides a secure platform for Sellers to list real estate and furniture, and for Users to book properties or purchase products.

## ✨ Key Features

### 🏢 Dual Marketplace
* **Real Estate Management:** Browse, filter, and book apartments, villas, offices, and shops. Includes dynamic rent/sell pricing.
* **Interior Products:** A built-in e-commerce store with cart functionality to purchase furniture and home decor.

### 👥 Strict Role-Based Access Control (RBAC)
* **Admin Dashboard:** Total system oversight. Manage all users, sellers, properties, and track every transaction on the platform.
* **Seller Dashboard:** A dedicated portal for vendors to upload listings, manage their inventory, and fulfill specific orders made for their products.
* **User Portal:** A seamless frontend experience for buyers to browse listings, add to cart, and checkout.

### 🛡️ Enterprise-Grade Security
* **Session Fixation Protection:** Session keys are dynamically cycled upon login.
* **Atomic Transactions:** E-commerce checkouts are wrapped in database transactions to prevent partial orders and data corruption during server faults.
* **IDOR Prevention:** Strict ownership verification prevents users from modifying or deleting data that doesn't belong to them.
* **Password Hashing:** All passwords are cryptographically hashed using PBKDF2 SHA256.
* **Environment Variables:** Secrets are stripped from the codebase and loaded via `.env` files.

---

## 🏗️ Technical Architecture
EstateHub utilizes the **Model-View-Template (MVT)** architecture pattern:
- **Backend:** Django (Python)
- **Database:** SQLite3 (Configured for easy local setup)
- **Frontend:** HTML5, CSS3, JavaScript, jQuery, Bootstrap
- **Image Processing:** Python `Pillow` library

---

## 🚀 Local Installation & Setup

Want to run EstateHub on your local machine? Follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/rajat799/EstateHub.git
cd EstateHub
```

### 2. Set up the Environment Variables
Copy the template environment file:
```bash
cp .env.example .env
```
Open `.env` and add a generated secret key.

### 3. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser!

---

## 🌐 Live Deployment
This project is deployment-ready and configured for hosting on platforms like **PythonAnywhere**. Static files and media roots are pre-configured in `settings.py`.

---
*Created for a college final project presentation.*
