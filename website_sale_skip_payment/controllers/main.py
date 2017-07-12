# -*- coding: utf-8 -*-
# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import http
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale


class CheckoutSkipPayment(website_sale):

    @http.route(['/shop/payment'], type='http', auth="public", website=True)
    def payment(self, **post):
        context = request.context
        # check if user is logged
        if not request.session.uid:
            return super(CheckoutSkipPayment, self).payment(**post)

        order = request.website.sale_get_order(context=context)
        if order.action_confirm():
            # clean context and session, then redirect to the confirmation page
            request.website.sale_reset(context=context)
            return request.redirect('/shop/confirmation')
        else:
            return request.render(
                'website_sale_skip_payment.confirmation_order_error')
