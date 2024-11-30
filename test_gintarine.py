import unittest
from unittest.mock import patch
from crawler_gintarine2 import gintarine_products


class TestGintarineProducts(unittest.TestCase):

    @patch('crawler_gintarine2.get')
    def test_gintarine_products(self, mock_get):

        mock_html = """
        <div class="product-item">
            <input name="productName" value="RINOPANTEINA PLUS, nosies purškalas, 20 ml"/>
            <input name="productPrice" value="9.99"/>
        </div>
        <div class="product-item">
            <input name="productName" value="AFLUBIN PLUS, sirupas nuo kosulio, 175ml"/>
            <input name="productPrice" value="10.75"/>
        </div>
        """

        mock_get.return_value.text = mock_html

        products = gintarine_products("https://www.gintarine.lt/persalimas")

        expected = [
            {"Product_name": "RINOPANTEINA PLUS, nosies purškalas, 20 ml", "price": "9.99"},
            {"Product_name": "AFLUBIN PLUS, sirupas nuo kosulio, 175ml", "price": "10.75"},
        ]

        self.assertEqual(products, expected)


if __name__ == '__main__':
    unittest.main()







