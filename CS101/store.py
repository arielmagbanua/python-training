import csv

path = 'D:\\Training\\python-training\\CS101\\'

def make_product_tuples(products_dir: str):
    products = []

    with open(products_dir, newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        next(reader)

        for product in reader:
            prod_tup = tuple(product)
            products.append(prod_tup)

    return products

def make_product_objects(products):
    pass

if __name__ == "__main__":
    make_product_tuples(path + 'products.csv')
