from odoo import http
from odoo.http import request
from datetime import datetime




class Home(http.Controller):
    @http.route(['/'], type='http', auth='public', website=True)
    def home(self):
        return http.request.render('hotel_management.home',{})



class OurHotel(http.Controller):
    @http.route(['/ourhotel'], type='http', auth='public', website=True)
    def ourhotel(self):
        return http.request.render('hotel_management.our_hotel')



# class Event(http.Controller):
#     @http.route(['/events'], type='http', auth='public', website=True)
#     def event(self):
#         return http.request.render('hotel_management.event',{})


class Room(http.Controller):
    @http.route(['/room'], type='http', auth='public', website=True)
    def room(self):
        return http.request.render('hotel_management.room',{})



class Customer(http.Controller):
    @http.route(['/registration'], type='http', auth='public', website=True)
    def customer(self,**kw):
        return http.request.render('hotel_management.registration',{})


    @http.route(['/customer'], type='http', auth='public', website=True)
    def create_customer(self,**kw):
        request.env['hotel_management.customer'].sudo().create(kw)
        return http.request.render('hotel_management.customer_thanks',{})



class CheckAvailable(http.Controller):
    @http.route(['/checkavailable'], type='http', auth='public', website=True)
    def check(self,**kwargs):
        # room_rec=request.env['hotel_management.roomtype'].search([])
       
        return http.request.render('hotel_management.checkavailable_room',{})




class ListRoom(http.Controller):
    @http.route('/listroom', website=True, auth='public' ,type='http')
    def listroom(self, **kwargs):
        
        check_in = kwargs.get('check_in')
        check_out = kwargs.get('check_out')
        guest = kwargs.get('guest')
        print('#######',kwargs)
        
        room_model = request.env['hotel_management.room_b']
        available_rooms = room_model.search([
            ('check_out', '>=', check_in),
            ('check_in', '<=', check_out),
            # ('room_type_id.id', '=', room_type_id),
        ])
        print('#########',available_rooms)
        if len(available_rooms) == 0:
            check=request.env['hotel_management.roomtype'].search([('guest','>=',guest)])
            print('#########',check)
        else:
            check = False
            for rec in available_rooms:
            
                    check=request.env['hotel_management.roomtype'].search([('id','!=',rec.room_type_id.id),('guest','>=',guest)])
                    print('#########',check)
        
        
        
        return request.render('hotel_management.listroom',{
            'check':check,'check_in':check_in,'check_out':check_out
        })

        

class Booking(http.Controller):
    @http.route(['/booking'], type='http', auth='public', website=True)
    def booking(self,**kw):
        print('#######',kw)
        check_in=kw.get('check_in')
        check_out=kw.get('check_out')
        room=kw.get('roomid')
        cust_rec=request.env['hotel_management.customer'].search([])
        room_rec=request.env['hotel_management.roomtype'].search([('id','=',room)])
        amenities_rec=request.env['hotel_management.amenities_m'].search([])
        return http.request.render('hotel_management.booking_room',{'cust_rec':cust_rec,'room_rec':room_rec,'amenities_rec':amenities_rec,'check_in':check_in,'check_out':check_out})

    @http.route(['/bookingroom'], type='http', auth='public', website=True)
    def booking_room(self,**kw):
        val = request.env['hotel_management.customer'].search([('id','=',kw.get('cust_id'))])
        

        rec = request.env['hotel_management.booking'].sudo().create({'cust_id':kw.get('cust_id'),'email':val.email,'address':val.address,'contact':val.contact,'gender':val.gender,'checkin':(kw.get('check_in')),'checkout':(kw.get('check_out')),
            'room_ids': [(0, 0, {'room_type_id': int(kw.get('room_type_id')),'check_in':(kw.get('check_in')),'check_out':(kw.get('check_out')),'amenities_ids': [(6,0,[int(kw.get('amenities_ids'))])],'payment_type': (kw.get('payment_type'))})]
            

        })
        
       
        return http.request.render('hotel_management.booking_thanks',{})





class Contactus(http.Controller):
    @http.route(['/contactus'], type='http', auth='public', website=True)
    def contactus(self):
        return http.request.render('hotel_management.contact_us',{})







