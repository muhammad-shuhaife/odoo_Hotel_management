from odoo import models, fields, api

class AmenitiesManagement(models.Model):
    _name = "hotel_management.amenities_m"
    _description = "amenities"

# Fields ================================================================================================================================================

# Fields of "Amenities" table
    name= fields.Char(string="Name", required=True)
    price = fields.Float(string="Price",required=True)

