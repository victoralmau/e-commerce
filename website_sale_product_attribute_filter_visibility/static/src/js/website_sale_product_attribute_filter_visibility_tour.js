/* Copyright 2019 Sergio Teruel
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("website_sale_product_attribute_filter_visibility.tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    var steps = [

        {
            trigger: "span:contains('Shop')",
        },
         {
            trigger: 'input[name=search]',
            run: 'text Customizable Desk',
        },
        {
            trigger: '.oe_search_button',
        },
        {
            trigger: '.img'
        },
    ];
    tour.register("website_sale_product_attribute_filter_visibility",
        {
            url: "/",
            test: true,
            wait_for: base.ready(),
        },
        steps
    );
    return {
        steps: steps,
    };
});
