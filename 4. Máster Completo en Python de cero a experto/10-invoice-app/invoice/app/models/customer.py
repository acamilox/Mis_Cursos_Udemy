class Customer:
    def __init__(self, name: str, last_name: str, tax_id: str):
        self.__name: str = name
        self.__last_name: str = last_name
        self.__tax_id: str = tax_id

    # Getters and Setters
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        self.__last_name = value

    @property
    def tax_id(self) -> str:
        return self.__tax_id