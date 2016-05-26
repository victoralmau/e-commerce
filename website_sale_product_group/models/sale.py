# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class SeleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pack_item_id = fields.Many2one(
        comodel_name='product.website.pack.line', string='Pack Item')
    public_categ_id = fields.Many2one(
        comodel_name='product.public.category', string='Public Category')
