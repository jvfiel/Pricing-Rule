function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}


frappe.ui.form.on("Sales Invoice Item", {
    item_code: function (doc, cdt, cdn) {
          let me = this;
        let row = frappe.get_doc(cdt, cdn);

        console.log(row.item_code);
        cur_frm.fields_dict.items.grid.get_field('uom').get_query =
        function() {
            return {

                query: "pricing_rule.pricing_rule.filter_uom",
            filters: {
                "item":row.item_code
            }
            }
        };



        console.log("pricing rule**");
        console.log(row);

        if(row.item_code && row.uom) {
            frappe.call({
                method: "pricing_rule.pricing_rule.get_pricing",
                args: {
                    item: row.item_code,
                    uom: row.uom,
                    pricelist:cur_frm.doc.selling_price_list
                },
                callback: function (r) {
                        if(!isEmpty(r.message)) {
                            // row.margin_type = "Percentage";
                            // row.discount_percentage = r.message[0].discount_percentage;
                            console.log(r.message[0].name);
                            row.pricing_rule = r.message[0].name;
                        }
                        else {
                            row.pricing_rule = "";
                            frappe.msgprint("no Princing Rule found.");
                        }
                        refresh_field("items");
                }
            });
        }
    }
    ,
    uom: function (doc, cdt, cdn) {
          let me = this;
        let row = frappe.get_doc(cdt, cdn);
        console.log("pricing rule**");
        console.log(row);

            if (row.item_code && row.uom) {
                frappe.call({
                    method: "pricing_rule.pricing_rule.get_pricing",
                    args: {
                        item: row.item_code,
                        uom: row.uom,
                        pricelist:cur_frm.doc.selling_price_list
                    },
                    callback: function (r) {
                        console.log(r);
                        if(!isEmpty(r.message)) {
                            // row.margin_type = "Percentage";
                            // row.discount_percentage = r.message[0].discount_percentage;
                            console.log(r.message[0].name);
                            row.pricing_rule = r.message[0].name;
                        }
                        else {
                            row.pricing_rule = "";
                            frappe.msgprint("no Princing Rule found.");
                        }
                        refresh_field("items");
                    }
                });
            }
    }
});