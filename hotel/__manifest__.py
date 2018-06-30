# -*- coding: utf-8 -*-
{
    'name': "hotel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # For the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance', 'hr'],

    # always loaded
    'data': [

        'views/view.xml',
        'views/booking_tree.xml',
        'views/templates.xml',
        'views/menus.xml',
        'views/guestreport.xml',
        'views/group_booking.xml',
        'views/guest_reportform_templet.xml',
        'views/chach_date_booking.xml',
        'views/booking_report.xml',
        'views/booking_temp_rep.xml',
        'views/room_report.xml',
        'views/roomtemp_report.xml',
        'views/customer.xml',
        'views/rest.xml',
        'views/guest_reportform.xml',
        'views/kitchen_report.xml',
        'views/kitchen_reporttemplet.xml',

        'views/kitchen.xml',
        'views/company_profile.xml',
        'views/groupbooking_report.xml',
        'views/groupbooking_reporttemplat.xml',
        'views/wizeredgroupreport.xml',
        'views/company_report.xml',
        'views/company_reporttemplate.xml',

        'security/employee_perm.xml',

        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
