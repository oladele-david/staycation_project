# STAYCATION

STAYCATION is an online platform that allows users to search for and book hotel rooms. This application is built using Flask, a lightweight web framework for Python. The backend leverages SQLAlchemy for ORM (Object Relational Mapping) and Flask-Migrate for handling database migrations. The platform allows users to register, search for hotels, and make bookings. Administrators can manage hotel listings, rooms, and bookings.

## Table of Contents
- [Features](#features)
- [Context](#context)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Database Migrations](#database-migrations)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
- [Development Checklist](#development-checklist)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **User Authentication**: Sign-up, login, and logout functionality.
- **Hotel Listings**: Users can browse and search for hotels.
- **Room Booking**: Users can book rooms in hotels.
- **Admin Panel**: Manage hotel listings, rooms, and bookings.
- **Responsive Design**: Future improvement to build a user-friendly frontend.
- **Search Functionality**: Search for hotels and rooms based on various criteria.

---

## Context
STAYCATION aims to simplify the process of searching for and booking hotel rooms. This project is suitable for learning about web development, specifically using the Flask framework, SQLAlchemy ORM, and handling database migrations with Flask-Migrate. It also provides a foundation for adding more advanced features, such as payment integration, real-time updates, and user reviews.

### Technologies Used
- **Flask**: Python web framework.
- **SQLAlchemy**: ORM for database interactions.
- **Flask-Migrate**: Database migrations.
- **PyMySQL**: MySQL database connector.
- **unittest**: Testing framework.
- **HTML/CSS/JavaScript**: Frontend development.

---

## Project Structure

```plaintext
your_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── hotel.py
│   │   ├── room.py
│   │   ├── user.py
│   │   ├── booking.py
│   │   ├── facility.py
│   │   └── rule.py
│   └── routes/
│       ├── __init__.py
│       ├── hotel_routes.py
│       ├── main.py
│       └── user_routes.py
├── migrations/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── test_config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── test_user_model.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── test_main_routes.py
│   │   ├── test_user_routes.py
│   │   └── test_hotel_routes.py
├── static/
│   ├── css/
│   ├── img/
│   ├── js/
├── templates/
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

---

## Setup and Installation

### Prerequisites
- Python 3.10+
- Virtualenv (optional but recommended)
- MySQL Database Server

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/oladele-david/staycation_project.git
   cd staycation
   ```

2. **Create and Activate a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root of the project and add the necessary environment variables:
   ```plaintext
   SECRET_KEY=your_secret_key
   DATABASE_URL=mysql+pymysql://db_username:db_password@db_host:db_port/db_name
   ```

5. **Initialize the Database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

---

## Environment Variables

- `SECRET_KEY`: A secret key for the Flask application.
- `DATABASE_URL`: The database connection URL.

---

## Database Migrations

Use Flask-Migrate for handling database migrations. Here are some common commands:

- **Initialize the Migration Repository**:
  ```bash
  flask db init
  ```

- **Create a New Migration**:
  ```bash
  flask db migrate -m "Description of migration"
  ```

- **Apply the Migration**:
  ```bash
  flask db upgrade
  ```

- **Downgrade the Migration**:
  ```bash
  flask db downgrade
  ```

---

## Running the Application

To run the application locally:
```bash
flask run
```
Visit `http://127.0.0.1:5000` same as `http://localhost:5000` to see the application in action.

---

## Running Tests

Use `unittest` to run the test suite:
```bash
python -m unittest discover -s tests
```

### Example for running a specific test file:

```bash
python -m unittest tests/models/test_user_model.py
```

Make sure to check for correct environment variables and configurations before running tests.

---

## API Endpoints

### User Routes
- `GET /users/`: List of users
- `POST /users/`: Creates a new user (registration)
- `POST /users/login`: Log in a user
- `POST /users/logout`: Log out a user

### Hotel Routes
- `GET /hotels/`: List of hotels
- `POST /hotels/`: Creates a new hotel (admin only)

### Main Routes
- `GET /`: Main route

### Authentication Routes
- `POST /auth/login`: Log in a user
- `POST /auth/register`: Register a new user

---

## Development Checklist

### Initial Setup
- [x] Flask application structure
- [x] SQLAlchemy setup
- [x] Flask-Migrate setup
- [x] Environment configuration

### Authentication
- [x] User model and password hashing
- [x] User registration route
- [x] User login route
- [ ] User session management
- [ ] Role-based access control

### Hotel Management
- [x] Hotel model
- [ ] Hotel listing route
- [ ] Hotel details route
- [ ] Admin route for creating hotels
- [ ] Admin route for managing hotels

### Room Booking
- [x] Room model
- [ ] Room availability check
- [ ] Room booking route
- [ ] Booking management
- [ ] Booking confirmation emails

### Search Functionality
- [ ] Search hotels by location and amenities
- [ ] Filter results by price, rating, etc.
- [ ] Search optimization

### Testing
- [x] Basic test framework setup
- [x] Configuration tests
- [x] User model tests
- [ ] Hotel model tests
- [ ] Route tests
- [ ] Integration tests
- [ ] Mock external services for testing

### Frontend Integration
- [ ] Basic HTML templates
- [ ] CSS for styling
- [ ] JavaScript for interactivity
- [ ] Responsive design principles

### Deployment
- [ ] Dockerfile for containerization
- [ ] Deployment scripts for cloud providers
- [ ] Continuous Integration setup
- [ ] Monitoring and logging

---

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

Please ensure your code follows the PEP 8 standards and includes appropriate docstrings.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## AUTHORS

This project is a collective effort by amazing developers who are passionate about building web applications. See the `AUTHORS` file for more details.

---


This README serves as a detailed guide for the STAYCATION project, providing essential information for setting up, running, and contributing to the application. As the project evolves, the README should be updated with new features, improvements, and additional documentation.