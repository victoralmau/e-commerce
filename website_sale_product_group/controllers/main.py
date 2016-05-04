# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import http
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale


class WebsiteSale(website_sale):

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        """/shop/category/<model("product.public.category"):category>/page/
        <int:page>"""], type='http', auth='public', website=True)
    def shop(self, page=0, category=None, search='', **post):
        cr, uid, context = request.cr, request.uid, request.context
        product_pack_obj = request.registry['product.website.pack']
        result = super(WebsiteSale, self).shop(
            page=page, category=category, search=search, **post)
        if category:
            result.qcontext['product_packs'] = category.website_pack_ids
        else:
            packs_ids = product_pack_obj.search(
                cr, uid, [], context=context)
            result.qcontext['product_packs'] = product_pack_obj.browse(
                cr, uid, packs_ids, context=context)
        return result
