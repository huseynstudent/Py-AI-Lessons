from pathlib import Path

import pandas as pd


# Task 1
books = pd.DataFrame(
    [
        {"Title": "The Hobbit", "Author": "J.R.R. Tolkien", "Year Published": 1937, "Price": 14.99},
        {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Year Published": 1960, "Price": 12.50},
        {"Title": "The Martian", "Author": "Andy Weir", "Year Published": 2011, "Price": 18.75},
        {"Title": "Educated", "Author": "Tara Westover", "Year Published": 2018, "Price": 16.00},
        {"Title": "Where the Crawdads Sing", "Author": "Delia Owens", "Year Published": 2018, "Price": 13.25},
        {"Title": "Tomorrow, and Tomorrow, and Tomorrow", "Author": "Gabrielle Zevin", "Year Published": 2022, "Price": 21.00},
    ]
)

print("Task 1: Books")
print(books.to_string(index=False))
print(f"\nAverage book price: ${books['Price'].mean():.2f}")
print("\nBooks published after 2015:")
print(books.loc[books["Year Published"] > 2015].to_string(index=False))
print("\nBooks sorted by price (ascending):")
print(books.sort_values("Price").to_string(index=False))


# Task 2: Orders from CSV file
orders = pd.read_csv(Path(__file__).with_name("orders.csv"))

print("\nTask 2: Orders")
print("First ten rows:")
print(orders.head(10).to_string(index=False))
print("\nNumber of orders per customer:")
print(orders["Customer"].value_counts().to_string())
print(f"\nMaximum order amount: ${orders['Amount'].max():.2f}")
print(f"Minimum order amount: ${orders['Amount'].min():.2f}")
print(f"Total amount of all orders: ${orders['Amount'].sum():.2f}")


# Task 3
foods = pd.DataFrame(
    [
        {"Product": "Apple", "Category": "Fruit", "Calories": 95, "Protein": 0.5},
        {"Product": "Banana", "Category": "Fruit", "Calories": 105, "Protein": 1.3},
        {"Product": "Avocado", "Category": "Fruit", "Calories": 320, "Protein": 4.0},
        {"Product": "Broccoli", "Category": "Vegetable", "Calories": 55, "Protein": 3.7},
        {"Product": "Sweet potato", "Category": "Vegetable", "Calories": 180, "Protein": 4.0},
        {"Product": "Lentils", "Category": "Legume", "Calories": 230, "Protein": 18.0},
        {"Product": "Chickpeas", "Category": "Legume", "Calories": 364, "Protein": 19.0},
        {"Product": "Chicken breast", "Category": "Protein", "Calories": 165, "Protein": 31.0},
        {"Product": "Salmon", "Category": "Protein", "Calories": 412, "Protein": 25.0},
        {"Product": "Almonds", "Category": "Nuts", "Calories": 579, "Protein": 21.0},
    ]
)

print("\nTask 3: Food products")
print(foods.to_string(index=False))
print("\nFoods with more than 300 calories:")
print(foods.loc[foods["Calories"] > 300].to_string(index=False))
print("\nAverage protein by category:")
print(foods.groupby("Category")["Protein"].mean().to_string())
print("\nFoods sorted by calories (descending):")
print(foods.sort_values("Calories", ascending=False).to_string(index=False))


# Task 4
employee_projects = pd.DataFrame(
    [
        {"Name": "Ava", "Project": "Website", "Hours": 12},
        {"Name": "Ava", "Project": "Mobile App", "Hours": 8},
        {"Name": "Noah", "Project": "Website", "Hours": 15},
        {"Name": "Mia", "Project": "Data Dashboard", "Hours": 10},
        {"Name": "Noah", "Project": "Data Dashboard", "Hours": 9},
        {"Name": "Liam", "Project": "Mobile App", "Hours": 14},
        {"Name": "Mia", "Project": "Website", "Hours": 7},
        {"Name": "Liam", "Project": "Data Dashboard", "Hours": 11},
    ]
)

print("\nTask 4: Employee project hours")
print("Original data:")
print(employee_projects.to_string(index=False))
hours_by_employee = employee_projects.groupby("Name")["Hours"].sum()
print("\nTotal hours by employee:")
print(hours_by_employee.to_string())
print("\nTotal hours by project:")
print(employee_projects.groupby("Project")["Hours"].sum().to_string())
top_employee = hours_by_employee.idxmax()
print(f"\nEmployee with the most hours: {top_employee} ({hours_by_employee.max()} hours)")


# Task 5
ticket_sales = pd.DataFrame(
    [
        {"Movie": "Starlight", "City": "Baku", "Tickets Sold": 120},
        {"Movie": "Ocean Deep", "City": "Ganja", "Tickets Sold": 85},
        {"Movie": "Starlight", "City": "Sumqayit", "Tickets Sold": 95},
        {"Movie": "The Last Garden", "City": "Baku", "Tickets Sold": 110},
        {"Movie": "Ocean Deep", "City": "Baku", "Tickets Sold": 130},
        {"Movie": "The Last Garden", "City": "Ganja", "Tickets Sold": 75},
        {"Movie": "Starlight", "City": "Ganja", "Tickets Sold": 105},
        {"Movie": "Ocean Deep", "City": "Sumqayit", "Tickets Sold": 90},
        {"Movie": "The Last Garden", "City": "Sumqayit", "Tickets Sold": 80},
        {"Movie": "Starlight", "City": "Baku", "Tickets Sold": 140},
        {"Movie": "Ocean Deep", "City": "Ganja", "Tickets Sold": 100},
        {"Movie": "The Last Garden", "City": "Baku", "Tickets Sold": 125},
    ]
)

print("\nTask 5: Movie ticket sales")
print(ticket_sales.to_string(index=False))
sales_by_movie = ticket_sales.groupby("Movie")["Tickets Sold"].sum()
print("\nTickets sold by movie:")
print(sales_by_movie.to_string())
print("\nTickets sold by city:")
print(ticket_sales.groupby("City")["Tickets Sold"].sum().to_string())
top_movie = sales_by_movie.idxmax()
print(f"\nMovie with the highest sales: {top_movie} ({sales_by_movie.max()} tickets)")

 
# Task 6
customers = pd.DataFrame( 
    [
        {"ID": 1, "Name": "Aylin", "City": "Baku"},
        {"ID": 2, "Name": "Murad", "City": "Ganja"},
        {"ID": 3, "Name": "Leyla", "City": "Sumqayit"},
        {"ID": 4, "Name": "Rashad", "City": "Baku"},
        {"ID": 5, "Name": "Nigar", "City": "Sheki"},
    ]
)

customer_orders = pd.DataFrame(
    [
        {"Customer ID": 1, "Order": "Notebook", "Cost": 8.50},
        {"Customer ID": 1, "Order": "Pens", "Cost": 4.25},
        {"Customer ID": 2, "Order": "Backpack", "Cost": 32.00},
        {"Customer ID": 3, "Order": "Desk lamp", "Cost": 19.99},
        {"Customer ID": 3, "Order": "Planner", "Cost": 12.50},
        {"Customer ID": 4, "Order": "Headphones", "Cost": 45.00},
        {"Customer ID": 5, "Order": "Water bottle", "Cost": 15.75},
    ]
)

print("\nTask 6: Customers and orders")
print("Customers:")
print(customers.to_string(index=False))
print("\nOrders:")
print(customer_orders.to_string(index=False))
merged_orders = customers.merge(
    customer_orders,
    left_on="ID",
    right_on="Customer ID",
)
customer_totals = (
    merged_orders.groupby(["ID", "Name", "City"], as_index=False)["Cost"]
    .sum()
    .rename(columns={"Cost": "Total Cost"})
)
print("\nTotal order cost by customer:")
print(customer_totals.to_string(index=False))
