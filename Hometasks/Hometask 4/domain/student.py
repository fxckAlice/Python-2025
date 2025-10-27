class Student:
    def __init__(self, full_name: str, group_number: str, birth_date: str | None = None, address: str | None = None):
        self._full_name = full_name
        self._group_number = group_number
        self._birth_date = birth_date
        self._address = address

    def get_full_name(self) -> str:
        return self._full_name

    def set_full_name(self, value: str) -> None:
        self._full_name = value

    def get_group_number(self) -> str:
        return self._group_number

    def set_group_number(self, value: str) -> None:
        self._group_number = value

    def get_birth_date(self) -> str | None:
        return self._birth_date

    def set_birth_date(self, value: str | None) -> None:
        self._birth_date = value

    def get_address(self) -> str | None:
        return self._address

    def set_address(self, value: str | None) -> None:
        self._address = value
