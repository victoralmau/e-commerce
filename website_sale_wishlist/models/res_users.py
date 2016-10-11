# -*- coding: utf-8 -*-
# Copyright 2016 Jairo Llopis <jairo.llopis@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from openerp import api, fields, models
from openerp.http import request


class ResUsers(models.Model):
    _inherit = "res.users"

    current_session = fields.Char(compute="_compute_current_session")

    @api.one
    def _compute_current_session(self):
        """Know current session for this user."""
        try:
            self.current_session = request.session.sid
        except AttributeError:
            self.current_session = False

    @api.model
    def check_credentials(self, password):
        """Make all this session's wishlists belong to its owner user."""
        result = super(ResUsers, self).check_credentials(password)
        self.env["wishlist.product"]._join_current_user_and_session()
        return result
