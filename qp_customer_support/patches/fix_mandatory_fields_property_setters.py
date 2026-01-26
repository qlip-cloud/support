import frappe

def execute():
  """
  Elimina los Property Setters que establecen los siguientes campos como obligatorios:
  - Contact: designation
  - Customer: Sales Team
  - Customer: Industry
  """

  mandatory_fields = [
    {"doctype": "Contact", "fieldname": "designation"},
    {"doctype": "Customer", "fieldname": "sales_team"},
    {"doctype": "Customer", "fieldname": "industry"},
  ]

  for field in mandatory_fields:
    ps = frappe.get_all(
      "Property Setter",
      filters={
        "doc_type": field["doctype"],
        "field_name": field["fieldname"],
        "property": "reqd",
        "value": "1"
      },
      pluck="name"
    )

    for name in ps:
      frappe.delete_doc("Property Setter", name)