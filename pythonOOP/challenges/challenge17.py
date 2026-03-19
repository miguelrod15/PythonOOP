from rich import print
from rich.panel import Panel

class Product:
    '''
    This class creates a panel that show the product's name and price
    '''
    def __init__(self, name='', price=0):
        # Instance Attributes
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} costs €{self.price:.2f}"
    
    # Methods
    def price_tag(self):
        content = f"{self.name.center(30, ' ')}"
        content += f"{'-' * 30}"
        formated_price = f"€{self.price:,.2f}"
        content += f"{formated_price.center(30, '.')}"
        tag = Panel(content, title="Product", width=34)
        print(tag)
    

# Object declaration
p1 = Product("Iphone 17 Pro Max", 1500)
p2 = Product("PC GAMER", 3000)

p1.price_tag()
p2.price_tag()