# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pricing_rule"
app_title = "Pricing Rule"
app_publisher = "John Vincent Fiel"
app_description = "Pricing Rule based on UOM"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "johnvincentfiel@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pricing_rule/css/pricing_rule.css"
# app_include_js = "/assets/pricing_rule/js/pricing_rule.js"

# include js, css files in header of web template
# web_include_css = "/assets/pricing_rule/css/pricing_rule.css"
# web_include_js = "/assets/pricing_rule/js/pricing_rule.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Sales Invoice": "public/js/si.js",
    "Sales Order": "public/js/so.js"
    # "Purchase Order": "public/js/purchase_order.js",
    # "Production Order": "public/js/production_order.js",
    # "Production Planning Tool": "public/js/production_planning_tool.js",
    # "BOM": "public/js/bom.js",
    # "Stock Entry": "public/js/stock_entry.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pricing_rule.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pricing_rule.install.before_install"
# after_install = "pricing_rule.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pricing_rule.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pricing_rule.tasks.all"
# 	],
# 	"daily": [
# 		"pricing_rule.tasks.daily"
# 	],
# 	"hourly": [
# 		"pricing_rule.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pricing_rule.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pricing_rule.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pricing_rule.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pricing_rule.event.get_events"
# }

fixtures = ["Custom Script"]