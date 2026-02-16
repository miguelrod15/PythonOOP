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
    
    # Methods
    def price_tag(self):
        panel = Panel(f'{self.name:^30}\n{self.price:^30}', title='Product', width=35)
        print(panel)
    

# Object declaration
p1 = Product("Iphone 17 Pro Max", 1500)
p2 = Product("PC GAMER", 3000)

p1.price_tag()
p2.price_tag()
print(p1.__doc__)