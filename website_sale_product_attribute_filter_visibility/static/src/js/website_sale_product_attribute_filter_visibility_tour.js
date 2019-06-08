/* Copyright 2019 Sergio Teruel
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("website_sale_product_attribute_filter_visibility.tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    var steps = [
          
    /*    {
            content: "open customize menu",
            trigger: '#customize-menu > a',
            timeout: 1000,
        },
        {
            content: "click on 'Product Attribute's Filter'",
            trigger: "#customize-menu a:contains(Product Attribute's Filter)",
            timeout: 1000,
        },
        */
        {
            trigger: "a:contains('Customize')",
        },
        {
            trigger: "a:contains('Product Attribute')",
        },
        {
            trigger: "a[href='/shop']",
            extra_trigger: ".js_attributes:has(strong:contains('Test Color'))",

        },
       {
            trigger: "a:contains('Customizable Desk')",
        },
    
        {
            trigger: "a[href='/shop']",
        },
        /*
        {
            trigger: "a:contains('Customizable Desk')",
           extra_trigger: ".js_attributes:not(:has(strong:contains('Test Size')))", 
        }, */
 /*     
        {
            content: "open customize menu",
            trigger: '#customize-menu > a',
            timeout: 1000,
        },
        {
            content: "click on 'Product Attribute's Filter'",
            trigger: "#customize-menu a:contains(Product Attribute's Filter)",
            timeout: 1000,
        }, */
    ];
    tour.register("website_sale_product_attribute_filter_visibility",
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
