# -*- coding: utf-8 -*-

{
    'name': 'SAAS Repository Management',
    'summary': 'Manage Repositories.',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'website': "https://softwareescarlata.com/",
    'author': 'David Montero Crespo',
    'installable': True,
    'depends': [
        'base', 'se_repository_management', 'contract', 'saas'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/saas_db.xml',
    ],
    'application': False,
    'license': 'AGPL-3',

}
