import frappe
from frappe import _

@frappe.whitelist()
def get_employee_training(employee_id):
    if not employee_id:
        return {"error": _("Employee ID is required")}

    trainings = frappe.get_all(
        "Employee Training Table",
        filters={"employee": employee_id},
        fields=["employee", "training_type", "trainer", "training_date", "duration", "status"]
    )
    frappe.local.response["training details"] = trainings