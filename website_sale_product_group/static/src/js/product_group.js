/* © 2016 Tecnativa, S.L.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

(function () {
    'use strict';
    var website = openerp.website;

    $(document).ready(function () {
        $( ".chk_line" ).change(function () {
            var amount = 0.0;
            $( ".chk_line:checked" ).each(function() {
                amount += parseFloat($(this).attr('data_oe_lst_price'));
            });
            $("#total_selected").text(amount.toFixed(2).toString() +' €');
          }).change();
    });
})();