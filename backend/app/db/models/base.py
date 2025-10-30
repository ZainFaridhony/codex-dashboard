"""Base declarative model for the Codex Dashboard backend."""
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """Base class adding automatic table name generation."""

    @declared_attr.directive
    def __tablename__(cls) -> str:  # type: ignore[override]
        return cls.__name__.lower()
