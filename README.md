# Records Management System

## Overview
This project is a Records Management System designed for managing customer records. It provides functionality to add, delete, update, and view customer details. Initially, dummy data is used to populate the system.

## Features
- Add new customer records
- Delete existing customer records
- Update customer details
- View all customer records

## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
- Python 3.12 and above
- Django

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/my_username/records-management-system.git
Navigate into the project directory
sh
Copy code
cd records-management-system
Install dependencies
sh
Copy code
pip install -r requirements.txt
Setup
Apply migrations
sh
Copy code
python manage.py migrate
Create a superuser (optional but recommended)
sh
Copy code
python manage.py createsuperuser
Run the development server
sh
Copy code
python manage.py runserver
Access the application at http://127.0.0.1:8000/
Usage
Navigate to the admin interface at http://127.0.0.1:8000/admin/ to manage records.
Use the provided views and forms to add, delete, update, and view customer records.
Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request