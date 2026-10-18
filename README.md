# Account Management System (Django)

A student project for tracking personal income and expenses. This is **not** a real banking system and does not connect to bank accounts or process payments.

## Features
- User registration, login and logout
- Private dashboard for each signed-in user
- Add income and expense transactions
- View transaction history
- Automatically calculated income, expenses and current balance
- SQLite database (created by Django migrations)
- Django CSRF protection and authentication

## Technology
- Python 3
- Django
- SQLite
- HTML and CSS

## Run locally
1. Install Python 3.10 or newer.
2. Extract the project ZIP and open a terminal in the extracted `account_management_django` folder.
3. Create and activate a virtual environment:
   - Windows: `py -m venv venv` then `venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create database tables: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`
7. Open `http://127.0.0.1:8000/` in your browser.
8. Register a new account.

## Upload to GitHub
1. Create a new **public** GitHub repository named `account-management-system` (or choose private if required).
2. Extract this ZIP, open a terminal in the project folder, and run:
   ```bash
   git init
   git add .
   git commit -m "Initial Django Account Management System"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/account-management-system.git
   git push -u origin main
   ```
3. Replace `YOUR-USERNAME` with your GitHub username.
4. Submit the repository URL in Google Classroom. Do not submit a made-up link.

## Project description for submission
**Title:** Account Management System using Django

**Description:** The Account Management System is a web application developed using Python and the Django framework. It helps a registered user maintain a simple record of personal income and expenses. Users can register and log in securely, add income or expense entries with a description, amount and date, and view a transaction history. The dashboard summarizes total income, total expenses and the calculated balance. Each user can access only their own transaction records.

**Objective:** To develop a simple, user-friendly web application that demonstrates Django authentication, database models, forms, CRUD operations and summary reporting.

**Modules:** User Authentication, Dashboard, Transaction Management, Transaction History and Balance Summary.

**Database:** SQLite.

**Note:** This educational project is not intended for real banking, storing bank credentials, or processing real payments.
