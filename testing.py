from database import session, Restaurant, Customer, Review

# Create new restaurant and customer instances
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Add the instances to the session and commit to save them to the database
session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()

# Add reviews for customers
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Retrieve the favorite restaurant, full name, and review information
favorite_restaurant_name = customer1.favorite_restaurant().name
full_name = customer1.full_name()
first_review = restaurant1.reviews[0].full_review()
all_reviews_for_restaurant1 = restaurant1.all_reviews()

# Print the results
print(f"Favorite Restaurant for {full_name}: {favorite_restaurant_name}")  # Should print 'Favorite Restaurant for John Doe: Restaurant B'
print(f"Full Name: {full_name}")  # Should print 'Full Name: John Doe'
print(f"First Review: {first_review}")  # Should print the review for Restaurant A
print("All Reviews for Restaurant A:")
for review in all_reviews_for_restaurant1:
    print(review)
