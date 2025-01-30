
import re
import csv
from collections import Counter

# Define the file path
file_path = "orders.csv"

# Read file content
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Task 1: Extract all order numbers
order_number_pattern = r"\bORD\d{5}\b"
order_numbers = re.findall(order_number_pattern, content)

# Task 2: Extract all product names
product_name_pattern = r"(?<=Product: )[A-Za-z0-9\s]+"
product_names = re.findall(product_name_pattern, content)

# Task 3: Extract all prices
price_pattern = r"\$\d+\.\d{2}"
prices = re.findall(price_pattern, content)
numeric_prices = [float(p[1:]) for p in prices]  # Convert to float for processing

# Task 4: Extract all order dates
date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"
order_dates = re.findall(date_pattern, content)

# Task 5: Find all orders for products priced over $500
expensive_orders = [p for p in prices if float(p[1:]) > 500]

# Task 6: Change the date format to DD/MM/YYYY
formatted_dates = [re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\1/\2/\3", date) for date in order_dates]

# Task 7: Extract product names that have more than 6 characters
long_product_names = [name for name in product_names if len(name) > 6]

# Task 8: Count the occurrence of each product in the text
product_counts = Counter(product_names)

# Task 9: Extract the orders with prices ending in .99
prices_ending_in_99 = [p for p in prices if p.endswith(".99")]

# Task 10: Find the cheapest product
cheapest_price = min(numeric_prices)
cheapest_product_index = numeric_prices.index(cheapest_price)
cheapest_product = product_names[cheapest_product_index]

# Print results
print("Extracted Order Numbers:", order_numbers)
print("Extracted Product Names:", product_names)
print("Extracted Prices:", prices)
print("Extracted Order Dates:", order_dates)
print("Orders Priced Over $500:", expensive_orders)
print("Formatted Dates:", formatted_dates)
print("Products with >6 Characters:", long_product_names)
print("Product Occurrences:", product_counts)
print("Prices Ending in .99:", prices_ending_in_99)
print("Cheapest Product:", cheapest_product)
