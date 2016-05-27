# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'product.pricelist'

    delivery_ids = fields.Many2many(
        comodel_name='delivery.carrier',
        string='Delivery Method')
