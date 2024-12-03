# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe import utils
from datetime import datetime, timedelta


@frappe.whitelist()
def update_status_close():
    """Called when Issue doctype is load"""
    ISSUE_STATUS = 'Esperando cierre'
    date = datetime.now()
    data = frappe.db.sql("""select name, DATEDIFF(%s, modified) as issue_modified_time from `tabIssue` where status = %s""", (date, ISSUE_STATUS), as_dict=True)
    close_issue_param = 3

    for issue in data:
        if issue.get('issue_modified_time') >= close_issue_param:
            """Update issue"""
            doc = frappe.get_doc("Issue", issue.get('name'))
            doc.status = "Closed"
            doc.flags.ignore_permissions = True
            doc.flags.ignore_mandatory = True
            doc.save()