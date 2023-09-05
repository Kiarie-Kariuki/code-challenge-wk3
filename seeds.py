from database import session
from database import Restaurant, Customer

restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()
