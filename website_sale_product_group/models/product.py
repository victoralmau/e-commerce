# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    website_pack_ids = fields.One2many(
        comodel_name='product.website.pack.line', inverse_name='product_id')


class ProductProduct(models.Model):
    _inherit = 'product.product'
