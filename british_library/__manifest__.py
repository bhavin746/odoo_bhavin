# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Library Management',
    'version' : '14.0.1',
    'summary': 'Library Management Software',
    'sequence': -100,
    'description': """Library Management Software""",
    'category': 'Library',
    'website': 'https://www.erpharbor.com',
    'depends' : ['website','mail','base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/student_update_view_wizard.xml',
        'wizard/create_book_view_wizard.xml',
        'report/report_library_transaction.xml',
        'views/student_library.xml',
        'views/book_library.xml',
        'views/author_library.xml',
        'views/transaction_library.xml',
        'views/book.xml',
        'views/interestbook_library.xml',
        'views/template.xml',
        'views/website_form.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
