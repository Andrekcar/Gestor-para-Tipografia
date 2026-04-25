"""
Conexion a la base de datos SQLite.

La base de datos se crea automaticamente si no existe.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "tipografia.db" # ubicación de la base de datos 

# Conexión 
def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# Inicializa la base de datos
def init_db():
    with get_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS clientes (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre      TEXT    NOT NULL,
                telefono    TEXT             DEFAULT '',
                email       TEXT             DEFAULT '',
                direccion   TEXT             DEFAULT '',
                notas       TEXT             DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS pedidos (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente         TEXT    NOT NULL DEFAULT '',
                tipo_trabajo    TEXT    NOT NULL DEFAULT '',
                descripcion     TEXT             DEFAULT '',
                estado          TEXT    NOT NULL DEFAULT 'No Iniciado',
                fecha_solicitud TEXT             DEFAULT (date('now')),
                fecha_entrega   TEXT             DEFAULT '',
                plantilla       TEXT             DEFAULT '',
                unidades        INTEGER          DEFAULT 1
            );
        """)

