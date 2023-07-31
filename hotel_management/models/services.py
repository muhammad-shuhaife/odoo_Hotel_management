from odoo import models,fields,api

class Services(models.Model):
    _name = 'hotel_management.services'
    _description = "hotel_managemnt.services"

# Fields ================================================================================================================================================

# Fields of "Services" table
    name = fields.Char(string="Name", required=True)
    extra_cost = fields.Float(string="Extra Cost", required=True)

    