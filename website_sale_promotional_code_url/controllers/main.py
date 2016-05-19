# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from openerp import http
from openerp.http import request

from openerp.addons.website_sale.controllers.main import website_sale
from openerp.addons.website_sale.controllers.main import \
    get_pricelist as orig_get_pricelist

_logger = logging.getLogger(__name__)


def get_pricelist():
    sale_order_id = request.session.get('sale_order_id')
    if sale_order_id:
        sale_order = request.env['sale.order'].sudo().browse(sale_order_id)
        return sale_order.pricelist_id
    else:
        return orig_get_pricelist()


class WebsiteSale(website_sale):

    def get_pricelist(self):
        return get_pricelist()

    @http.route(
        ['/shop/code/<pricelist_code>'], type='http', auth="public",
        website=True)
    def promotional_code_pricelist(self, pricelist_code, **post):
        request.website.sale_get_order(
            code=pricelist_code, context=request.context)
        return request.redirect("/shop")
