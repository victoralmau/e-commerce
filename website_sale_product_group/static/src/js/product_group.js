/* © 2016 Tecnativa, S.L.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */
(function () {
    'use strict';
    var website = openerp.website;

    openerp.website.productpack = {};
    openerp.website.productpack.Pack = openerp.Widget.extend({
        init: function (dom) {
            var self = this;
            this.$el = this.$target = $(dom);
            this.start();
        },
        start: function () {
            var self = this;
            this.$el.find('#add_to_cart').on('click', function (event) {
                    event.preventDefault();
                    self.on_click();
                });
            this.$el.find('form input:checkbox').on('change', function (event) {
                    self.on_change();
                });
            $("#total_selected").text(self.calculate_total().toFixed(2).toString() +' €');
        },
        stop: function () {
        },
        on_click: function(){
            this.add_to_cart_group();
        },
        on_change: function(){
            $("#total_selected").text(this.calculate_total().toFixed(2).toString() +' €');
        },
        calculate_total: function(){
            var self = this;
            var amount = 0.0;
            $( ".chk_line:checked" ).each(function() {
                amount += parseFloat($(this).data('price')) * parseFloat($(this).data('unit'));
            });
            return amount;
        },
        add_to_cart_group: function (){
            var product_ids = [];
            product_ids = this.selected_lines();
            openerp.jsonRpc("/shop/cart/products_update_json", 'call', {
                'line_id': null,
                'product_ids': product_ids,
                'set_qty': 1})
                .then(function (data) {
                    if (!data.quantity) {
                        location.reload(true);
                        return;
                    }
                    var $q = $(".my_cart_quantity");
                    $q.parent().parent().removeClass("hidden", !data.quantity);
                    $q.html(data.cart_quantity).hide().fadeIn(600);
                    $("#cart_total").replaceWith(data['website_sale.total']);
                });
        },
        selected_lines: function (){
            var self = this;
            var product_ids = new Array();
            $( ".chk_line:checked" ).each(function() {
                var $check = $(this);
                product_ids.push({
                    'product_id': $check.data('product_id'),
                    'qty': $check.data('unit'),
                    'pack_item_id': $check.data('pack_item_id'),
                    'public_categ_id': $check.data('public_categ_id'),
                    });
            });
            return product_ids;
        }
    });

    $(document).ready(function () {
        new openerp.website.productpack.Pack(this);
    });
})();