from requests import get
import pprint

response = get("https://www.gintarine.lt/persalimas")
html_content = response.text
from lxml.html import fromstring

tree = fromstring(html_content)

products = tree.xpath("//div[contains(@class, 'product-item')]")

product_data = []

for product in products:

    product_name = product.xpath(".//input[@name='productName']/@value")
    product_price = product.xpath(".//input[@name='productPrice']/@value")

    if product_name and product_price:
        product_data.append({
            "Product_name": product_name[0],
            "price": product_price[0],
        })

pprint.pprint(product_data)




