# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProductWebsitePackBlock(models.Model):
    _name = 'product.website.pack.block'

    name = fields.Char()


class ProductWebsitePack(models.Model):
    _name = 'product.website.pack'
    _order = 'sequence, id'
    _rec_name = 'block'

    name = fields.Char(string='Description')
    block = fields.Many2one(comodel_name='product.website.pack.block')
    sequence = fields.Integer()
    public_categ_ids = fields.Many2many(
        comodel_name='product.public.category',
        relation='product_website_pack_product_public_category_rel',
        column1='pack_id',
        column2='category_id',
        string='Public Category')
    line_ids = fields.One2many(
        comodel_name='product.website.pack.line', inverse_name='pack_id',
        string='Products')


class ProductWebsitePackLine(models.Model):
    _name = 'product.website.pack.line'
    _order = 'sequence, id'

    pack_id = fields.Many2one(
        comodel_name='product.website.pack', ondelete='cascade',
        string='Product Pack')
    product_id = fields.Many2one(
        comodel_name='product.product', ondelete='restrict', string='Product')
    default_checked = fields.Boolean()
    sequence = fields.Integer()

    @api.multi
    def name_get(self):
        return {
            line.id: '%s%s' % (
                line.default_checked and '*' or '',
                line.product_id.name)
            for line in self}
