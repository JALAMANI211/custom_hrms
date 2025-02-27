// Copyright (c) 2025, jalamani and contributors
// For license information, please see license.txt

// custom_hrms/custom_hrms/report/training_summary/training_summary.js
frappe.query_reports["Training Summary"] = {
    "filters": [
        {
            "fieldname": "employee",
            "label": __("Employee"),
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
            "fieldname": "training_type",
            "label": __("Training Type"),
            "fieldtype": "Select",
            "options": "\nTechnical\nSoft Skills\nCompliance"
        },
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": "\nPlanned\nOngoing\nCompleted"
        }
    ]
};