# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    website_pack_ids = fields.One2many(
        comodel_name='product.website.pack.line', inverse_name='product_id')


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    website_pack_ids = fields.Many2many(
        comodel_name='product.website.pack',
        relation='product_website_pack_product_public_category_rel',
        column1='category_id',
        column2='pack_id',
        string='Website Packs',
        help="Those packs are used to group similar products for "
             "e-commerce.")
    website_published = fields.Boolean('Available in the website', copy=False)
    website_description = fields.Char(
        'Description for the website', translate=True)
