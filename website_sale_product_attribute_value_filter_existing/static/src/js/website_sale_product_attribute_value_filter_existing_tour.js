/* Copyright 2019 Sergio Teruel
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("website_sale_product_attribute_value_filter_existing.tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    var steps = [
        {
            trigger: 'input[name=search]',
            run: 'text Ipod',
            extra_trigger: ".js_attributes:has(span:contains('Test Blue'))",
        },
        {
            trigger: '.oe_search_button',
            extra_trigger: ".js_attributes:has(span:contains('Test Blue'))",
        },
        {
            trigger: "a[href='/shop']",
            extra_trigger: "li:not(:has(span:contains('Test Blue')))",
        },
    ];
    tour.register("website_sale_product_attribute_value_filter_existing",
        {
            url: "/shop",
            test: true,
            wait_for: base.ready(),
        },
        steps
    );
    return {
        steps: steps,
    };
});
