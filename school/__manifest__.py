{
    'name':'School',
    'version': '1.1',
    'author': 'Weblearns',
    'summary': "School Management System",
    'sequence': 1,
    'description':"This is school management system software suppored in "
                  "Odoo v13",
    'category':'School',
    'website':'https://freeweblearns.blogspot.com',
    'depends':['base'],
    'data':[
        # "data/school_data.xml",
        "security/ir.model.access.csv",
        "views/school_view.xml",
        "views/marks.xml",
        # 'demo/school_demo_data.xml'
    ],
    # 'demo': ['demo/school_demo_data.xml']

}