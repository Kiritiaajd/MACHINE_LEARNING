import csv
import random

# Define the file name
file_name = 'atm_customers.csv'

# Define some sample names
sample_names = ["Kiriti Aajad", "John Doe", "Jane Smith", "Alice Johnson", "Bob Brown",
                "Charlie White", "David Black", "Eva Green", "Frank Blue", "Grace Yellow"]

# Create data for 100 customers
customers = []
for i in range(100):
    name = random.choice(sample_names)
    acc_no = str(random.randint(10000, 99999))
    pin = str(random.randint(1000, 9999))
    balance = random.randint(5000, 100000)
    customers.append([name, acc_no, pin, balance])

# Write to a CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Account Number", "PIN", "Balance"])  # Header
    writer.writerows(customers)

file_name
