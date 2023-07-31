from odoo import models, fields, api

class HotelSpaManagement(models.Model):
    _name = 'hotel_management.spa_m'
    _description = "Hotel management's Spa Management"

# Fields ========================================================================

# Fields of "Spa Management" table
    name = fields.Char(string = 'Spa Facility Name', required = True)
    spa_m_description = fields.Text(string = 'Description', required = True)
    price = fields.Float(string = 'Price', required =True)