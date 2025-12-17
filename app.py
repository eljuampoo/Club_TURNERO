from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "club_turnero_seguro"

# ---------------- CONEXIÓN ----------------
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",   # NO TOCAR
        database="club_turnero"
    )

# ---------------- INDEX ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        accion = request.form.get("accion")

        # REGISTRO
        if accion == "registro":
            nombre = request.form["nombre"]
            email = request.form["email"]
            password = request.form["password"]

            db = conectar_db()
            cur = db.cursor()
            cur.execute(
                "INSERT INTO usuarios (nombre, email, password) VALUES (%s,%s,%s)",
                (nombre, email, password)
            )
            db.commit()
            db.close()

            return redirect("/?registro=ok")

        # LOGIN
        if accion == "login":
            email = request.form["email"]
            password = request.form["password"]

            db = conectar_db()
            cur = db.cursor(dictionary=True)
            cur.execute(
                "SELECT * FROM usuarios WHERE email=%s AND password=%s",
                (email, password)
            )
            usuario = cur.fetchone()
            db.close()

            if usuario:
                session["id"] = usuario["id"]
                session["nombre"] = usuario["nombre"]
                return redirect("/turnos")

    return render_template("index.html")

# ---------------- TURNOS ----------------
@app.route("/turnos", methods=["GET", "POST"])
def turnos():
    if "id" not in session:
        return redirect("/")

    mensaje = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        jugadores = int(request.form["jugadores"])
        hora = request.form["hora"]
        fecha = request.form["fecha"]

        precio = 15000 if jugadores <= 10 else 20000

        db = conectar_db()
        cur = db.cursor(dictionary=True)

        # VERIFICAR SI YA EXISTE TURNO EN ESA FECHA Y HORA
        cur.execute("""
            SELECT * FROM turnos 
            WHERE fecha_turno=%s AND hora_turno=%s
        """, (fecha, hora))
        existe = cur.fetchone()

        if existe:
            mensaje = "ocupado"
        else:
            cur.execute("""
                INSERT INTO turnos
                (usuario_id, nombre_reserva, cantidad_jugadores, hora_turno, fecha_turno, precio)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (session["id"], nombre, jugadores, hora, fecha, precio))
            db.commit()
            mensaje = "ok"

        db.close()

    db = conectar_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM turnos WHERE usuario_id=%s", (session["id"],))
    lista = cur.fetchall()
    db.close()

    return render_template(
        "turnos.html",
        turnos=lista,
        nombre=session["nombre"],
        mensaje=mensaje
    )

# ---------------- CANCELAR TURNO ----------------
@app.route("/cancelar_turno/<int:id_turno>", methods=["POST"])
def cancelar_turno(id_turno):
    if "id" not in session:
        return redirect("/")

    db = conectar_db()
    cur = db.cursor()
    cur.execute(
        "DELETE FROM turnos WHERE id=%s AND usuario_id=%s",
        (id_turno, session["id"])
    )
    db.commit()
    db.close()

    return redirect("/turnos")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(debug=True)
