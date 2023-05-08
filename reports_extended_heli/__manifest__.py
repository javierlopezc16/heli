# -*- coding: utf-8 -*-
{
    'name': "Extensión de Reportes",

    'summary': """
        Módulo para mejoras de los reportes de Odoo""",

    'description': """
        Este módulo extiende los reportes de Odoo para incluir mejoras de Heli
    """,

    'author': "Javier López Castillo",
    'website': "https://nndeveloper.com",
    'version': '0.1',
    'depends': [
        'sale'
    ],
    'data': [
        'reports/sale_report.xml',
        'reports/sale_report_templates.xml',
        'views/res.company.xml',
    ],

}