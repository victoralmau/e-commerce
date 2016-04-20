# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models, _


class ProductWebsitePack(models.Model):
    _name = 'product.website.pack'
    _order = 'sequence'

    name = fields.Char(string='Name')
    public_categ_ids = fields.many2many(
        'product.public.category',
        string='Public Category',
        help="Those categories are used to group similar products for "
             "e-commerce.")
    line_ids = fields.One2many(
        comodel_name='product.website.pack.line', inverse_name='pack_id',
        string='Lines')
    sequence = fields.Integer()


class ProductWebsitePackLine(models.Model):
    _name = 'product.website.pack.line'
    _order = 'sequence'
    _rec_name = 'pack_id'

    pack_id = fields.Many2one(
        comodel_name='product.website.pack', ondelete='cascade',
        string='Product Pack')
    product_id = fields.Many2one(
        comodel_name='product.template', ondelete='restrict', string='Product')
    default_checked = fields.Boolean()
    sequence = fields.Integer()
