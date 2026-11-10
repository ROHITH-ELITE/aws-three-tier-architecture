from flask import Flask, jsonify, request
from dotenv import load_dotenv
import pymysql
import os

load_dotenv()

app = Flask("app")


def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        connect_timeout=5
    )


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to our AWS 3-Tier Architecture Project!",
        "server": "Application Server",
        "status": "Running Successfully"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/db-test")
def db_test():
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
        return jsonify({
            "database": "Connected Successfully",
            "mysql_version": version[0]
        })
    except Exception:
        app.logger.exception("Database connection failed")
        return jsonify({"database": "Connection Failed"}), 500
    finally:
        if connection:
            connection.close()


@app.route("/visitors", methods=["POST"])
def add_visitor():
    data = request.get_json(silent=True) or {}
    name = data.get("visitor_name", "").strip()

    if not name:
        return jsonify({"error": "visitor_name is required"}), 400

    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO visitors (visitor_name) VALUES (%s)",
                (name,)
            )
            visitor_id = cursor.lastrowid
        connection.commit()

        return jsonify({
            "message": "Visitor added successfully",
            "id": visitor_id,
            "visitor_name": name
        }), 201

    except Exception:
        app.logger.exception("Could not add visitor")
        return jsonify({"error": "Database operation failed"}), 500
    finally:
        if connection:
            connection.close()


@app.route("/visitors", methods=["GET"])
def get_visitors():
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, visitor_name, visited_at FROM visitors ORDER BY id DESC"
            )
            rows = cursor.fetchall()

        visitors = [
            {
                "id": row[0],
                "visitor_name": row[1],
                "visited_at": row[2].isoformat()
            }
            for row in rows
        ]

        return jsonify({"visitors": visitors})

    except Exception:
        app.logger.exception("Could not retrieve visitors")
        return jsonify({"error": "Database operation failed"}), 500
    finally:
        if connection:
            connection.close()
