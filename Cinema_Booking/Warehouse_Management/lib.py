class Prodotto:
    def __init__(self, name: str, quantity: str) -> None:
        self.name = name
        self.quantity = quantity

class Magazzino:
    def __init__(self) -> None:
        self.products: list[Prodotto] = []

    def add_product(self, new_product: Prodotto) -> None:
        self.products.append(new_product)
        print(f"Succesfully added product {new_product.name} to current warehouse")

    def find_product(self, product_name: str) -> Prodotto:
        for product in self.products:
            if product.name == product_name:
                return product

    def check_availability(self, product_name: str) -> str:
        found_product: Prodotto = self.find_product(product_name)
        if found_product:
            if found_product.quantity > 0:
                return f"Product {product_name} is aviable, {found_product.quantity} unit left"
            else:
                return f"Product {product_name} is not aviable"
        else:
            return f"Product {product_name} not found in current warehouse"
    


# Tests
def main():

    print() # Formatting

    # Creating some products
    product1 = Prodotto("Lamp", 10)
    product2 = Prodotto("Chair", 5)
    product3 = Prodotto("Pillow", 0)

    # Creating a warehouse
    warehouse = Magazzino()

    # Adding products to the warehouse
    warehouse.add_product(product1)
    warehouse.add_product(product2)
    warehouse.add_product(product3)

    print() # Formatting

    # Checking availability of some products
    print(warehouse.check_availability("Lamp"))
    print(warehouse.check_availability("Table"))
    print(warehouse.check_availability("Pillow"))

    # Finding a product
    warehouse.find_product("Chair")

if __name__ == "__main__":
    main()