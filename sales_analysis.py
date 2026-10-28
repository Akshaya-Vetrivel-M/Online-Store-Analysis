import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("online_store_sales.csv")

# Clean the data
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Quantity"] = df["Quantity"].fillna(0)

# Remove duplicate records
df = df.drop_duplicates()

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Group revenue by product
product_sales = df.groupby("Product")["Revenue"].sum()
product_sales = product_sales.sort_values(ascending=False)

print("\nREVENUE BY PRODUCT")
print(product_sales)

# Create bar chart
plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("charts/revenue_by_product.png")
plt.show()

print("\nChart saved in charts/revenue_by_product.png")

# STEP 7: REVENUE BY CITY

city_sales = df.groupby("City")["Revenue"].sum()
city_sales = city_sales.sort_values(ascending=False)

print("\nREVENUE BY CITY")
print(city_sales)

# Create city revenue chart
plt.figure(figsize=(10, 6))
city_sales.plot(kind="bar")

plt.title("Total Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("charts/revenue_by_city.png")
plt.show()

print("\nCity chart saved successfully!")

# STEP 8: REVENUE BY CATEGORY

category_sales = df.groupby("Category")["Revenue"].sum()
category_sales = category_sales.sort_values(ascending=False)

print("\nREVENUE BY CATEGORY")
print(category_sales)

# Create category revenue chart
plt.figure(figsize=(9, 6))
category_sales.plot(kind="bar")

plt.title("Total Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("charts/revenue_by_category.png")
plt.show()

print("\nCategory chart saved successfully!")

# STEP 9: MONTHLY SALES TREND

# Extract year and month from the Date column
df["Year_Month"] = df["Date"].dt.to_period("M").astype(str)

# Calculate monthly revenue
monthly_sales = df.groupby("Year_Month")["Revenue"].sum()

print("\nMONTHLY SALES REVENUE")
print(monthly_sales)

# Create line chart
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig("charts/monthly_sales_trend.png")
plt.show()

print("\nMonthly sales chart saved successfully!")

# STEP 10: KEY BUSINESS METRICS

# Total revenue
total_revenue = df["Revenue"].sum()

# Total quantity sold
total_quantity = df["Quantity"].sum()

# Total number of orders
total_orders = df["Order_ID"].nunique()

# Average order value
average_order_value = total_revenue / total_orders if total_orders > 0 else 0

# Best-selling product by quantity
product_quantity = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_quantity.idxmax()

# City generating the highest revenue
city_revenue = df.groupby("City")["Revenue"].sum()
top_city = city_revenue.idxmax()

# Category generating the highest revenue
category_revenue = df.groupby("Category")["Revenue"].sum()
top_category = category_revenue.idxmax()

# Display results
print("\n========== BUSINESS METRICS ==========")

print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,.0f}")
print(f"Total Unique Orders: {total_orders}")
print(f"Average Revenue per Order: {average_order_value:,.2f}")
print(f"Best-Selling Product: {best_selling_product}")
print(f"Highest-Revenue City: {top_city}")
print(f"Highest-Revenue Category: {top_category}")

print("======================================")

# STEP 11: EXPORT CLEANED DATA

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_sales_data.csv")

# STEP 12: VERIFY TOP-SELLING PRODUCTS

# Product with the highest quantity sold
quantity_by_product = df.groupby("Product")["Quantity"].sum()
top_quantity_product = quantity_by_product.idxmax()

# Product with the highest revenue
revenue_by_product = df.groupby("Product")["Revenue"].sum()
top_revenue_product = revenue_by_product.idxmax()

print("\n========== PRODUCT PERFORMANCE ==========")
print("Most units sold:", top_quantity_product)
print("Units sold:", quantity_by_product.max())

print("Highest revenue product:", top_revenue_product)
print("Revenue:", revenue_by_product.max())
print("=========================================")

# STEP 15: FINAL PROJECT SUMMARY

# Calculate key results
total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()

product_revenue = df.groupby("Product")["Revenue"].sum()
city_revenue = df.groupby("City")["Revenue"].sum()
category_revenue = df.groupby("Category")["Revenue"].sum()

top_product = product_revenue.idxmax()
top_city = city_revenue.idxmax()
top_category = category_revenue.idxmax()

# Build report
report = f"""
ONLINE STORE SALES DATA ANALYTICS REPORT

1. PROJECT OBJECTIVE
To analyze online store sales and identify
top-performing products, cities, and categories.

2. TOOLS USED
Python, Pandas, Matplotlib, VS Code

3. DATASET SUMMARY
Total records: {len(df)}
Total unique orders: {total_orders}
Total quantity recorded: {total_quantity:,.0f}

4. KEY FINDINGS
Total revenue: {total_revenue:,.2f}
Highest-revenue product: {top_product}
Highest-revenue city: {top_city}
Highest-revenue category: {top_category}

5. RECOMMENDATIONS
- Review inventory for high-revenue products.
- Study the sales performance of each city.
- Investigate low-performing product categories.
- Validate missing quantities and negative prices.
- Monitor monthly revenue to identify trends.

6. CONCLUSION
The analysis summarizes sales performance by
product, city, category, and month. The findings
can help the business plan inventory and improve
sales decisions. Revenue figures should be finalized
after validating negative prices and missing values.
"""

# Display report
print(report)

# Save report
with open("sales_analysis_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Report saved as sales_analysis_report.txt")
