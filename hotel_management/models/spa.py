from odoo import models, fields, api


class HotelSpa(models.Model):
    _name = 'hotel_management.spa'
    _description = 'hotel_management spa'

    spa_id = fields.Integer(string='Spa Id ')
    cust_id = fields.Many2one('hotel_management.customer',string='cust')

    name=fields.Many2one("hotel_management.spa_m",string="Spa Name")
    
    price = fields.Float(compute="_compute",string='Price', required=True)

    date=fields.Date(string='Preferred Date',required=True)
    schedule_time= fields.Selection([('_15 minute','15 minute'),
                             ('_30 minute','30 minute'),
                             ('_45 minute','45 minute'),
                             ('_1 hr','1 hr'),
                             ('_1.5 hr','1.5 hr'),
                             ('_2 hr','2 hr')
                             ],string='Scheduled time', required=True)
    booking_id = fields.Many2one('hotel_management.booking')

    payment_id = fields.Many2one('account.move')  
 


    @api.depends('name')
    def _compute(self):
        for rec in self:
            if rec.name:
                rec.price = rec.name.price
            else:
                rec.price = 0

    





  


