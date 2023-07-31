from odoo import models, fields, api

class HotelEventtype(models.Model):
    _name = 'hotel_management.event_m'
    _description = "Hotel_Management's Event_Management"
    _rec_name = 'venue'
    
# Fields ================================================================================================================================================

# Fields of "Event Management" table
    name_id = fields.Integer(string="Event Id  ")
    venue = fields.Char(string='Event Venue',required=True)
    attendees =fields.Integer(string="Attendees")
    description = fields.Text (string="Description")
    staff_id = fields.Many2one('hotel_management.staff',string='Event Manager',required=True)
    contact = fields.Char(related='staff_id.work_mobile',string='Contact No')
    price = fields.Float(string='price',required=True)
    # price = fields.Float(related='name_id.price',string='Price',required=True)