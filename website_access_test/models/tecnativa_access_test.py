# Copyright 2020 Tecnativa
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields
from odoo.tools import html_translate


class TecnativaAccessTest(models.Model):
    _name = "tecnativa.access.test"

    name = fields.Char("name", required=True)
    duration = fields.Float("Duration")
    website_description = fields.Html(
        sanitize_attributes=False, translate=html_translate
    )
