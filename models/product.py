class Product:
    """ Класс продукта """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


    def check_quantity(self, quantity) -> bool:
        """
        Возвращает True, если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity and quantity >= 0


    def buy(self, quantity):
        """
         Метод покупки
            Проверяет количество продукта, используя метод check_quantity
            Если продуктов не хватает, то выбрасывает исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
            return quantity
        else:
            raise ValueError("Недостаточно продукта")


    def __hash__(self):
        return hash(self.name + self.description)

