from odoo import models, fields, api


class Payment(models.Model):
    _inherit = 'account.move'
    
    booking_id = fields.Many2one("hotel_management.booking", store=True)
    paymentdate = fields.Datetime(string="payment date", default = fields.Datetime.now, readonly=True, store=True)
    cust_id = fields.Char(string="Name", store=True)
    email = fields.Char(string='Email  ', store=True)
    contact = fields.Char(string="Contact", store=True)
    gender = fields.Char(string='Gender', store=True)  
    address = fields.Text(string='Address',store=True)
    checkin = fields.Datetime(string="Check In",store=True)
    checkout = fields.Datetime(string="Check Out",store=True)
    

    room_ids = fields.One2many('hotel_management.room_b','payment_id' ,string="Room Details ", store=True)
    spa_ids = fields.One2many('hotel_management.spa','payment_id',string='Spa Details',store=True)
    food_ids = fields.One2many('hotel_management.food_b','payment_id',string="Food Details ", store=True)

    Paymentmethod = fields.Selection([('public','online'),('privte','offline')],string="payment method", store=True)

    total_price = fields.Float(compute="_compute", string="Toatal Price", store=True)

    pending_amount = fields.Float(string="pending_amount", store=True)

    states = fields.Selection([
       ('paid','Paid'),
       ], string="states")

    def button(self):
        self.states = "paid"

    @api.depends('room_ids','spa_ids','food_ids')
    def _compute(self):
        for rec in self:
            if rec.room_ids or rec.spa_ids or rec.food_ids :
                rec.total_price = rec.room_ids.payment + rec.spa_ids.price + rec.food_ids.price 
            else:
                rec.total_price = 0
