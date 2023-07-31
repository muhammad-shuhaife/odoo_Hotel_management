from odoo import models, fields, api 

class HotelCabBooking(models.Model):
    _name = "hotel_management.cab_b"
    _description = "Hotel Management's Cab Booking"
    _rec_name = "cab_b_booking_date"
    # _inherit = "hotel_management.cab_management"


# Fields ================================================================================================================================================

# Fields of "Cab Booking" table (It will hold the Booking ID)
    booking_id = fields.Many2one('hotel_management.booking')

# Fields of "Customer" table
    cust_id = fields.Many2one('hotel_management.customer')

# Fields of "Cab Booking" table
    cab_b_booking_date = fields.Datetime(string = "Booking Date", default = fields.Date.today(), required = True,)
    cab_b_drop_off_location = fields.Char(string = "Drop-Off Location", required = True)

# Fields of "Cab Management" table

    # Fetching all the fields value from "Cab Management" model
    no_of_cab_booked = fields.Many2many("hotel_management.cab_m", string = "No. of Cab Booked", )



# Functions ==================================================================================================================================================

# Function for fetching unique value from "cab management's cab_m_capacity" 
    # def fetch_unique_values_of_capacity(self):
    #     cab_management_obj = self.env["hotel_management.cab_m"]
    #     cab_details = cab_management_obj.search([]).mapped("cab_m_capacity")
    #     self.cab_details = [(0, 0, {"cab_m_capacity": value}) for value in set(cab_details)]
