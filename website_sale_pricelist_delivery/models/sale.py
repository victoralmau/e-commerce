# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.addons.web.http import request


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _website_product_id_change(
            self, order_id, product_id, qty=0, line_id=None):
        res = super(SaleOrder, self)._website_product_id_change(
            order_id, product_id, qty, line_id)
        if 'product_ids' in request.params:
            res['wrap_option'] = False
            for product in request.params['product_ids']:
                if 'wrap_product' in product:
                    if product_id == product['wrap_product']:
                        res['wrap_option'] = True
        return res

    @api.model
    def _get_delivery_methods(self, order):
        print "pepe"
        delivery_ids = super(SaleOrder, self)._get_delivery_methods(order)
        deliveries = order.pricelist_id.delivery_ids
        if deliveries:
            delivery_ids = deliveries.filtered(
                lambda x: x.id in delivery_ids).ids
        return delivery_ids


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    wrap_option = fields.Boolean(string='Wrap Option')
