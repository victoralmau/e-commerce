# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http


class ProductAttributeValues(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values):
        domain = super(ProductAttributeValues, self)._get_search_domain(
            search, category, attrib_values)
        request.session['shop_search_domain'] = domain
        return domain

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        response = super(ProductAttributeValues, self).shop(
            page=page,
            category=category,
            search=search,
            ppg=ppg,
            **post)
        products = response.qcontext['products']
        if products:
            domain = request.session.get('shop_search_domain', [])
            # get all products without limit pagination
            products = request.env['product.template'].search(
                domain, limit=False)
        # Load all products without limit for the filter check on attribute
        # values
        response.qcontext['products_all'] = products
        response.qcontext['variants'] = products.mapped('product_variant_ids')
        return response
