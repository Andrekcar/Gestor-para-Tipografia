"""
Repositorio de clientes.

Encapsula todas las operaciones SQL sobre la tabla 'clientes'.
"""
from dataclasses import dataclass
from typing import Optional

from app.database.db import get_connection

@dataclass
class Cliente:
    nombre: str
    telefono: str = ""
    email: str = ""
    direccion: str = ""
    notas: str = ""
    id: Optional[int] = None


class ClienteRepository:

    def get_all(self) -> list[Cliente]:
        with get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM clientes ORDER BY nombre"
            ).fetchall()
        return [self._row_to_cliente(r) for r in rows]

    def get_by_id(self, cliente_id: int) -> Optional[Cliente]:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM clientes WHERE id = ?", (cliente_id,)
            ).fetchone()
        return self._row_to_cliente(row) if row else None

    def insert(self, cliente: Cliente) -> Cliente:
        sql = """
            INSERT INTO clientes (nombre, telefono, email, direccion, notas)
            VALUES (?, ?, ?, ?, ?)
        """
        with get_connection() as conn:
            cur = conn.execute(sql, (
                cliente.nombre, cliente.telefono, cliente.email,
                cliente.direccion, cliente.notas,
            ))
        cliente.id = cur.lastrowid
        return cliente

    def update(self, cliente: Cliente) -> None:
        sql = """
            UPDATE clientes
            SET nombre=?, telefono=?, email=?, direccion=?, notas=?
            WHERE id=?
        """
        with get_connection() as conn:
            conn.execute(sql, (
                cliente.nombre, cliente.telefono, cliente.email,
                cliente.direccion, cliente.notas,
                cliente.id,
            ))

    def delete(self, cliente_id: int) -> None:
        with get_connection() as conn:
            conn.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))

    @staticmethod
    def _row_to_cliente(row) -> Cliente:
        return Cliente(
            id=row["id"],
            nombre=row["nombre"],
            telefono=row["telefono"],
            email=row["email"],
            direccion=row["direccion"],
            notas=row["notas"],
        )
