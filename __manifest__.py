# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Finances domèstiques',
    'version': '12.0.1.0.0',
    'category': 'Extra tools',
    'summary': 'Finances domèstiques amb odoo',
    'sequence': 10,
    'description': 'Aplicació de dinances domèstiques amb odoo',
    'license': 'AGPL-3',
    'author': 'jordiisidrollobet',
    'depends': ['mail'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/grupmoviment.xml',
        'views/subgrupmoviment.xml',
        'views/detallmoviment.xml',
        'views/formapagament.xml',
        'views/caixa.xml',
        'views/moviment.xml',
        'reports/rpt_moviments.xml',
        'reports/reports.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
