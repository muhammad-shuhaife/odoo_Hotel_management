from odoo import models, fields, api

class HouseKeeping(models.Model):
    _name = 'hotel_management.housekeeping'
    _description = 'HouseKeeping'

# Fields ================================================================================================================================================

# Fields of "House Keeping" table
    name = fields.Char(string="Name", default="Spotless Cleaning Services", readonly=True)
    extra_cost = fields.Float(string="Extra Cost", required=True)
    services_id = fields.Many2one("hotel_management.services", string="Services",store=True, required=True)
    extra_cost = fields.Float(compute="_compute", string="Extra Cost", required=True)
    room_id = fields.Many2one("hotel_management.room_b", string="Room No",required=True)
    cust_id = fields.Many2one('hotel_management.customer', string="Customer Name")
    staff_name_id= fields.Many2one("hotel_management.staff",string="Staff", required=True)



# Functions ==================================================================================================================================================

    @api.depends('services_id')
    def _compute(self):
        for record in self:
            if record.services_id:
                record.extra_cost = record.services_id.extra_cost

            else:
                record.extra_cost = 0    


    


