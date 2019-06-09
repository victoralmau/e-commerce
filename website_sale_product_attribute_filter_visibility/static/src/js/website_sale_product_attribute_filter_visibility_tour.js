/* Copyright 2019 Sergio Teruel
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("website_sale_product_attribute_filter_visibility.tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    var steps = [
 
       {
            content: "open customize menu",
            trigger: "a:contains('Customize')",
        },
        {
            content: "click on 'Product Attribute's Filter' to enable",
            trigger: "a:contains('Product Attribute')",
        },

        {
            content: "Check that Test color is showed as attribute",
            extra_trigger: ".js_attributes:has(strong:contains('Test Color'))",
            trigger: "a:contains('Customizable Desk')",
            
        },
    /*
        {
            extra_trigger: "#product_details:has(strong:contains('Legs'))",
            trigger: "a:contains('Products')",
            
        },*/
        /*
        {
            trigger: "a:contains('Customizable Desk')",
            extra_trigger: ".js_attributes:not(:has(strong:contains('Test Size')))",
        },
        
        {
            trigger: "span:contains('Shop')",

        },
        {
            content: "Check that Test color is showed as attribute",
            extra_trigger: ".js_attributes:has(strong:contains('Test Color'))",
            trigger: "a:contains('Customizable Desk')",

        },
        */
        /*
        {
            content: " II open customize menu",
            extra_trigger: "#product_details:has(strong:contains('Test Color'))",
            trigger: '#customize-menu > a',
        },
        {
            content: "II click on 'Product Attribute's Filter' to enable",
            trigger: "#customize-menu a:contains(Product Attribute's Filter)",
            
        },*/
        
      /*  {
            trigger: "span:contains('Shop')",
            extra_trigger: "#product_details:has(strong:contains('Test Color'))",
            extra_trigger: ".js_attributes:has(strong:contains('Test Color'))",

        },
        {
            content: "open customize menu",
            trigger: '#customize-menu > a',
        },
        {
            content: "click on 'Product Attribute's Filter' to enable",
            trigger: "#customize-menu a:contains(Product Attribute's Filter)",
            
        },
        {
            trigger: "a[href='/shop']",
            extra_trigger: "#product_details:has(strong:contains('Test Color'))",
            
        }, 
        {
            content: "Check that Test Size is showed as attibute",
            trigger: "a:contains('Customizable Desk')",
            extra_trigger: ".js_attributes:not(:has(strong:contains('Test Size')))",

        },
       {
            trigger: "a[href='/shop']",
            extra_trigger: "#product_details:has(strong:contains('Test Color'))",

        },
       {
            content: "open customize menu",
            trigger: '#customize-menu > a',
        },
        
        {
            content: "click on 'Product Attribute's Filter' to disable",
            trigger: "#customize-menu a:contains(Product Attribute's Filter)",
        },    */    

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
