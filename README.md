# code-challenge-wk3

# Restaurant Reviews Database

This project demonstrates a basic database application for managing restaurant reviews. It uses SQLAlchemy, a Python SQL toolkit and Object-Relational Mapping (ORM) library, to create and interact with a SQLite database. The database consists of three main tables: restaurants, customers, and reviews. The code provides functionality to add restaurants and customers, write reviews, and retrieve various information from the database.


# Prerequisites

Before running this code, make sure you have the following dependencies installed:

Python (3.6 or higher)
SQLAlchemy

You can install SQLAlchemy using pip:

pip install sqlalchemy

# Getting Started

Clone this repository to your local machine:


git clone https://github.com/Kiarie-Kariuki/code-challenge-wk3.git

Change to the project directory:

cd code-challenge

Create a virtual environment (optional but recommended):

python -m venv venv


Install the required dependencies:

pip install -r requirements.txt

# Database Structure

The database consists of three tables:

    restaurants: Stores information about restaurants, including their name and price range.
    customers: Contains data about customers, including their first name and last name.
    reviews: Links customers to restaurants and stores review information, including star ratings.

# Usage

The restaurant_reviews.db SQLite database is automatically created when you run the code. You can interact with the database using the provided classes and methods:

    Restaurant: Represents a restaurant and has methods for retrieving the fanciest restaurant and all reviews for a restaurant.
    Customer: Represents a customer and includes methods to retrieve their favorite restaurant, full name, and add/delete reviews.
    Review: Represents a review and contains methods for retrieving customer and restaurant information, as well as the full review text.

## Examples

Here are some example usages of the code:

# Creating restaurant and customer instances
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Adding instances to the database and committing changes
session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()

# Adding reviews for customers
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Retrieving information
favorite_restaurant_name = customer1.favorite_restaurant().name
full_name = customer1.full_name()
first_review = restaurant1.reviews[0].full_review()
all_reviews_for_restaurant1 = restaurant1.all_reviews()

# Printing the results
print(f"Favorite Restaurant for {full_name}: {favorite_restaurant_name}")
print(f"Full Name: {full_name}")
print(f"First Review: {first_review}")
print("All Reviews for Restaurant A:")
for review in all_reviews_for_restaurant1:
    print(review)

This code demonstrates how to create restaurant and customer instances, add them to the database, write reviews, and retrieve information about customers and restaurants.

# Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please open an issue or create a pull request.

# License

This project is licensed under the CAK License - see the LICENSE file for details.