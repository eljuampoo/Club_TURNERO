# ⚽ Club Turnero – Aplicación Web

Aplicación web desarrollada con **Flask y MySQL** que permite a los socios de un club de fútbol registrarse, iniciar sesión y gestionar la reserva de turnos de manera simple, ordenada y segura.

Este proyecto fue desarrollado como **tesina de 6° año**, aplicando conceptos de desarrollo web, bases de datos y operaciones CRUD.

---

## 📌 Tecnologías utilizadas

- Python 3  
- Flask  
- MySQL  
- HTML5  
- CSS3  
- JavaScript  
- XAMPP (MySQL + phpMyAdmin)

---

## ▶️ Cómo ejecutar la aplicación (Español)

### 1️⃣ Requisitos previos
- Tener Python 3 instalado  
- Tener XAMPP instalado  
- MySQL activo desde XAMPP  
- Navegador web  

---

### 2️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/club-turnero.git
cd club-turnero

### 3️⃣ Crear y activar entorno virtual (opcional)
python -m venv .venv
.\.venv\Scripts\activate

4️⃣ Instalar dependencias
pip install flask mysql-connector-python

5️⃣ Configuración de la base de datos

Abrir phpMyAdmin

Crear una base de datos llamada:

club_turnero


Importar o ejecutar el script SQL que crea las tablas:

usuarios

turnos

 ### 6️⃣ Configuración de conexión MySQL

En el archivo app.py, verificar los datos de conexión:

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
        database="club_turnero"
    )

7️⃣ Ejecutar la aplicación
python app.py


Abrir en el navegador:

http://127.0.0.1:5000

⚙️ Funcionalidades implementadas (CRUD)
👤 Usuarios

Crear usuario (Registro)

Leer usuario (Login)

Cerrar sesión

⚽ Turnos

Crear turno (Reserva)

Leer turnos reservados

Eliminar turno (Cancelar)

Validación de horarios duplicados

🧪 Pruebas de funcionalidades
✔ Registro

Presionar “Registrarse”

Completar el formulario

Verificar mensaje de registro exitoso

✔ Inicio de sesión

Presionar “Iniciar sesión”

Ingresar email y contraseña válidos

Acceder a la página de turnos

✔ Reserva de turnos

Completar el formulario

Confirmar turno

Verificar que aparece en la tabla

✔ Validación de horario ocupado

Reservar un turno

Intentar reservar el mismo horario

Aparece mensaje de error

✔ Cancelación de turno

Presionar “Cancelar”

Confirmar acción

El turno se elimina de la base de datos

⭐ Funcionalidades extra implementadas

Ventanas modales para login, registro y mensajes

Validación de turnos duplicados

Confirmación visual de acciones

Cancelación segura de turnos

Interfaz moderna con imagen de fondo

Manejo de sesiones de usuario

🌍 English Version
⚽ Club Turnero – Web Application

Web application developed using Flask and MySQL that allows football club members to register, log in, and manage field reservations in a simple and organized way.

This project was developed as a final school project, applying web development and database concepts.

📌 Technologies Used

Python 3

Flask

MySQL

HTML5

CSS3

JavaScript

XAMPP (MySQL + phpMyAdmin)

▶️ How to Run the Application (English)
1️⃣ Requirements

Python 3 installed

XAMPP installed

MySQL running

Web browser

2️⃣ Clone the repository
git clone https://github.com/your-username/club-turnero.git
cd club-turnero

3️⃣ Create and activate virtual environment (optional)
python -m venv .venv
.\.venv\Scripts\activate

4️⃣ Install dependencies
pip install flask mysql-connector-python

5️⃣ Database setup

Open phpMyAdmin

Create database:

club_turnero


Import SQL script to create tables

6️⃣ Database connection configuration

Check database credentials in app.py:

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
        database="club_turnero"
    )

7️⃣ Run the application
python app.py


Open in browser:

http://127.0.0.1:5000

⚙️ Implemented Features (CRUD)
👤 Users

Create user (Registration)

Read user (Login)

Logout

⚽ Reservations

Create reservation

Read reservations

Delete reservation

Duplicate schedule validation

🧪 Testing Instructions

Register a new user

Log in with valid credentials

Book a time slot

Try booking the same time slot again

Cancel a reservation

⭐ Extra Features

Modal-based interface

Reservation validation by date and time

Visual confirmations

Secure reservation cancellation

Modern responsive design
