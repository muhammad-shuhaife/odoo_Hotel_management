from odoo import models, fields, api

class FoodManagement(models.Model):
    _name = 'hotel_management.food_m'
    _description = "Hotel Management's Food Management"
    
# Fields ================================================================================================================================================

# Fields of "Food Management" table
    food_id = fields.Char(string='Food id')
    name = fields.Char(string='Food Name',required=True)
    category = fields.Selection ([('1', 'Appetizers'), ('2', 'Soups'),('3', 'Main Courses'), 
                                ('4', 'Desserts'),('5', 'Breakfast'), ('6', 'Brunch'),('7', 'Snacks')], string='Category')
    type1 = fields.Selection([('1', 'Veg'), ('2', 'Non-veg')], string='Food Type')
    description =fields.Text(string="Food description") 
    price = fields.Float(string='Price',required=True)








