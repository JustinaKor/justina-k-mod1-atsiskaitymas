from requests import get
from lxml.html import fromstring

def gintarine_products(url):
    response = get(url)
    html_content = response.text
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

            return product_data