from . import __version__ as app_version

app_name = "orc"
app_title = "orc"
app_publisher = "jhansi64"
app_description = "orc"
app_email = "jhansi.a64@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/orc/css/orc.css"
# app_include_js = "/assets/orc/js/orc.js"

# include js, css files in header of web template
# web_include_css = "/assets/orc/css/orc.css"
# web_include_js = "/assets/orc/js/orc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "orc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "orc.utils.jinja_methods",
#	"filters": "orc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "orc.install.before_install"
# after_install = "orc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "orc.uninstall.before_uninstall"
# after_uninstall = "orc.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# nosssstification_config = "orc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways
fixtures = [{"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Opportunity item-orc","Opportunity Item-column_break_aeclv",
		"Opportunity Item-rate_value","Opportunity Item-commission_type",
		"Opportunity Item-commission_section","Sales Partner-bank_details","Sales Partner-bank_details_section","Sales Partner-customer_name",
		"ORC List-pan_number","ORC List-sales_invoice_id","ORC List-contact_person","ORC List-workflow_state"

            ]
        ]
    ]},"Client Script","Property Setter"
]

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"orc.tasks.all"
#	],
#	"daily": [
#		"orc.tasks.daily"
#	],
#	"hourly": [
#		"orc.tasks.hourly"
#	],
#	"weekly": [
#		"orc.tasks.weekly"
#	],
#	"monthly": [
#		"orc.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "orc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "orc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "orc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["orc.utils.before_request"]
# after_request = ["orc.utils.after_request"]

# Job Events
# ----------
# before_job = ["orc.utils.before_job"]
# after_job = ["orc.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"orc.auth.validate"
# ]
