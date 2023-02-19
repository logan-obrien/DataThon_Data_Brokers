"""
Initial data cleaning
3 Steps:
Combine 'Beverage' and 'Beverages'
Fix null rows in unit_buying_price
Fix null rows in total_buying_price
"""
import pandas as pd
data = pd.read_csv('sales_data_2017_2018.csv')

# Combine beverage, beverages of main_category
data.loc[data.main_category == "Beverage", "main_category"] = "Beverages"
print(data["main_category"].unique())

# Unit_buying null rows calculated
# total_buying null rows calculated
data['unit_buying_price'] = data['unit_selling_price'] - data['unit_price_margin']
data['total_buying_price'] = data['total_selling_price'] - data['total_profit']

# Save final as csv
data.to_csv("cleaned_sales_data_2017_2018.csv", sep=',', encoding='utf-8')