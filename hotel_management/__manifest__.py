# -*- coding: utf-8 -*-
{
    'name': 'Hotel Management',
    'version': '1.1',
    'category': 'Management',
    'summary': 'Hotel Management',
    'sequence': '-100',
    'description': """
         This module contains all the common features of Hotel Management.
    """,

    # any module necessary for this one to work correctly

    'depends': ['base','website','account'],

    'data': [
        'security/hotel_security.xml',
        'security/ir.model.access.csv',

        
        

        'views/website_home.xml',   
        'views/website_our_hotel_views.xml',
        'views/website_room_views.xml',
        'views/website_contactus_views.xml',
        'views/website_hotel_fom_views.xml',
        'views/website_registration.xml',
        'views/website_checkavailability_views.xml',
        'views/website_list_room_views.xml',


        'views/amenities_management.xml',
        'views/booking.xml',
        'views/cab_booking.xml',
        'views/cab_management.xml',
        'views/customer.xml',
        'views/event_booking.xml',
        'views/event_management.xml',
        'views/food_booking.xml',
        'views/food_management.xml',
        'views/house_keeping.xml',
        'views/payment.xml',
        'views/room_booking.xml',
        'views/spa_views.xml',
        'views/room_management.xml',
        'views/spa_management.xml',        
        'views/staff_attendance.xml',       
        'views/staff.xml',
        'views/services_view.xml',
        'views/contract_views.xml',
        'views/menu_views.xml',
    ],
    

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application' : True,
}
