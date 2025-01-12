# Digital Products Management System

This repository contains a comprehensive Django-based backend project for managing digital products and user subscriptions. Developed with a focus on scalability and modularity, this project integrates several essential features for managing users, products, and payments.

---

## 📚 **Project Source Of Tutorial**

- **YouTube Tutorial**: [Vision Academy](https://www.youtube.com/watch?v=HQwPC5CkOG4&list=PL8oRZVu1TnSJdnbFLDoXKPkd_5gdaAu-z&index=11)
- **GitHub Repository**: [arashsa07/digital_products](https://github.com/arashsa07/digital_products)

---

## 🎯 **Features**

### User Management
- Add users along with their profiles, devices, and associated provinces.
- Secure token management with creation and refresh capabilities.

### Subscriptions
- Purchase time-based subscriptions with a user-friendly interface.
- Mock payment integration for testing payment flows.

### Database Management
- Import and export database entries directly from the admin panel using specialized packages.

### File Management
- Upload images and files to both product entries and user profiles.

---

## 🛠️ **Applications Overview**

### Products
- **Models**:
  - Category
  - Product

### Users (Custom Implementation)
- **Models**:
  - User
  - UserProfile
  - Device
  - Province

### Subscriptions
- Handle subscription models and related workflows.

### Payments
- Payment model and processing logic (includes mock payment functionality).

---

## 🚀 **Getting Started**

### Prerequisites
- Python 3.x
- Django
- Additional dependencies as listed in the `requirements.txt` file.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/arashsa07/digital_products.git
   ```

2. Navigate to the project directory:
   ```bash
   cd digital_products
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## 🔗 **Links**
- email : masoodyarab2@gmail.com
- [GitHub Repository](https://github.com/masoodhh)

---

## 📜 **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 **Acknowledgments**
Special thanks to Vision Academy for their excellent tutorials and guidance in building this project.

