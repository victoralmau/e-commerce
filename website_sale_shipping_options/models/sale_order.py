# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    shipping_option_ids = fields.Many2many(
        comodel_name='shipping.options',
        column1='order_id', column2='option_id',
        string='Shipping Options')

