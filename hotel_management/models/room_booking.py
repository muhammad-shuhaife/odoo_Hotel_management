from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class HotelRoomBooking(models.Model):
    _name = 'hotel_management.room_b'
    _description = "Hotel Management's Room Booking"
    _rec_name = "room_no"


# Fields ================================================================================================================================================

# Fields of "Room Booking" table
    booked_date = fields.Datetime(string="Booked_Time", default = fields.Datetime.now, readonly=True)

    check_in = fields.Date(string="Check In",required=True)

    check_out = fields.Date(string="Check Out", required = True)

    cust_id = fields.Many2one('hotel_management.customer', string='Cust')

    availability = fields.Char(string="Status", compute="check_availability")

    price = fields.Float(compute="_compute", string="Price", required=True)


    room_type_id = fields.Many2one("hotel_management.roomtype",string="Room Type",required=True, store=True)

    room_no = fields.Integer(string='Room No')

    no_beds = fields.Integer(string="No of Beds")
    amenities_ids = fields.Many2many("hotel_management.amenities_m", store=True)    
    amenities_name = fields.Char(string="amenities",compute="_amenities")
    payment_type = fields.Selection([('advance1','Advance Payment (10%)'),
                                    ('advance','Advance Payment (50%)'),
                                    ('full','Full Payment'),
                                    ],string="Payment Option",required=True)
    


    payment = fields.Float(compute="_advance",string="Payment Amount",required=True)
 
    balance = fields.Float(compute="_balance",string="pending Amount")
  
    booking_id = fields.Many2one('hotel_management.booking')  

    payment_id = fields.Many2one('account.move')  


# Functions ==================================================================================================================================================


    @api.onchange('room_type_id')
    def _onchange_room_type(self):
        
        self.room_no = self.room_type_id.room_no
        self.no_beds = self.room_type_id.no_beds    
    


    @api.depends('payment_type','price','payment')
    def _balance(self):
        for rec in self:
            if rec.payment_type == 'advance1':
                rec.balance = rec.price - rec.payment
            elif rec.payment_type == 'advance':
                rec.balance = rec.price - rec.payment
            else:
                rec.balance = 0        



    @api.depends('amenities_ids')
    def _amenities(self):
        for record in self:
            record.amenities_name  = ', '.join(record.amenities_ids.mapped('name'))
            

    @api.depends('room_type_id', 'amenities_ids', 'check_in', 'check_out')
    def _compute(self):
        for record in self:
            if record.room_type_id or record.amenities_ids:
                if record.check_in and record.check_out:
                    check_in_date = fields.Datetime.from_string(record.check_in)
                    check_out_date = fields.Datetime.from_string(record.check_out)
                    num_days = (check_out_date - check_in_date).days
                    record.price = record.room_type_id.price * num_days
                    record.price  = record.price + sum(record.amenities_ids.mapped('price'))
                    if record.check_in == record.check_out:
                        record.price = record.room_type_id.price
                else:
                    record.price = record.room_type_id.price
            else:
                record.price = 0




    @api.depends('check_out','check_in', 'room_type_id')
    def check_availability(self):
        for rec in self:

            avaliable = self.env['hotel_management.room_b'].search([('check_out','>=',rec.check_in),('check_in', '<=', rec.check_out), ('room_type_id', '=', rec.room_type_id.id)])

            if avaliable:
                rec.availability = "Booked (Un Availiable)"
                rec.room_no = rec.room_no
                # raise ValidationError('The room is not available for the selected dates. Please choose different dates.')
            else:
                rec.availability = "Availiable"
                rec.room_no = rec.room_no
                   

    @api.depends('price', 'payment_type')
    def _advance(self):
        for rec in self:
            if rec.payment_type == 'full':
                rec.payment = rec.price
            elif rec.payment_type == 'advance':
                rec.payment = (50*rec.price)/100
            elif rec.payment_type == 'advance1':
                rec.payment = (10*rec.price)/100    
            else :
                rec.payment = 0     







