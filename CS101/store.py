import csv

path = 'D:\\Training\\python-training\\CS101\\'

def make_product_tuples(products_dir: str):
    products = []

    with open(products_dir, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        next(reader)

        for product in reader:
            print(product)

if __name__ == "__main__":
    make_product_tuples(path + 'products.csv')
