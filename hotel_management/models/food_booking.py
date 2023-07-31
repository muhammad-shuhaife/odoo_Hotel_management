from odoo import models, fields, api


class HotelFood(models.Model):
    _name = 'hotel_management.food_b'
    _description = "Hotel Management's Food Booking"

# Fields ================================================================================================================================================

# Fields of "Food Booking" table
    food_id = fields.Many2one('hotel_management.food_m')
    cust_id = fields.Many2one('hotel_management.customer',string='Cust')
    # name = fields.Char(string='Food Name',required=True)
    name = fields.Many2one("hotel_management.food_m",string="Food Name")
    category = fields.Selection ([('1', 'Appetizers'), ('2', 'Soups'),('3', 'Main Courses'), 
                                ('4', 'Desserts'),('5', 'Breakfast'), ('6', 'Brunch'),('7', 'Snacks')], string='Category',readonly=True)
    type1 = fields.Selection([('1', 'Veg'), ('2', 'Non-veg')], string='Food Type',readonly=True)
    description =fields.Text(string="Food description",readonly=True) 
    spiciness_level = fields. Selection ([('1', 'Normal'), ('2', 'Medium'),('3', 'Spicy')], string='Spiciness Level')
    price = fields.Float(string='Price')
    
    booking_id = fields.Many2one('hotel_management.booking')

    payment_id = fields.Many2one('account.move')


 # Functions ==================================================================================================================================================

    # @api.depends('name')
    # def _compute(self):

    #     for rec in self:
    #         if rec.name:
    #             rec.price = rec.name.price
    #         else:
    #             rec.price = 0

    @api.onchange('food_id')
    def hotel_food(self):
        if self.food_id:
            self.category=self.food_id.category
            self.type1=self.food_id.type1
            self.description=self.food_id.description
            self.price=self.food_id.price
            