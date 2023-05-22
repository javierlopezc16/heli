# -*- coding: utf-8 -*-
{
    'name': "Heli Permisos de Accesos",

    'summary': """
        """,

    'description': """
        No permite modificar precio de venta ni descuentos en pedido de venta
    """,

    'author': "Javier López",
    'website': "http://nndeveloper.com",
    'category': 'Retail',
    'version': '16.0.1',
    'depends': [
        'base',
        'product',
        'sale',
    ],

    'data': [
        'data/data.xml',
        'views/product.product.xml',
        'views/product.template.xml',
        'views/sale.order.xml',
        
        
    ],
    'license': 'LGPL-3',
}
