{
    "name": """Custom Reports""",
    "summary": """This module have some custom reports of sale, purchase""",
    "category": "Reports",
    "images": [],
    "version": "13.0.1.0.0",
    "application": False,
    "depends": ["base", "product", "crm", 'account', 'sale', 'sale_management', 'purchase', 'globozor_admin', 'wh_crm_custom', 'wh_sale_custom'],
    "data": [
        
        'reports/report_templates/report_quotation.xml',
        'reports/report_templates/report_globozor_quotation.xml',
        'reports/report_templates/report_contract_sale.xml',
        'reports/purchase_order_report.xml',
    ],
    "demo": [],
    "installable": True,
}
