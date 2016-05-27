# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _website_product_id_change(
            self, order_id, product_id, qty=0, line_id=None):
        res = super(SaleOrder, self)._website_product_id_change(
            order_id, product_id, qty, line_id)
        ctx = self.env.context
        if 'public_categ_id' in ctx:
            res['public_categ_id'] = ctx['public_categ_id']
        if 'pack_item_id' in ctx:
            res['pack_item_id'] = ctx['pack_item_id']
        return res


class SeleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pack_item_id = fields.Many2one(
        comodel_name='product.website.pack.line', string='Pack Item')
    public_categ_id = fields.Many2one(
        comodel_name='product.public.category', string='Public Category')
