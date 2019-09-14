function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}

frappe.ui.form.on("Sales Invoice Item", "item_code", function(doc,cdt,cdn){
     let row = frappe.get_doc(cdt, cdn);
    if(row.item_code) {
        frappe.call({
            method: "pricing_rule.pricing_rule.filter_uom",
            args: {
                item: row.item_code
            },
            callback: function (data) {
                if (data.message) {
                    var options = data.message;
                    console.log(data.message.length);
                    console.log("options.join:" + options.join("\n"));
                    var options_new = options.join("\n");

                    // var df = frappe.meta.get_docfield('Show Hide Desktop Icons','icon', cur_frm.doc.name);
                    // 		// console.log(df);
                    // 		df.options = r.message;
                    console.log(options_new);
                    frappe.meta.get_docfield("Sales Invoice Item", "uom_select", cur_frm.doc.name).options = options_new;
                    refresh_field("items");
                }
            }
        });
    }
});


frappe.ui.form.on("Sales Invoice Item", {

    uom_select:function(doc,cdt,cdn)
    {
        let row = frappe.get_doc(cdt, cdn);
        row.uom = row.uom_select;


         if(row.item_code && row.uom)
         {

              frappe.call({
                  method: "pricing_rule.pricing_rule.filter_uom_rate",
                  args: {
                      item: row.item_code,
                      uom:row.uom
                  },
                  async:false,
                  callback: function (data) {
                      if (!isEmpty(data.message)) {

                            frappe.call({
                                method: "pricing_rule.pricing_rule.get_price",
                                args: {
                                    item_code: row.item_code,
                                    price_list: cur_frm.doc.selling_price_list
                                },
                                async: false,
                                callback: function (price_list) {
                                        console.log(price_list);
                                    if(!isEmpty(price_list.message)) {
                                        frappe.call({
                                            method: "pricing_rule.pricing_rule.get_pricing",
                                            args: {
                                                item: row.item_code,
                                                uom: row.uom,
                                                pricelist: cur_frm.doc.selling_price_list
                                            },
                                            async: false,
                                            callback: function (r) {
                                                if (!isEmpty(r.message)) {
                                                    // row.margin_type = "Percentage";
                                                    // row.discount_percentage = r.message[0].discount_percentage;
                                                    console.log(r.message[0].name);
                                                    row.pricing_rule = r.message[0].name;
                                                    console.log(r.message[0].discount_percentage);
                                                    row.discount_percentage = r.message[0].discount_percentage;

                                                    var options = data.message;
                                                    console.log(options);
                                                    row.conversion_factor = options;
                                                    row.stock_qty = row.conversion_factor;
                                                    row.price_list_rate = price_list.message.price_list_rate * row.conversion_factor;
                                                    // row.rate = row.price_list_rate;
                                                    // row.rate = row.price_list_rate*row.conversion_factor;
                                                    row.rate = row.price_list_rate;
                                                    // console.log("-------------------------------");
                                                    // console.log(((row.price_list_rate*row.conversion_factor) * row.qty));
                                                    // console.log((((row.price_list_rate*row.conversion_factor) * row.qty) * (row.discount_percentage/100)));
                                                    // row.discount_amount = (((row.price_list_rate*row.conversion_factor) * row.qty) * (row.discount_percentage/100));
                                                    row.discount_amount = ((row.price_list_rate * row.qty) * (row.discount_percentage / 100));
                                                    // row.amount = (row.rate * row.qty) - (((row.price_list_rate*row.conversion_factor) * row.qty) * (row.discount_percentage/100));
                                                    row.amount = (row.rate * row.qty) - ((row.price_list_rate * row.qty) * (row.discount_percentage / 100));


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
                            })


                      }
                  }
              });


        }

        refresh_field("items");
    },
    item_code: function (doc, cdt, cdn) {
          let me = this;
        let row = frappe.get_doc(cdt, cdn);
        row.uom_select = row.stock_uom;
        row.uom = row.stock_uom;


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
                            console.log(r.message[0].discount_percentage);
                            row.discount_percentage = r.message[0].discount_percentage;


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