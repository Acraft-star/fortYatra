# 🏰 Fort Yatra - Fort Tourism And Booking System

<p align="center">
  <b>A Web-Based Tourism And Tour Package Booking System For Exploring The Historic Forts Of Maharashtra.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.0-darkgreen?logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/HTML5-orange?logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-blue?logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-yellow?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Bootstrap-purple?logo=bootstrap&logoColor=white" alt="Bootstrap">
</p>

---

## 📌 Project Overview

**Fort Yatra** is a web-based **Fort Tourism And Booking Management System** developed using Python and Django.

The main purpose of this project is to provide users with an easy platform to explore the historic forts of Maharashtra and book available tour packages online.

The system provides features such as user registration, OTP verification, secure login, tour package management, real-time seat tracking, package booking, booking history, login history, PDF booking tickets, and email confirmation.

This project focuses on providing a simple and user-friendly experience for both tourists and administrators.

---

## 🎯 Project Objectives

- Provide information about historical forts in Maharashtra.
- Allow users to explore available tour packages.
- Provide an online tour package booking system.
- Track available and booked seats.
- Provide secure user registration and OTP verification.
- Maintain booking history for users.
- Allow administrators to create and manage tour packages.
- Generate booking tickets in PDF format.
- Share booking confirmation and PDF tickets through email.

---

## 🚀 Key Features

### 👤 User Features

- User Registration
- OTP Verification
- Secure Login And Logout
- Password Hashing
- Browse Fort Information
- View Available Tour Packages
- Book Tour Packages
- Real-Time Seat Availability
- View Booking History
- View Login History
- Receive Booking Confirmation Through Email
- Receive Booking Ticket In PDF Format

### 🔐 Admin Features

- Admin Login
- Create Tour Packages
- Manage Tour Packages
- Update Package Information
- Manage Package Availability
- Monitor Bookings
- Manage Available Seats

### 📄 Booking Features

- Tour Package Selection
- Passenger Booking
- Seat Availability Tracking
- Booking Confirmation
- PDF Ticket Generation
- Email Confirmation
- Booking History

---

## 🏯 Fort Information

Fort Yatra provides information about historical forts of Maharashtra.

Users can explore forts and learn about their basic information before selecting a suitable tour package.

Some of the forts included in the project are:

- Rajgad Fort
- Historic Fort Locations
- Maharashtra Fort Tourism Information

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite | Database Management |
| HTML5 | Website Structure |
| CSS3 | Styling |
| JavaScript | Client-Side Functionality |
| Bootstrap | Responsive UI |
| xhtml2pdf | PDF Ticket Generation |
| Gmail SMTP | Email Notification |
| Git & GitHub | Version Control |

---

## 📂 Project Modules

The project is divided into the following main modules:

### 1. User Registration

Users can create an account by providing their required details.

### 2. OTP Verification

OTP verification is used during the registration process to verify the user's email address.

### 3. Login System

Registered users can securely log in and access the booking system.

### 4. Tour Packages

Users can view available tour packages along with package details.

### 5. Package Management

Administrators can create and manage tour packages.

### 6. Booking System

Users can select a tour package and complete the booking process.

### 7. Seat Tracking

The system tracks available and booked seats for tour packages.

### 8. Booking History

Users can view their previous bookings.

### 9. Login History

The system maintains login-related activity for users.

### 10. PDF Booking Ticket

After successful booking, a booking ticket is generated in PDF format.

### 11. Email Confirmation

Booking confirmation and the PDF ticket are shared with the user through email.

---

## 🔄 Booking Flow

```text
User Registration
       ↓
OTP Verification
       ↓
User Login
       ↓
Explore Forts
       ↓
View Tour Packages
       ↓
Select Package
       ↓
Check Seat Availability
       ↓
Confirm Booking
       ↓
Generate PDF Ticket
       ↓
Send Confirmation Email
       ↓
Booking Completed
📸 Screenshots
🏠 Home Page

Add your Home Page screenshot here.

![Home Page](screenshots/home.png)
🏯 Fort Information

Add your Fort Information screenshot here.

![Fort Information](screenshots/fort-information.png)
🎫 Tour Packages

Add your Tour Packages screenshot here.

![Tour Packages](screenshots/packages.png)
📝 Booking Page

Add your Booking Page screenshot here.

![Booking Page](screenshots/booking.png)
📄 Booking Confirmation

Add your Booking Confirmation screenshot here.

![Booking Confirmation](screenshots/booking-confirmation.png)
🌐 Live Demo

The live demo link will be added after deploying the project.

Live Demo: Coming Soon

💻 Run The Project Locally
Step 1: Clone The Repository
git clone https://github.com/Acraft-star/fortYatra.git
Step 2: Open The Project Folder
cd fortYatra
Step 3: Create A Virtual Environment
python -m venv venv
Step 4: Activate The Virtual Environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
Step 5: Install Required Packages
pip install -r requirements.txt
Step 6: Apply Database Migrations
python manage.py migrate
Step 7: Run The Development Server
python manage.py runserver
Step 8: Open The Website

Open the following URL in your browser:

http://127.0.0.1:8000/
📁 Project Structure
FortYatra/
│
├── fortYatra/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│
├── static/
│
├── media/
│
├── db.sqlite3
│
├── manage.py
│
├── requirements.txt
│
└── README.md
🗄️ Database

Fort Yatra uses SQLite as the database.

The database stores information related to:

Users
Tour Packages
Bookings
Seat Availability
Login History
OTP Verification
Other Application Data
📧 Email And PDF System

The project uses Gmail SMTP for sending email notifications.

After a successful booking:

Booking information is processed.
A booking ticket is generated in PDF format.
The PDF ticket is attached to the confirmation email.
The booking confirmation is shared with the user through email.

The PDF ticket is generated using xhtml2pdf.

🔒 Security Features
OTP-Based Email Verification
Password Hashing
Django Authentication
User Session Management
Protected Booking Process
Admin Access Control
🎓 Academic Project

Project Name: Fort Yatra - Fort Tourism And Booking System

Project Type: Academic / College Project

Company: Omkar Infotech

Partner: Sanket Shrikant Motewad

Technology: Python, Django, SQLite, HTML, CSS, JavaScript, Bootstrap

🔮 Future Scope

The project can be further improved by adding:

Online Payment Gateway
Google Maps Integration
More Maharashtra Forts
Tourist Reviews And Ratings
Advanced Admin Dashboard
Mobile Application
Cloud Database
Online Tour Guide Support
Real-Time Location Tracking
👨‍💻 Developer

Ashish Sanjay Shete

Bachelor Of Computer Applications (BCA)
Tilak Maharashtra Vidyapeeth, Pune

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
