from logger import logger


class Catalogue:
    def __init__(self):
        self.products = {}

    @logger
    def add_product(self, item_name: str, price: float):
        """
        This function take item_name and price as a input.add the item to the cataloge
        input: {item_name, price}
        """
        if price < 0:
            raise ValueError("Price can not be negative")
        self.products[item_name] = price
        return

    @logger
    def remove_product(self, item_name: str):
        if not self.products:
            print("Cataloge is empty")
            return

        self.products.pop(item_name, None)
        return

    @logger
    def view_products(self):
        if not self.products:
            print("Cataloge is empty")
            return
        for item, price in self.products.items():
            print(item, " : ", price)
        print("-"*20)
        print(f"total : {self.total_cost}")
        return

    @logger
    def search_product(self, item_name):
        if item_name in self.products:
            print("item found ", item_name, ":", self.products[item_name])
            print("-"*20)
        else:
            print(f"{item_name} not found")

    @property
    def total_cost(self):
        return sum(self.products.values())


def main():
    ItemList = Catalogue()
    ItemList.add_product('laptop', 55000.00)
    ItemList.add_product('mouse', 500.00)

    ItemList.view_products()
    print("-"*20)
    ItemList.search_product('mouse')

    print(f"Total is {ItemList.total_cost}")


if __name__ == "__main__":
    main()
