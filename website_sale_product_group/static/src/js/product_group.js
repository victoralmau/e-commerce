/* © 2016 Tecnativa, S.L.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

(function () {
    'use strict';
    var website = openerp.website;

    website.productpack = {};
    website.productpack = openerp.Class.extend({
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
            this.$el.find('.chk_line').on('change', function (event) {
                    self.on_change();
                });
            self.calculate_total();
        },
        stop: function () {
        },
        on_click: function(){
            this.add_to_cart_group();
        },
        on_change: function(){
            this.calculate_total();
        },
        calculate_total: function(){
            var self = this;
            var amount = 0.0;
            $( ".chk_line:checked" ).each(function() {
                amount += parseFloat($(this).data('lst_price')) * parseFloat($(this).data('unit'));
            });
            $("#total_selected").text(amount.toFixed(2).toString() +' €');
        },
        add_to_cart_group: function (){
            var product_ids = [];
            var $check = $(this);
            $( ".chk_line:checked" ).each(function() {
                var $check = $(this);
                product_ids.push($check.data('product_id'));
            });
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
        }
    });

    $(document).ready(function () {
        new website.productpack(this);
    });
})();