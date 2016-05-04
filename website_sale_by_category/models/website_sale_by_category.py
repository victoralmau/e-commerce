# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    show_child_category = fields.Boolean(string='Show Child Categories')
