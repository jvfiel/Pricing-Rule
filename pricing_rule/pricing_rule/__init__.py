import frappe


@frappe.whitelist()
def get_price(item_code, price_list):
    template_item_code = frappe.db.get_value("Item", item_code, "variant_of")

    if price_list:
        price = frappe.get_all("Item Price", fields=["price_list_rate", "currency"],
                               filters={"price_list": price_list, "item_code": item_code})

        if template_item_code and not price:
            price = frappe.get_all("Item Price", fields=["price_list_rate", "currency"],
                                   filters={"price_list": price_list, "item_code": template_item_code})

        if price:
            # pricing_rule = get_pricing_rule_for_item(frappe._dict({
            #     "item_code": item_code,
            #     "qty": qty,
            #     "transaction_type": "selling",
            #     "price_list": price_list,
            #     "customer_group": customer_group,
            #     "company": company,
            #     "conversion_rate": 1,
            #     "for_shopping_cart": True,
            #     "currency": frappe.db.get_value("Price List", price_list, "currency")
            # }))
            #
            # if pricing_rule:
            #     if pricing_rule.pricing_rule_for == "Discount Percentage":
            #         price[0].price_list_rate = flt(
            #             price[0].price_list_rate * (1.0 - (flt(pricing_rule.discount_percentage) / 100.0)))
            #
            #     if pricing_rule.pricing_rule_for == "Rate":
            #         price[0].price_list_rate = pricing_rule.price_list_rate
            #
            # price_obj = price[0]
            # if price_obj:
            #     price_obj["formatted_price"] = fmt_money(price_obj["price_list_rate"], currency=price_obj["currency"])
            #
            #     price_obj["currency_symbol"] = not cint(frappe.db.get_default("hide_currency_symbol")) \
            #                                    and (frappe.db.get_value("Currency", price_obj.currency, "symbol",
            #                                                             cache=True) or price_obj.currency) \
            #                                    or ""
            #
            #     uom_conversion_factor = frappe.db.sql("""select	C.conversion_factor
				# 	from `tabUOM Conversion Detail` C
				# 	inner join `tabItem` I on C.parent = I.name and C.uom = I.sales_uom
				# 	where I.name = %s""", item_code)
            #
            #     uom_conversion_factor = uom_conversion_factor[0][0] if uom_conversion_factor else 1
            #     price_obj["formatted_price_sales_uom"] = fmt_money(price_obj["price_list_rate"] * uom_conversion_factor,
            #                                                        currency=price_obj["currency"])
            #
            #     if not price_obj["price_list_rate"]:
            #         price_obj["price_list_rate"] = 0
            #
            #     if not price_obj["currency"]:
            #         price_obj["currency"] = ""
            #
            #     if not price_obj["formatted_price"]:
            #         price_obj["formatted_price"] = ""

            return price[0]


@frappe.whitelist()
def get_pricing(item, uom, pricelist):
    item_group = frappe.db.sql("""SELECT item_group FROM `tabItem` WHERE item_code=%s""", (item))

    pricing_rule = frappe.db.sql("""SELECT * FROM `tabPricing Rule`
                                WHERE (item_code=%s OR item_group=%s)
                                AND uom=%s AND for_price_list=%s""", (item, item_group[0][0], uom, pricelist),
                                 as_dict=True)

    if pricing_rule != ():
        frappe.db.sql("""UPDATE `tabPricing Rule` SET priority = ''
                WHERE (item_code=%s OR item_group=%s)  AND uom != %s AND for_price_list=%s""",
                      (item, item_group[0][0], uom, pricelist))

        frappe.db.sql("""UPDATE `tabPricing Rule` SET priority = '1'
              WHERE (item_code=%s OR item_group=%s)  AND uom = %s AND for_price_list=%s""",
                      (item, item_group[0][0], uom, pricelist))

        frappe.db.commit()

    return pricing_rule


@frappe.whitelist()
def filter_uom(doctype, txt, searchfield, start, page_len, filters):
    print "*****************filter_uom......."
    uoms = frappe.db.sql("""SELECT uom FROM `tabUOM Conversion Detail` WHERE parent=%s""", (filters.get("item")))

    print uoms

    return uoms


@frappe.whitelist()
def filter_uom(item):
    print "*****************filter_uom......."
    uoms = frappe.db.sql("""SELECT uom FROM `tabUOM Conversion Detail` WHERE parent=%s""", (item))

    print uoms

    return uoms


@frappe.whitelist()
def filter_uom_rate(item, uom):
    print "*****************filter_uom......."
    uoms = frappe.db.sql("""SELECT conversion_factor FROM `tabUOM Conversion Detail` WHERE parent=%s AND uom=%s""",
                         (item, uom))

    print uoms
    if uoms:
        return uoms[0][0]
    else:
        return None
