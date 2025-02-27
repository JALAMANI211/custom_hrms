# Copyright (c) 2025, jalamani and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": _("Employee"),
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 200
        },
        {
            "label": _("Employee Name"),
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Training Type"),
            "fieldname": "training_type",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Trainer"),
            "fieldname": "trainer",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Duration (Hours)"),
            "fieldname": "duration",
            "fieldtype": "Float",
            "width": 200
        }
    ]

def get_data(filters):
    # Query to fetch employee training data
    query = """
        SELECT 
            et.employee,
            emp.employee_name,
            et.training_type,
            et.trainer,
            et.status,
            et.duration
        FROM 
            `tabEmployee Training Table` et
        LEFT JOIN 
            `tabEmployee` emp ON et.employee = emp.name
        WHERE 
            1=1
    """
    
    if filters and filters.get("employee"):
        query += f" AND et.employee = '{filters.get('employee')}'"
    
    if filters and filters.get("training_type"):
        query += f" AND et.training_type = '{filters.get('training_type')}'"
    
    if filters and filters.get("status"):
        query += f" AND et.status = '{filters.get('status')}'"
    
    data = frappe.db.sql(query, as_dict=1)
    return data