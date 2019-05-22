# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.addons.http_routing.models.ir_http import slug
from werkzeug.routing import RequestRedirect


class ProductAttributeResetValues(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        # Store in a user session the previous category to reset filter
        # attributes selected when the user changes to other category
        return super().shop(
            page=page, category=category, search=search, ppg=ppg, **post)
        if category:
            previous_category_id = request.session.get(
                'previous_category_id', False)
            if category.id != previous_category_id:
                request.session['previous_category_id'] = category.id
                # return request.render("website_sale.products", res.qcontext)
                # raise RequestRedirect('/shop/category/%s' % slug(category))
                # return redirect('/shop/category/%s' % slug(category))
                # return super().shop(page=page, category=category, search=search, ppg=ppg, **post)
                return res
        request.session['previous_category'] = (category and
                                                category.id or False)
        return super().shop(
            page=page, category=category, search=search, ppg=ppg, **post)
