# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HotelEvent(models.Model):
    _name = 'hotel_management.event_b'
    _description = "Hotel_Management's Event_Booking"

# Fields ================================================================================================================================================

# Fields of "Event Booking" table
    name_id = fields.Many2one('hotel_management.event_m',string='Event Type')
    venue = fields.Selection([('conference_room','Conference Room'),
                                ('banquet_hall','banquet Hall'),
                                ('outdoor_spaces','Outdoor Spaces')
                                ],string='Event Venue',required=True)
    name = fields.Selection([('marriage','Marriage'),
                            ('birthday','Birthday'),
                            ('conference','Conference')
                            ],string='Event Type',required=True)
    attendees =fields.Selection([('1','30'),('2','50'),('3','100'),('4','200'),('5','500')])
    description = fields.Text (string="Description",readonly=True)
    staff_id = fields.Many2one('hotel_management.staff',string='Event Manager',required=True)
    contact = fields.Char(related='staff_id.work_mobile',string='Contact No',readonly=True)
    price = fields.Float(related='name_id.price',string='Price',required=True)
    cust_id = fields.Many2one('hotel_management.customer')
    booking_id = fields.Many2one('hotel_management.booking')


# Functions ==================================================================================================================================================

    @api.onchange('name_id')
    def hotel_event(self):
        if self.name_id:
            self.attendees=self.name_id.attendees
            self.description=self.name_id.description
            self.staff_id=self.name_id.staff_id
            self.contact=self.name_id.contact
            self.price=self.name_id.price
            

    



