from rich import print
from rich.table import Table

table = Table(title='PRICE TABLE')

table.add_column('Name', justify='left', style='red')
table.add_column('Price', justify='center')
table.add_row('Pen', '€2.99')
table.add_row('Keyboard', '€20.99')

print(table)