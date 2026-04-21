"""
Repositorio para pedidos.

Encapsula todas las operaciones SQL sobre la tabla 'pedidos'.
La vista nunca toca SQL directamente — solo llama metodos de esta clase.
"""
from dataclasses import dataclass # para @dataclass, que nos ahorra escribir __init__ y otros métodos comunes
from typing import Optional # para indicar que el campo id puede ser int o None (antes de guardar en BD)
from app.database.db import get_connection # para obtener una conexión a la base de datos y ejecutar consultas SQL

@dataclass # convierte la clase en un contenedor de datos con constructor automático, etc.
class Pedido:
    cliente: str
    tipo_trabajo: str = ""
    descripcion: str = ""
    estado: str = "No Iniciado"
    fecha_solicitud: str = ""
    fecha_entrega: str = ""
    plantilla: str = ""
    id: Optional[int] = None   # None mientras no esta guardado en BD

class PedidoRepository:
    def get_all(self) -> list[Pedido]:
        """Devuelve todos los pedidos ordenados por id."""
        with get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM pedidos ORDER BY id"
            ).fetchall() # 
        return [self._row_to_pedido(r) for r in rows] 

    def get_by_id(self, pedido_id: int) -> Optional[Pedido]: #
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM pedidos WHERE id = ?", (pedido_id,)
            ).fetchone() # fetchone devuelve una fila o None si no encuentra nada
        return self._row_to_pedido(row) if row else None

    def insert(self, pedido: Pedido) -> Pedido:
        """Inserta un pedido nuevo y devuelve el mismo objeto con su id asignado."""
        sql = """
            INSERT INTO pedidos
                (cliente, tipo_trabajo, descripcion, estado,
                 fecha_solicitud, fecha_entrega, plantilla)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        with get_connection() as conn:
            cur = conn.execute(sql, (
                pedido.cliente, pedido.tipo_trabajo, pedido.descripcion,
                pedido.estado, pedido.fecha_solicitud,
                pedido.fecha_entrega, pedido.plantilla,
            ))
        pedido.id = cur.lastrowid # asigna el id generado por la BD al objeto Pedido
        return pedido

    def update(self, pedido: Pedido):
        """Actualiza un pedido existente (requiere pedido.id)."""
        sql = """
            UPDATE pedidos
            SET cliente=?, tipo_trabajo=?, descripcion=?, estado=?,
                fecha_solicitud=?, fecha_entrega=?, plantilla=?
            WHERE id=?
        """
        with get_connection() as conn:
            conn.execute(sql, (
                pedido.cliente, pedido.tipo_trabajo, pedido.descripcion,
                pedido.estado, pedido.fecha_solicitud,
                pedido.fecha_entrega, pedido.plantilla,
                pedido.id,
            ))

    def delete(self, pedido_id: int):
        with get_connection() as conn:
            conn.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,)) #

    # ------------------------------------------------------------------
    # Privado
    # ------------------------------------------------------------------

    @staticmethod #
    def _row_to_pedido(row: object) -> Pedido: # 
        return Pedido(
            id=row["id"],
            cliente=row["cliente"],
            tipo_trabajo=row["tipo_trabajo"],
            descripcion=row["descripcion"],
            estado=row["estado"],
            fecha_solicitud=row["fecha_solicitud"],
            fecha_entrega=row["fecha_entrega"],
            plantilla=row["plantilla"],
        )
