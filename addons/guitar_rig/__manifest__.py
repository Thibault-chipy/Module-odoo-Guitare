{
    'name': 'Guitar Rig',
    'description': "Application de gestion de matériel guitare, presets et sessions.",
    'version': '1.0',
    'summary': 'Gestion de matériel guitare, presets et sessions',
    'category': 'Services/GuitarRig',
    'license': 'LGPL-3',
    'application': True,
    'depends': ['base', 'web', 'website'],
    'images':[
        'static/description/icon.png',
    ],
    'data': [
        'security/guitar_rig_security.xml',
        'security/ir.model.access.csv',
        'views/guitarRig_menu.xml',
        'views/gear_views.xml',
        'views/session_views.xml',
        'views/partner_view.xml',
        'views/list_gear_templates.xml',
    ],

    'demo': [        
        'demo/demo_partnerFabricant.xml',
        'demo/demo_gear.xml',
        'demo/demo_session.xml',
    ],

}
