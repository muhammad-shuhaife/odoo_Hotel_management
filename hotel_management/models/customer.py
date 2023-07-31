import re
from odoo import models, fields, api , _
from odoo.exceptions import ValidationError


class HotelCustomer(models.Model):
    _name = 'hotel_management.customer'
    _description = 'Hotel Customer'
    _rec_name = 'name'

# Fields ================================================================================================================================================

# Fields of "Customer" table
    cust_id = fields.Integer(string="Cust Id  ")
    name = fields.Char(string="Name  ", required=True)
    email = fields.Char(string='Email  ', required=True)
    contact = fields.Char(string="Contact  ", required=True)
    alcontact = fields.Char(string="Alternate Contact ")
    gender = fields.Selection(string='Gender  ',
                                selection=[(' ',' '),('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default=' ',
                                required=True)
    address = fields.Text(string='Address  ', required=True)

    # Fields of other table (Room, Food, Spa, Event, Cab)
    booking_ids = fields.One2many('hotel_management.booking','cust_id')
    room_ids = fields.One2many('hotel_management.room_b', 'cust_id' ,string="Room Details ")
    food_ids = fields.One2many('hotel_management.food_b','cust_id',string="Food Details ")
    spa_ids = fields.One2many('hotel_management.spa','cust_id',string='Spa Details')
    event_ids = fields.One2many('hotel_management.event_b','cust_id',string='Event Details')
    cab_ids = fields.One2many('hotel_management.cab_b','cust_id',string='Cab Details')

    @api.constrains('email')
    def constrains_email(self):
        for record in self:
            if record.email:
                match = re.search('^[_A-Za-z0-9-]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*(\.[A-Za-z]{2,4})$',record.email)
                print("=============match======",match)
                if match == None:
                    raise ValidationError('Invalid Email')

    @api.constrains('contact')
    def _contact(self):
        for record in self:
            if record.contact:
                pattern = r'^[789]\d{9}$'
                if not re.match(pattern, record.contact):
                    raise models.ValidationError('Invalid Customer Contact Number!')

    @api.constrains('alcontact')
    def _validate_contact(self):
        for record in self:
            if record.alcontact:
                pattern = r'^[789]\d{9}$'
                if not re.match(pattern, record.alcontact):
                    raise models.ValidationError('Invalid Customer Alternate Contact Number!')






