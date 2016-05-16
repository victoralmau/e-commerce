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
            # result.qcontext['products'] -= category.website_pack_ids.mapped(
            #     'line_ids.product_id.product_tmpl_id')
        else:
            # packs_ids = product_pack_obj.search(
            #     cr, uid, [], context=context)
            # result.qcontext['product_packs'] = product_pack_obj.browse(
            #     cr, uid, packs_ids, context=context)
            result.qcontext['product_packs'] = product_pack_obj.browse(
                cr, uid, [], context=context)
        return result

    @http.route(['/shop/cart/products_update_json'], type='json',
                auth="public", methods=['POST'], website=True)
    def cart_products_update_json(
            self, product_ids, line_id, add_qty=None, set_qty=None):
        order = request.website.sale_get_order(force_create=1)
        for product_id in product_ids:
            value = order._cart_update(
                product_id=product_id, line_id=line_id, add_qty=add_qty,
                set_qty=set_qty)
        value['cart_quantity'] = order.cart_quantity
        value['website_sale.total'] = request.website._render(
            "website_sale.total", {
                'website_sale_order': request.website.sale_get_order()
            })
        return value
