# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.website_sale.controllers.main import website_sale


class WebsiteSale(website_sale):

    def _get_search_domain(self, search, category, attrib_values):
        domain = super(WebsiteSale, self)._get_search_domain(
            search, category, attrib_values)
        if category:
            orig_condition = ('public_categ_ids', 'child_of', int(category))
            if orig_condition in domain:
                pos = domain.index(orig_condition)
                domain[pos] = ('public_categ_ids', '=', int(category))
        else:
            domain.append(('id', '=', 0))
        return domain
