{
    'name' : 'Vote Management',

    'description' : """
        Sistema de votaciones
    """,

    'author': "Gustavo",
    'website': "http://localhost",
    'category': 'Education',
    'version': '0.1',
    'apllication': True,
    'installable': True,
    'depends': ['base'],

    'data': [
        'data/security/ir.model.access.csv',
        'data/views/menu_view.xml',
        'data/views/university_campus_form_view.xml',
        'data/views/university_campus_list_view.xml',
        'data/views/inherit_res_partner_form_view.xml',
        'data/views/inherit_res_partner_list_view.xml'
    ],

    'assets': {
        'web.assets_backend': [
            'uniacme/static/src/**/*'
        ]
    },
    'license': 'AGPL-3'
}