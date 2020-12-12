import csv

path = 'D:\\Training\\python-training\\CS101\\products.csv'

# Read the products.csv and extract each product, creating tuple for each product, and put them to a list.
# Then finally return the list of tuple.
# The field type should be tthe following
# - sku -> str
# - description -> str
# - title -> str
# - price -> float
# - weight -> float
# - inactive -> boolean
# - sale_price -> float / None
# - product_discount -> float / None
# - product_type -> str / None
# - quantity -> int
def make_product_tuples(products_dir: str):
    products = []

    with open(products_dir, newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        next(reader)

        for product in reader:

            sale_price = None
            if product[6] != 'NULL':
                sale_price = float(product[6])

            product_discount = None
            if product[7] != 'NULL':
                product_discount = float(product[7])

            product_type = product[8]
            if product_type == 'NULL':
                product_type = None

            weight = 0.0
            if product[4] != '':
                weight = float(product[4])

            prod_tup = (
                product[0],
                product[1],
                product[2],
                float(product[3]),
                weight,
                product[5] == '1',
                sale_price,
                product_discount,
                product_type,
                int(product[9])
            )
            products.append(prod_tup)

    return products

# Product class
# Product should have the following attributes or properties
# - sku -> str
# - description -> str
# - title -> str
# - price -> float
# - weight -> float
# - inactive -> boolean
# - sale_price -> float / None
# - product_discount -> float / None
# - product_type -> str / None
# - quantity -> int

# create a list of product objects from the list of product tuples
def make_product_objects(product_tuples):
    pass

# Store class
# The store should have the following attributes or properties
# - name -> str
# - products -> list of product objects
# - total_sold_amount -> float 
# 
# The store should have the following helper methods / functions
# - find_product -> should receive a sku string argument and then returns the product that have the same sku
# - find_discounted_products -> returns a list of discounted products and sort from cheapest to most expensive.
#       By default it will return only active products otherwise if specified it will include the inactive products.
# - find_products_on_sale -> returns a list of discounted products and sort from cheapest to most expensive.
#       By default it will return only active products otherwise if specified it will include the inactive products.
# - most_expensive -> this method returns the most expensive product of the store.
# - cheapest -> this method returns the cheapest product of the store.
# - sell -> this method should receive the sku to and quanity to sell.
#       After selling update the total_sold_amount and the quantity of the product.

# Customer class
# The customer should have the following attributes or properties
# - name -> str
# - purchase_history -> list of tuples which contains the product object, quantity, date of purchase
# - balance -> float
#
# The customer should have the following helper methods / functions
# - buy -> Buy method enables customer to buy products from the store.
#       It should receive the store object, product sku to buy, and quantiy.
#       The customer can only buy if he/she has enough money base on the number of quantity and price of the product,
#       If there's enough product quantity from the store, and if product is active. Hint! you probably need to call the sell method of store in this method.
#       After buying update the balance of the customer

if __name__ == "__main__":
    make_product_tuples(path)
    pass
