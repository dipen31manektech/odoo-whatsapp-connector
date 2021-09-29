{
    'name': 'Whatsapp Odoo Connector',
    'version': '14.0.0.1',
    'summary': 'Whatsapp Odoo Connector',
    'author': 'MT',
    'company': 'MT',
    'maintainer': 'MT',
    'images': ['static/description/Banner.png'],
    'sequence': 4,
    'license': 'OPL-1',
    'description': """Whatsapp Odoo Connector""",
    'category': 'Connector',
    'depends': [
        'base', 'contacts', 'sale', 'crm', 'stock', 'sale_management', 'account', 'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'models/whatsapp_template.xml',
        'views/whatsapp_button_views.xml',
        'wizard/whatsapp_wizard.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False
}
