# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import operator
from odoo import fields, models
from odoo.tools import ormcache


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    has_distinct_variant_price = fields.Boolean(
        compute='_compute_has_distinct_variant_price',
        string='Has variants with distinct price extra',
    )

    def _compute_has_distinct_variant_price(self):
        partner = self.env.context.get('partner')
        pricelist_id = self.env.context.get('pricelist')
        for template in self:
            if template.product_variant_count > 1:
                prices = template._get_variants_price(pricelist_id, 1, partner)
                if len(set(prices.values())) > 1:
                    template.has_distinct_variant_price = True

    # TODO: Use ormcache but we need invalidate cache in all models involved
    #  in a price change
    @ormcache('self.id', 'pricelist_id', 'qty', 'partner')
    def _get_variants_price(self, pricelist_id, qty, partner):
        pricelist = self.env['product.pricelist'].browse(pricelist_id)
        variants_nbr = len(self.product_variant_ids)
        quantities = [qty] * variants_nbr
        partners = [partner] * variants_nbr
        prices = pricelist.get_products_price(self.product_variant_ids,
                                              quantities, partners)
        return prices

    def _get_minimal_price(self, pricelist_id, qty, partner):
        prices = self._get_variants_price(pricelist_id, qty, partner)
        minimal_price = sorted(prices.items(), key=operator.itemgetter(1))[:1]
        return minimal_price

    def _get_combination_info(
        self, combination=False, product_id=False, add_qty=1, pricelist=False,
            parent_combination=False, only_template=False):
        """
        Update product template prices for products items view in website shop
        render with cheaper variant prices.
        """
        combination_info = super()._get_combination_info(
            combination=combination, product_id=product_id, add_qty=add_qty,
            pricelist=pricelist, parent_combination=parent_combination,
            only_template=only_template)
        if (only_template and self.env.context.get('website_id') and
                self.product_variant_count > 1):
            partner = self.env.context.get('partner')
            pricelist_id = self.env.context.get('pricelist')
            minimal_price = self._get_minimal_price(
                pricelist_id, add_qty, partner)
            combination_info.update({
                'price': minimal_price[0][1],
                'list_price': minimal_price[0][1],
            })
        return combination_info

    # TODO: Active cache
    @ormcache('self.id', 'product_attribute_values')
    def _get_cheaper_combination(self, product_attribute_values):
        ptav_obj = self.env['product.template.attribute.value']
        cheaper_combination = ptav_obj.search([
            ('product_tmpl_id', '=', self.id),
            ('product_attribute_value_id', 'in', product_attribute_values),
        ])
        return cheaper_combination.ids

    def _get_first_possible_combination(
            self, parent_combination=None, necessary_values=None):
        """
        Get the cheaper product combination for the product for website view.
        We only take into account attributes that generate variants and
        products with more than one variant.
        """
        combination = super()._get_first_possible_combination(
            parent_combination=parent_combination,
            necessary_values=necessary_values
        )
        if (self.env.context.get('website_id') and
                self.product_variant_count > 1):
            ptav_obj = self.env['product.template.attribute.value']
            partner = self.env.context.get('partner')
            pricelist_id = self.env.context.get('pricelist')
            minimal_price = self._get_minimal_price(
                pricelist_id, 1, partner)
            cheaper_variant_id = minimal_price[0][0]
            pav = self.env['product.product'].browse(
                cheaper_variant_id).attribute_value_ids
            cheaper_combination_ids = self._get_cheaper_combination(pav.ids)
            cheaper_combination = ptav_obj.browse(cheaper_combination_ids)
            variant_combination = combination.filtered(
                lambda x: x.attribute_id.create_variant == 'always')
            combination_returned = cheaper_combination + (
                combination - variant_combination)
            # Keep order to avoid This combination does not exist message
            return combination_returned.sorted(
                lambda x: x.attribute_id.sequence)
        return combination
