# Authentication System Backend

This project serves as the backend component of a secure authentication system built with Django and Django REST Framework. It is designed to integrate seamlessly with a React frontend while implementing robust security measures to withstand common web vulnerabilities.

## Project Purpose

Developed for educational and practical security research, this project focuses on building a full-stack authentication architecture and evaluating its resilience against cyber threats such as brute-force attacks, unauthorized data access, and credential compromise.

## Key Security Features

- Custom User Model using unique email addresses instead of standard usernames.
- Secure password hashing using Argon2.
- JWT-based authentication using HTTP-only, Secure, and SameSite cookies to protect tokens from XSS and CSRF attacks.
- Brute-force protection via Axes middleware to monitor and restrict repeated failed login attempts.
- Obfuscated administrative access paths to prevent automated directory scanning.
- Environment-based configuration management for sensitive credentials.

## Tech Stack

- Framework: Django / Django REST Framework
- Authentication: djangorestframework-simplejwt (Cookie-based)
- Security & Utilities: django-axes, argon2-cffi, python-dotenv
- Database: SQLite (Development)
