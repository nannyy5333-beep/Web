
"""
dbx.py — единый адаптер БД для Web и Bot (Postgres через SQLAlchemy).
Оставляйте в SQL знаки вопроса '?', адаптер сам преобразует их в именованные параметры для Postgres.
"""
from __future__ import annotations
import os
from typing import Any, Iterable, Dict, List, Tuple
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL не задан. Создай переменную окружения в Render для Web и Bot "
        "(возьми значение из Internal Database URL)."
    )

# Подходит для Render (автопереподключение, future API)
engine: Engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)

def _qmark_to_named(sql: str, params: Iterable[Any] | None) -> Tuple[str, Dict[str, Any]]:
    """
    Преобразует плейсхолдеры '?' в именованные :p0, :p1, ...
    """
    if not params:
        return sql, {}
    if isinstance(params, dict):
        # Уже именованные параметры — оставляем как есть
        return sql, params  # type: ignore[return-value]
    named: Dict[str, Any] = {}
    out: list[str] = []
    i = 0
    for ch in sql:
        if ch == '?':
            key = f"p{i}"
            out.append(f":{key}")
            i += 1
        else:
            out.append(ch)
    for j, v in enumerate(params):  # type: ignore[arg-type]
        named[f"p{j}"] = v
    return ''.join(out), named

def run(sql: str, params: Iterable[Any] | Dict[str, Any] | None = None) -> None:
    sql, bind = _qmark_to_named(sql, params)
    with engine.begin() as con:
        con.execute(text(sql), bind)

def all(sql: str, params: Iterable[Any] | Dict[str, Any] | None = None) -> List[Dict[str, Any]]:
    sql, bind = _qmark_to_named(sql, params)
    with engine.begin() as con:
        res = con.execute(text(sql), bind)
        return [dict(r._mapping) for r in res.fetchall()]

def one(sql: str, params: Iterable[Any] | Dict[str, Any] | None = None) -> Dict[str, Any] | None:
    rows = all(sql, params)
    return rows[0] if rows else None

def scalar(sql: str, params: Iterable[Any] | Dict[str, Any] | None = None) -> Any:
    sql, bind = _qmark_to_named(sql, params)
    with engine.begin() as con:
        return con.execute(text(sql), bind).scalar()

def executemany(sql: str, seq_params: Iterable[Iterable[Any]]) -> None:
    """
    Упрощённая версия executemany для одного SQL.
    """
    with engine.begin() as con:
        for params in seq_params:
            q, bind = _qmark_to_named(sql, params)
            con.execute(text(q), bind)

def healthcheck() -> bool:
    try:
        return scalar("SELECT 1") == 1
    except Exception:
        return False
