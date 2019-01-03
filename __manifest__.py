# -*- coding: utf-8 -*-
{
    'name': "Calculate Unbuild Percentage",
    'summary': """Put short summary here.""",
    'description': '',
    'author': "Linksoft Mitra Informatika",
    'website': "https://linksoft.id",
    # Check here: https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/module/module_data.xml
    'category': 'Uncategorized',
    'version': '1.0.0',
    'depends': [
        # odoo addons
        'base',
        # third party addons

        # developed addons
        'ls_odoo_process_costing_manufacturing_patch',
    ],
    # always loaded
    'data': [
        # group

        # data

        # action

        # view
        'views/view_mrp_bom.xml',
        # wizard

        # action menu

        # menu

        # security
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}