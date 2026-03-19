from rich import print
from rich.panel import Panel

class Barbecue:
    #Class Attributes
    standard_consumption:float = 0.400 # Each person on average, eat 400g of meat
    price_kg:float = 82.40 # Each Kg of meat cost €82.40

    def __init__(self, tittle, amount):
        # Instance Attributes
        self.tittle = tittle
        self.participants = amount
    
    def __str__(self):
        return f"This is {self.tittle} with {self.participants} people participating"
    
    #Methods
    def calculate_meat_amount(self) -> float:
        return self.participants * Barbecue.standard_consumption
    
    def calculate_total_cost(self)  -> float:
        return self.calculate_meat_amount() * Barbecue.price_kg

    def calculate_individual_cost(self) -> float:
        return self.calculate_total_cost() / self.participants

    def analyze(self):
        content = f"Analyzing [green]{self.tittle}[/] with [blue]{self.participants}[/]"
        content += f"\nEach participant will eat {Barbecue.standard_consumption}Kg and each Kg cost €{Barbecue.price_kg:,.2f}"
        content += f"\nYou should buy [blue]{self.calculate_meat_amount():.3f}Kg[/] of meat"
        content += f"\nThe final cost will be [red]€{self.calculate_total_cost():.2f}[/]"
        content += f"\nEach person will pay [yellow]€{self.calculate_individual_cost():,.2f}[/]"
        tag = Panel(content, title=self.tittle)
        print(tag)

#Object declaration   
c1 = Barbecue("Friends Barbecue", 15)
c1.analyze()

c2 = Barbecue("Barbeceu", 20)
c2.analyze()