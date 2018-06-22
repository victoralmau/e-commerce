# -*- coding: utf-8 -*-

from odoo.addons.website_sale_stock.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteSale(WebsiteSale):

    def get_attribute_value_ids(self, product):
        res = super(WebsiteSale, self).get_attribute_value_ids(product)
        ProductProduct = request.env['product.product']
        for r in res:
            product_id = r[0]
            r[4]['virtual_available'] = ProductProduct.browse(
                product_id).virtual_available_global
        return res
