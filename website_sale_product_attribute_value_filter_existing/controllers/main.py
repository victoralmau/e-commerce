# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http


class ProductAttributeValues(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        response = super(ProductAttributeValues, self).shop(
            page=page,
            category=category,
            search=search,
            ppg=ppg,
            **post)

        # Include all products
        # url = "/shop"
        attrib_list = request.httprequest.args.getlist('attrib')
        attrib_values = [
            [int(x) for x in v.split("-")] for v in attrib_list if v]
        domain = self._get_search_domain(search, category, attrib_values)

        product = request.env['product.template']
        products = response.qcontext['products']
        if products:
            # get all products without limit
            selected_products = product.search(domain, limit=False)

        # Load all products without limit for the
        # filter check on attribute values
        response.qcontext['products_all'] = selected_products

        return response
