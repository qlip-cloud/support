# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe import utils
from datetime import datetime, timedelta


@frappe.whitelist()
def update_status_close(**args):
    """Called when Issue doctype is load"""
    ISSUE_STATUS = args.get('issue_status')
    CLOSE_ISSUE_PARAM = int(args.get('expiration_days'))
    
    date = datetime.now()
    data = frappe.db.sql("""select name, DATEDIFF(%s, modified) as issue_modified_time from `tabIssue` where status = %s""", (date, ISSUE_STATUS), as_dict=True)

    ISSUE_STATUS = ISSUE_STATUS if ISSUE_STATUS else 'Esperando cierre'
    CLOSE_ISSUE_PARAM = CLOSE_ISSUE_PARAM if CLOSE_ISSUE_PARAM else 3

    for issue in data:
        if issue.get('issue_modified_time') > CLOSE_ISSUE_PARAM:
            """Update issue"""
            doc = frappe.get_doc("Issue", issue.get('name'))
            doc.status = "Closed"
            doc.flags.ignore_permissions = True
            doc.flags.ignore_mandatory = True
            doc.save()