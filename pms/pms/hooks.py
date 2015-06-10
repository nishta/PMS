# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "pms"
app_title = "Pms"
app_publisher = "Nishta"
app_description = "PMS"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@nishta.in"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pms/css/pms.css"
# app_include_js = "/assets/pms/js/pms.js"

# include js, css files in header of web template
# web_include_css = "/assets/pms/css/pms.css"
# web_include_js = "/assets/pms/js/pms.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pms.install.before_install"
# after_install = "pms.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pms.notifications.get_notification_config"

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
# 		"pms.tasks.all"
# 	],
# 	"daily": [
# 		"pms.tasks.daily"
# 	],
# 	"hourly": [
# 		"pms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pms.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pms.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pms.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pms.event.get_events"
# }

