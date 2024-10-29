# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147


class Product:
    def __init__(self, name: str, price: float, weight: float = 1.0):
        self.name = name
        self.price = price
        self.weight = weight

    def apply_discount(self, percent: float) -> float:
        self.price = self.price * (1 - percent / 100)
        return self.price

    def __str__(self) -> str:
        if self is None:
            return ""
        return f"Product: {self.name}, Price: ${self.price}, Weight: {self.weight}kg"

    def __eq__(self, other) -> bool:
        if other is None or isinstance(other, str) or not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price and self.weight == other.weight

    def __iadd__(self, other) -> "Product":
        if other is None or isinstance(other, str) or not isinstance(other, Product):
            return self
        if self.name == other.name:
            self.weight += other.weight
            self.price = max(self.price, other.price)
        return self


class FragileProduct(Product):
    def __init__(self, name: str, price: float, weight: float = 1.0, _fragility_level: float = 0):
        super().__init__(name, price, weight)
        self._fragility_level = _fragility_level

    @property
    def fragility_level(self):
        return self._fragility_level

    @fragility_level.setter
    def fragility_level(self, level: int | float):
        self._fragility_level = max(1, min(5, level))

    def apply_discount(self, percent: float) -> float:
        self.price = self.price * (1 - min(percent, 10) / 100)
        return self.price

    def __str__(self):
        if self is None:
            return ""
        return super().__str__() + f", Fragility Level: {self._fragility_level}"


class Order:
    def __init__(self):
        self.products = []

    def calculate_total(self):
        sum = 0
        total_weight = 0
        for product in self.products:
            sum += product.price
            total_weight += product.weight / 2
            if isinstance(product, FragileProduct):
                sum += 5
            if product.get_fragility_level() > 5:
                sum += 5
        return sum + (total_weight / 2)

    def add_product(self, obj):
        if obj is None or isinstance(obj, str) or not isinstance(obj, Product):
            return False
        if self.calculate_total() + obj.price + obj.weight / 2 <= 1400:
            self.products.append(obj)
            return True

    def view_order(self):
        if not self.products:
            print("Empty order.")
        else:
            for product in range(0, len(self.products), 1):
                print(str(product).join(';'))
            print(self.products[-1])
