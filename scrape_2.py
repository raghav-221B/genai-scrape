
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import json
import csv
import pandas as pd

# Open and read the details.json file
with open('details.json', 'r', encoding='utf-8') as file:
    content = json.load(file)

# Extract the relevant information about vendors
vendors_info = content.get('props', {}).get('pageProps',{}).get('data',{}).get('vendors',{})

# Print the extracted information
with open('details_2.json','w', encoding ='utf-8') as file:
    json.dump(vendors_info,file, indent=2)
# print(json.dumps(vendors_info, indent=2))
with open('details_2.json', 'r') as json_file:
    data = json.load(json_file)
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
    
    # Write header
    writer.writeheader()
    
    # Write data rows
    writer.writerows(data)

rest_id_arr =[]
with open('details_2.json', 'r') as json_file:
    data=json.load(json_file)
    for i in range(len(data)):
        rest_id_arr.append(data[i]['branchId'])
print(rest_id_arr)

df1 = pd.read_csv('PROD (4).csv')
df2 = pd.read_csv('output.csv')


df2['branchId'] = pd.to_numeric(df2['branchId'], errors='coerce')

df1_sorted = df1.sort_values(by='RESTAURANT_ID', ascending=True)
df2_sorted = df2.sort_values(by='branchId', ascending=True)

df1_sorted = df1_sorted.reset_index(drop=True)
df2_sorted = df2_sorted.reset_index(drop=True)

columns_df1 =['RESTAURANT_ID', 'RESTAURANT_NAME', 'STATUS', 'LISTING_POSITION', 'SCRAPE_CENTROID_LAT', 'SCRAPE_CENTROID_LNG', 'EOD_MINUTES_AVERAGE', 'RATING_VALUE', 'RATING_COUNT']
columns_df2 =['branchId', 'name', 'statusCode', 'shopPosition', 'latitude', 'longitude', 'avgDeliveryTime', 'rate', 'totalRatings']

columns_to_extract_df1 = df1_sorted[columns_df1[0]]
columns_to_extract_df2 = df2_sorted[columns_df2[0]]
zyte_output_recorded_at = df1_sorted['RECORDED_AT_UTC']
merged_df = pd.concat([zyte_output_recorded_at,columns_to_extract_df1], axis =1)
merged_df = pd.concat([merged_df, columns_to_extract_df2], axis=1)


for i in range(1,len(columns_df1)):
    columns_to_extract_df1 = df1_sorted[columns_df1[i]]
    columns_to_extract_df2 = df2_sorted[columns_df2[i]]
    merged_df = pd.concat([merged_df, columns_to_extract_df1], axis =1)
    merged_df = pd.concat([merged_df, columns_to_extract_df2], axis =1)


extra_columns_from_output = ['totalReviews', 'deliveryFee', 'minimumOrderAmount', 'acceptCreditCard', 'acceptDebitCard', 'acceptCash', 'isTalabatGO', 'preOrder', 'isGrocery', 'isDarkstore', 'isCokeRestaurant', 'isShopSponcered', 'isCateringAvailable', 'contactlessDelivery', 'IsProvideTracking', 'isProvideOrderStatus', 'Sponsored']
extra_columns_df2 =df2_sorted[extra_columns_from_output]


merged_df = pd.concat([merged_df, extra_columns_df2], axis =1)



merged_df.to_csv('output_file_combined.csv', index=False)
print(df2['branchId'].dtype)

