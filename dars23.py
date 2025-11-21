class Products:
    def __init__(self,title_name,price,year_of_production, expiring_date, country, product_type):
        self.title_name=title_name
        self.price=price
        self.year_of_production=year_of_production
        self.expiring_date=expiring_date
        self.country=country
        self.product_type=product_type


Product=Products('Zam-zam',13000, "10.11.2025", "10.05.2026", "Made in Uzbekistan", "water")
Product1=Products('Zizi',1000,"01.11.2025", "01.11.2026", "Made in Uzbekistan", "gum")
Product2=Products('chupa chups',2000,"12.10.2025", "12.10.2026", "Made in Spain", "lolipop")

base=[Product, Product1,Product2]

def view_product(s:list):
    count=0
    for product in base:
        count+=1
        print(f"{count}. {product.title_name}, {product.price}, {product.year_of_production}, {product.expiring_date}, {product.country}, {product.product_type}")
# view_product(base)
def add_product(s:list):
    title_name=input("Enter the title of the product: ")
    price=input("Enter the price of the product: ")
    year_of_production=input("Enter the year of the product: ")
    expiring_date=input("Enter the expiring date: ")
    country=input("Enter the country: ")
    product_type=input("Enter the product type: ")
    product = Products(title_name,price,year_of_production,expiring_date,country,product_type)
    s.append(product)
# add_product(base)
# view_product(base)
def product_manager(s:list):
    while True:
        kod=input(" 1. View products \n 2. Add products \n 3. Exit \n ")
        if kod=="1":
            view_product(s)
        elif kod=="2":
            add_product(s)
        elif kod=="3":
            break
        else:
            print("Invalid input")
            return
product_manager(base)