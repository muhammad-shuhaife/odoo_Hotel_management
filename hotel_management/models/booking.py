from odoo import models, fields, api


class HotelBooking(models.Model):
    _name = 'hotel_management.booking'
    _description = 'Hotel Booking'
    _rec_name = 'cust_id'

# Fields ================================================================================================================================================

# Fields of "Customer" table
    cust_id = fields.Many2one('hotel_management.customer')
    booking_id = fields.Char(string='Book Id')
    name = fields.Char(string="Name  ",related='cust_id.name')
    email = fields.Char(string='Email  ',related='cust_id.email')
    contact = fields.Char(string="Contact  ",related='cust_id.contact')
    alcontact = fields.Char(string="Alternate Contact  ",related='cust_id.alcontact')
    gender = fields.Selection(string='Gender ',related='cust_id.gender')
    address = fields.Text(string='Address  ',related='cust_id.address')
    checkin = fields.Date(string="Check In  ")
    checkout = fields.Date(string="Check Out  ")
    invoice_id = fields.Many2one("account.move")
    

# Fields of other table (Room, Food, Spa, Event)
    # room_ids = fields.One2many('hotel_management.room_b', 'availability' ,string="Room Details ")
    # food_ids = fields.One2many('hotel_management.food_b','name',string="Food Details ")
    # spa_ids = fields.One2many('hotel_management.spa_b','spa_b_schedule_time',string='Spa Details')
    # event_ids = fields.One2many('hotel_management.event_b','venue',string='Event Details')  
    # cab_details = fields.Many2many("hotel_management.cab_b", string = "Cab Details")
    # cab_details = fields.One2many('hotel_management.cab_b','cab_details',string='Cab Details')

    # payment_ids = fields.One2many('account.move', 'cust_id',string="Bank Details ")
    

    room_ids = fields.One2many('hotel_management.room_b', 'booking_id' ,string="Room Details ")
    spa_ids = fields.One2many('hotel_management.spa','booking_id',string='Spa Details')
    food_ids = fields.One2many('hotel_management.food_b','booking_id',string="Food Details ")
    event_ids = fields.One2many('hotel_management.event_b','booking_id',string='Event Details')
    cab_ids = fields.One2many('hotel_management.cab_b','booking_id',string='Cab')
    # payment_ids = fields.One2many('account.move', 'booking_id',string="Bank Details ")
    
    total_price = fields.Float(compute="_compute")

    pending_amount = fields.Float(related="room_ids.balance")
    



    @api.depends('room_ids','spa_ids','food_ids','event_ids')
    def _compute(self):
        for rec in self:
            if rec.room_ids or rec.spa_ids or rec.food_ids or rec.event_ids:
                rec.total_price = rec.room_ids.payment + rec.spa_ids.price + rec.food_ids.price + rec.event_ids.price
            else:
                rec.total_price = 0
    
# Field for state of an booking application
    state = fields.Selection([
         ('confirm','Confirmed'),
         ('create_invoice','Created Invoice'),
    ], string="status")


    def action_confirm(self):
        self.state = "confirm"



    def action_invoice(self):
        self.state = "create_invoice"    
        inv = self.env['account.move'].create({
            'cust_id': self.cust_id.name,
            'email': self.email,
            'contact': self.contact,
            'gender': self.gender,
            'address': self.address,
            'checkin': self.checkin,
            'checkout': self.checkout,
            'room_ids': self.room_ids,
            'spa_ids' : self.spa_ids,
            'food_ids': self.food_ids,
            'total_price':self.total_price,
            'pending_amount' : self.pending_amount,
            'move_type':'out_invoice',
        })
        self.invoice_id = inv
        # return{
        #     'type':'ir.actions.act_window',
        #     'name':'Invoice',
        #     'res_model':'account.move',
        #     'domain':[('booking_id','=',inv.id)],
        #     'view_mode':'tree,form',
        #     'target':'current',
        #     }
    

# Functions ==================================================================================================================================================


    @api.onchange('cust_id')
    def hotel_booking(self):
        self.email=self.cust_id.email
        self.contact=self.cust_id.contact
        self.alcontact=self.cust_id.alcontact
        self.gender=self.cust_id.gender
        self.address=self.cust_id.address
            # self.checkin=self.cust_id.checkin
            # self.checkout=self.cust_id.checkout
#
            



