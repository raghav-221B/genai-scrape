from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from openai import OpenAI
import json
import csv
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import uuid
import requests
from selenium.common.exceptions import StaleElementReferenceException
from openai.types.chat.completion_create_params import ResponseFormat





class OpenAIChatBot:
    def __init__(self, api_key:str, gpt_model:str):
        self.api_key = api_key
        self.gpt_model = gpt_model
        self.client = OpenAI(api_key=self.api_key)

    def chat(self, system : str, user : str) ->str:
        try:
            result= self.client.chat.completions.create(
                model=self.gpt_model,
                response_format={ "type": "json_object" },

                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ]
            )
            output = result.choices[0].message.content
            if not output:
               raise Exception("No response from the chatbot")
            return output   
        except Exception as e:
            print(f"Error: {e}")
            raise e

def extract_info_from_chunk(chunk):

    restaurant_id = 12345
    restaurant_url = "https://www.talabat.com/uae/restaurant/664974/italiere-muwaileh-commercial?aid=1513"
    restaurant_name = "Example Restaurant"
    position = 1
    cuisines = ["Italian", "Pizza", "Pasta"]
    is_new = True
    is_promoted = False
    average_delivery_time = 30
    max_delivery_time = 40
    min_delivery_time = 25
    delivery_time_description = "30 mins"
    fulfillment_type = "PLATFORM_FLEET"
    status = "ONLINE"
    delivery_fee = 5.0
    minimum_order_value = 20.0
    currency = "AED"
    rating_value = 4.7
    rating_count = 350
    prompt = f"""
    ## CONTEXT: We have a large HTML document that we have chunked up into smaller chunks.
    You are receiving a smaller chunk. The large HTML document is a webpage of a restaurant listed on a food delivery website.
    You need to extract information about that restuarant from the given HTML chunk.
    
    
  
    #TASK: Extract the details of the restaurant from the provided HTML page source and output them in the following JSON format:

   {{
  "restaurant": {{
    "id": "",
    "url": "",
    "name": "",
    "position": 
    "tags": {{
      "cuisines": 
      "is_new": 
      "is_promoted": 
    }},
    "delivery": {{
      "eod": {{
        "average":
        "max": 
        "min": 
        "str": 
      }},
      "fulfillment_type": 
      "status": 
    }},
    "fees": {{
      "delivery_charge":
      "minimum_order_amount": 
      "currency": 
    }},
    "rating": {{
      "value":
      "count": 
    }}
  }}
}}


explanation for some metrics:
status : It shows whether the restaurant is online or offline
fulfillment_type : It shows the type of delivery service used by the restaurant
eod : It shows the estimated delivery time range for the restaurant
tags : It shows the tags associated with the restaurant like cuisines, is_new, is_promoted
delivery_charge : It shows the delivery charge for the restaurant
minimum_order_amount :It is minimum order amount from the restaurant it will be in the currency mentioned


##IMPORTANT: You are a webscrapper which outputs the above JSON format for the given chunk and if you are not able to find 
any information about restaurant details in the given chunk, then you need to return only empty JSON object, no additional text
should be there.


    HTML chunked content:
    {chunk}   """
    system = "You are a webscraping and HTML parsing expert who follows the given prompt."
    response = chatbot.chat(system=system, user=prompt)
    return response




    

# service = Service(ChromeDriverManager().install())
# ua_id = str(uuid.uuid4())
# chrome_options = uc.ChromeOptions()
# chrome_options.add_argument(f"uaId={ua_id}")
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
# driver = uc.Chrome(options=chrome_options, version_main=131)
# # for i in range(1, 2):

  
# #   url = "https://www.talabat.com/uae/restaurants/1513/al-gharayen"+"?page="+str(i)
# #   driver.get(url)     
# #   time.sleep(5)
# #   html_content = driver.page_source
# # # with open('html_content.txt', 'w', encoding='utf-8') as file:
# # #     file.write(html_content)
# # # bytes_data = html_content.encode()
# # # with open('bytes_data.txt', 'w', encoding='utf-8') as file:
# # #     file.write(str(bytes_data))

# #   chatbot= OpenAIChatBot(api_key ="sk-svcacct-5Ytc9Zs7cJADFx_-U1WE8VuUIw73XX2WYysFkJD61LwAQZyYbrnrLGPThUNfwLQV-ZO8-weH0EvT3BlbkFJBRCZXu9UydUxyhROcLroRgEeJAbFB38HaUm5zxxUmCpCq4JlI_CbvKbn-pfn2LBYQiM9cjR01AA", gpt_model="gpt-3.5-turbo")

