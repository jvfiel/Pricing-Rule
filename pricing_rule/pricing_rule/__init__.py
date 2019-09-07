import frappe

@frappe.whitelist()
def get_pricing(item,uom,pricelist):

    item_group = frappe.db.sql("""SELECT item_group FROM `tabItem` WHERE item_code=%s""",(item))


    pricing_rule = frappe.db.sql("""SELECT * FROM `tabPricing Rule`
                                WHERE (item_code=%s OR item_group=%s)
                                AND uom=%s AND for_price_list=%s""",(item,item_group[0][0],uom,pricelist),
                                 as_dict=True)

    if pricing_rule != ():

        frappe.db.sql("""UPDATE `tabPricing Rule` SET priority = ''
                WHERE (item_code=%s OR item_group=%s)  AND uom != %s AND for_price_list=%s""",
                      (item,item_group[0][0],uom,pricelist))

        frappe.db.sql("""UPDATE `tabPricing Rule` SET priority = '1'
              WHERE (item_code=%s OR item_group=%s)  AND uom = %s AND for_price_list=%s""",
                      (item,item_group[0][0],uom,pricelist))

        frappe.db.commit()

    return pricing_rule
