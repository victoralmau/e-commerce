# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProductWebsitePackBlock(models.Model):
    _name = 'product.website.pack.block'
    _order = 'sequence, id'

    name = fields.Char()
    sequence = fields.Integer()


class ProductWebsitePack(models.Model):
    _name = 'product.website.pack'
    _order = 'sequence, id'

    name = fields.Char()
    block = fields.Many2one(comodel_name='product.website.pack.block')
    sequence = fields.Integer(related='block.sequence', store=True)
    public_categ_ids = fields.Many2many(
        comodel_name='product.public.category',
        relation='product_website_pack_product_public_category_rel',
        column1='pack_id',
        column2='category_id',
        string='Public Category',
        help="Those categories are used to group similar products for "
             "e-commerce.")
    line_ids = fields.One2many(
        comodel_name='product.website.pack.line', inverse_name='pack_id',
        string='Lines')


class ProductWebsitePackLine(models.Model):
    _name = 'product.website.pack.line'
    _order = 'sequence, id'
    _rec_name = 'pack_id'

    pack_id = fields.Many2one(
        comodel_name='product.website.pack', ondelete='cascade',
        string='Product Pack')
    product_id = fields.Many2one(
        comodel_name='product.product', ondelete='restrict', string='Product')
    default_checked = fields.Boolean()
    sequence = fields.Integer()