# #   chunks = [html_content[i:i + 10000] for i in range(0, len(html_content), 10000)]
# #   response = []
# #   for chunk in chunks:
# #      response.append(extract_info_from_chunk(chunk))
# # #   parsed_data = [json.loads(i) for i in response]

    
# #   data =[]
# #   all_json_objects = []
  
# #   for item in response:
# #     s=""
# #     for i in range(len(item)):
# #         if(item[i]=='`'):
# #             i=i+7
# #         else:
# #             s=s+item[i]
# #     data.append(s[4:])

# #   for string in data:
# #     string.replace("json", "")
    

# #     json_strings = string.split('}, {')
    
# #     json_strings = [s.replace('}{', '}').replace('},{','}').replace('{ ', '{') for s in json_strings]
# #     for json_str in json_strings:
# #         try:
# #             json_obj = json.loads(json_str)
# #             print(f"working_fine: {json_obj}")
# #             all_json_objects.append(json_obj)
 
# #         except json.JSONDecodeError as e:
# #             print(f"Error decoding JSON: {e} for string: {json_str}")
# #   final=[]
# #   for obj in all_json_objects:
# #     for i in obj:
# #         if(isinstance(i, dict)):
# #             if((i['restaurant']['id']is not None ) and (i['restaurant']['id']!=0)):
# #                 final.append(i)
                
# #   with open("output.json", "w") as f:
# #     json.dump(final, f, indent=4)



    

  

  
# #   file_path = 'output.json'
# #   with open(file_path, 'w') as file:
# #      json.dump(filtered_data, file, indent=4)
    

# # Now parsed_data will be a list of dictionaries, excluding empty or invalid strings
url = "https://www.talabat.com/uae/restaurants/1513/al-gharayen"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)
time.sleep(5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# body = driver.find_element(By.TAG_NAME, "body")
# body_html = body.get_attribute("outerHTML")
# def extract_info(html):
#     prompt = f"""
#     I am passing samller chunks of a HTML source code of a webpage of a food delivery website.
#     There is an anchor tag in the given chunk which contains links to restaurant pages.
#     You need to tell me the id of that anchor tag.
#     Output should be:
#     ID : "id of the anchor tag"
#     If the given chunk doesnt seems to have such class, return null.
#     Output should only be the extracted information in the JSON format. No additional text.
#     HTML chunked content: {html}
#     """
   
#     system = "You are a webscraping and HTML parsing expert"
#     response = chatbot.chat(system=system, user=prompt)
#     return response

chatbot= OpenAIChatBot(api_key ="sk-svcacct-5Ytc9Zs7cJADFx_-U1WE8VuUIw73XX2WYysFkJD61LwAQZyYbrnrLGPThUNfwLQV-ZO8-weH0EvT3BlbkFJBRCZXu9UydUxyhROcLroRgEeJAbFB38HaUm5zxxUmCpCq4JlI_CbvKbn-pfn2LBYQiM9cjR01AA", gpt_model="gpt-3.5-turbo-1106")
# chunks = [body_html[i:i + 10000] for i in range(0, len(body_html), 10000)]
# response =[]
# id=""
# for chunk in chunks:
#     response.append(extract_info(chunk))
# for item in response:
#     try:
        
#         parsed_item = json.loads(item)
        
#         # Check if the 'ID' exists and is not null
#         if parsed_item.get("ID") and parsed_item["ID"] != "null":
#            id = parsed_item["ID"]
#            break  
#     except json.JSONDecodeError:
        
#         continue
# print(id)

# a_elements = driver.find_elements(By.CSS_SELECTOR, f'a[data-testid={id}]')
# a_elements[0].click()
# time.sleep(5)
# driver.back()
# time.sleep(5)
# a_elements = driver.find_elements(By.CSS_SELECTOR, f'a[data-testid={id}]')
# a_elements[0].click()
# time.sleep(5)


# print(a_elements[0])
# # # href_value = a_elements[0].get_attribute("href")
# # driver.get(href_value)
# wait = WebDriverWait(driver, 20)

# info_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Info"]')))

# print(info_button)
# info_button.click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# body = driver.find_element(By.TAG_NAME, "body")
# body_html = body.get_attribute("outerHTML")
# with open('html_content.txt', 'w', encoding='utf-8') as file:
#     file.write(body_html)
driver.implicitly_wait(10)
body =driver.find_element(By.ID, "__NEXT_DATA__")
body_html = body.get_attribute("innerHTML")
print(len(body_html))
with open('details.json','w', encoding ='utf-8') as file:
   file.write(body_html)
# chunks = [body_html[i:i + 10000] for i in range(0, len(body_html), 10000)]
# response = []
# for chunk in chunks:
#     ans=extract_info_from_chunk(chunk)
#     response.append(ans)
#     print(ans)
    
  
  




 
  

  

 



