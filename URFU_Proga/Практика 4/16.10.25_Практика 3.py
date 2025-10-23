class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

class Order:
    def __init__(self, items):
        self.items = items
        self.taxes = 0.2 
        self.discount = 0.15
    
    def calculate_total(self):
        total = []
        for item in self.items:
            price = item.price + item.price * self.taxes
            price = price - price * self.discount
            total.append(price)
        return total

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def add_order(self, order):
        self.orders.append(order)

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'Товар "{item.name}" отсутствует в корзине')


product1 = Product("Телефон", 10000, 5, "Электроника")
product2 = Product("Книга", 500, 10, "Литература")
product3 = Product("Нига", 0, 0, "Окак")

cart = ShoppingCart()
cart.add_item(product1)
cart.add_item(product2)
print(f"В корзине: {[item.name for item in cart.items]}")

cart.remove_item(product1)
print(f"После удаления: {[item.name for item in cart.items]}")

cart.remove_item(product3)

order = Order(cart.items)
print(f"Сумма заказа: {order.calculate_total()} руб.")

customer = Customer("Иван")
customer.add_order(order)
print(f"У клиента {customer.name} заказов: {len(customer.orders)}")
