{
    'name': "Biblioteca Comics Simple", 
    'summary': "Gestionar comics", 
    'description': """
        Gestor de bibliotecas (Version Simple)
        ==============
    """,  

    'application': True,
    'author': "Sergi García",
    'website': "http://apuntesfpinformatica.es",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_comic.xml'
    ],
}