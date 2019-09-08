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

@frappe.whitelist()
def filter_uom(doctype, txt, searchfield, start, page_len, filters):
    print "*****************filter_uom......."
    uoms = frappe.db.sql("""SELECT uom FROM `tabUOM Conversion Detail` WHERE parent=%s""",(filters.get("item")))

    print uoms

    return uoms

@frappe.whitelist()
def filter_uom(item):
    print "*****************filter_uom......."
    uoms = frappe.db.sql("""SELECT uom FROM `tabUOM Conversion Detail` WHERE parent=%s""",(item))

    print uoms

    return uoms

@frappe.whitelist()
def filter_uom_rate(item,uom):
    print "*****************filter_uom......."
    uoms = frappe.db.sql("""SELECT conversion_factor FROM `tabUOM Conversion Detail` WHERE parent=%s AND uom=%s""",(item,uom))

    print uoms
    if uoms:
        return uoms[0][0]
    else:
        return None