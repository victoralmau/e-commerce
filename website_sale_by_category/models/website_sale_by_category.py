# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    website_description = fields.Char(
        'Description for the website', translate=True)
    website_published = fields.Boolean(
        string='Available in the website', default=True, copy=False)
