# Copyright 2020 Tecnativa
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request


class Website(http.Controller):
    @http.route(['/tecnativa/access/test'], type='http', auth='user',
                website=True)
    def tecnativa_access_test(self):
        record = request.env['tecnativa.access.test'].search([
            ('id', '=', request.env.ref('website_access_test.tecnativa_access_test_01').id)
        ])
        return request.render('website_access_test.tectnativa_access_test', {
            'record': record
        })
