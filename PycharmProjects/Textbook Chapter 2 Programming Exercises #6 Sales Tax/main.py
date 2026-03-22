a=float(input("Enter the amount of purchase: $"))
state_sales_tax=(.05*a)
county_sales_tax=(.025*a)
total_sales_tax=(state_sales_tax + county_sales_tax)
print(f'The amount of purchase was {a:.2f}')
print(f'the state sales tax was {state_sales_tax:.2f}')
print(f'the county sales tax was {county_sales_tax:.2f}')
print(f'the total sales tax was {total_sales_tax:.2f}')
total_of_sale=(a + total_sales_tax)
print(f'The total of sale was {total_of_sale:.2f}')


