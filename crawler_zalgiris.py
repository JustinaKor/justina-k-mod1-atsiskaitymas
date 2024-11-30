from requests import get
import pprint

response = get("https://shop.zalgiris.lt/collections/moterims")
html_content = response.text
from lxml.html import fromstring

tree = fromstring(html_content)

products = tree.xpath("//div[contains(@class, 'product-card')]")

product_data = []

for product in products:
    product_name = product.xpath('//div/a[contains(@class,"product-card-title")]/text()') #išsitraukia visi kategorijos pavadinimai
    product_price = product.xpath('.//span[contains(@class,"amount")]/text()')

    if product_name and product_price:
        product_data.append({
            "Product_name": product_name,
            "price": product_price,
        })

pprint.pprint(product_data)


