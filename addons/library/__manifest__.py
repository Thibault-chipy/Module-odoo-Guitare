# -*- coding: utf-8 -*-
{
    'name': "Library",
    'summary': "Application de gestion de bibliothèque",
    'description': """
Application de gestion de bibliothèque.

Fonctionnalités initiales :
- Gestion des livres (Book)
- Vues liste/formulaire
- Recherche et filtres
    """,
    'author': "Thibault Chipy",
    'website': "https://yourcompany.com",
    'category': 'Services/Library',
    'version': '18.0.1.0.0',
    'depends': ['base', 'website'],  
    'application': True,
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png',
    ],  
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/library_menu.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
}
