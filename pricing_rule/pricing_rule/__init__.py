import frappe

@frappe.whitelist()
def get_pricing(item,uom):
    pricing_rule = frappe.db.sql("""SELECT * FROM `tabPricing Rule` WHERE item_code=%s AND uom=%s""",(item,uom),as_dict=True)
    return pricing_rule
