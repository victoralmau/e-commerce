# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class Website(models.Model):
    _inherit = 'website'

    @api.multi
    def sale_get_order(
            self, force_create=False, code=None, update_pricelist=None):
        res = super(Website, self).sale_get_order(
            force_create, code, update_pricelist)
        # re-order sale order lines
        if res:
            res.order_line.sorted(
                lambda x: (x.pack_item_id.sequence, x.pack_item_id.id))
        return res
