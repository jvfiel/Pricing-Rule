frappe.ui.form.on("Sales Invoice Item", {
    item_code: function (doc, cdt, cdn) {
          let me = this;
        let row = frappe.get_doc(cdt, cdn);
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
                    console.log(r);
                    row.margin_type = "Percentage";
                    row.discount_percentage = r.message[0].discount_percentage;
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
                        row.margin_type = "Percentage";
                        row.discount_percentage = r.message[0].discount_percentage;
                    }
                });
            }
    }
});