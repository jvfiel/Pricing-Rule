import frappe

@frappe.whitelist()
def get_pricing(item,uom):
    pricing_rule = frappe.db.sql("""SELECT * FROM `tabPricing Rule`
                                WHERE item_code=%s AND uom=%s""",(item,uom),as_dict=True)

    frappe.db.sql("""UPDATE `tabPricing Rule` SET priority = '' WHERE item_code=%s AND uom != %s""",(item,uom))

    frappe.db.sql("""UPDATE `tabPricing Rule` SET priority = '1' WHERE item_code=%s AND uom = %s""",(item,uom))

    frappe.db.commit()

    return pricing_rule
