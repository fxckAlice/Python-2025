from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self) -> None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def execute(self, sql: str, params: tuple | dict | None = None) -> int:
        ...

    @abstractmethod
    def executemany(self, sql: str, seq_of_params: list[tuple] | list[dict]) -> int:
        ...

    @abstractmethod
    def fetchone(self, sql: str, params: tuple | dict | None = None) -> tuple | None:
        ...

    @abstractmethod
    def fetchall(self, sql: str, params: tuple | dict | None = None) -> list[tuple]:
        ...

    @abstractmethod
    def is_connected(self) -> bool:
        ...
