class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        products_list = data.split('\n')
        return products_list

    def add(self, *products):
        existing_products = self.get_products()
        open_file = open(self.__file_name, 'a')
        for product_ in products:
            product_str = f'{product_.name}, {product_.weight}, {product_.category}'
            if product_str not in existing_products:
                open_file.write(f'{product_str}')
            else:
                print(f'Продукт {product_} уже есть в магазине')
        open_file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())