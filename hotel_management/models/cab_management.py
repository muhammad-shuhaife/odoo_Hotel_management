import re
from odoo import models, fields, api 

class HotelCabManagement(models.Model):
    _name = "hotel_management.cab_m"
    _description = "Hotel Management's Cab Management"

# Fields ================================================================================================================================================

# "Cab Management" fields for "Cab details"
    name = fields.Char(string = "Number Plate", required = True)
    cab_m_company_name = fields.Char(string = "Company Name", required = True)
    cab_m_brand = fields.Char(string = "Cab's Brand", required = True)
    cab_m_capacity = fields.Char(string = "Cab's Capacity", required = True)
    # cab_availability = fields.Selection([("Available","Available",),("Not_Available","Not-Available")], string = "Availability", required = True, default = "Available")


# "Cab Management" fields for "Driver details"
    cab_m_driver_name = fields.Char(string = "Driver Name", required = True)
    cab_m_driver_aadhaar_no = fields.Char(string = "Aadhaar No.", required = True)
    cab_m_driver_contact_no = fields.Char(string = "Contact No.", required = True)
    cab_m_driver_address = fields.Char(string = "Address", required = True)




# Functions ================================================================================================================================================

# Function for validating the entered 'Cab's Capacity field value' is numeric or not =============
    @api.onchange('cab_m_capacity')
    def check_numeric_value(self):
        for rec in self:
            if not re.match('^[0-9]+$', rec.cab_m_capacity):
                rec.cab_m_capacity = False
                return {
                    'warning': {
                        'title': "Invalid Value",
                        'message': "Cab's Capacity must contain only numeric values!",
                    },
                }

# ===============================================================================================


# Function for validating the entered 'Cab Driver Name field value' is character value or not ============
    @api.onchange('cab_m_driver_name')
    def check_character_value(self):
        for rec in self:
            if not re.match('^[A-Za-z]+$', rec.cab_m_driver_name):
                rec.cab_m_driver_name = False
                return {
                    'warning': {
                        'title': "Invalid Value",
                        'message': "Cab's Driver Name must contain only character values!",
                    },
                }
    
# =======================================================================================================


# Function for validating 'Driver Aadhaar Number field' ==============================================================
    @api.onchange('cab_m_driver_aadhaar_no')
    def check_aadhaar_no(self):
        for rec in self:
            if not re.match('^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$',rec.cab_m_driver_aadhaar_no):
                rec.cab_m_driver_aadhaar_no = False
                return {
                    'warning': {
                        'title': "Invalid Cab's Driver Aadhaar Number",
                        'message': "Please check whether entered number is of 12 digits including white space after 4th digit!",
                    },
                }
            # if not rec.cab_m_driver_aadhaar_no.isdigit():
            #     rec.cab_m_driver_aadhaar_no = False
            #     return {
            #         'warning': {
            #                 'title': "Invalid Value",
            #                 'message': "Cab's Driver Aadhaar Number must contain only numeric values!",
            #             },
            #     }

            # if not re.match(r'^\d{12}$',rec.cab_m_driver_aadhaar_no):
            #     rec.cab_m_driver_aadhaar_no = False
            #     return {
            #         'warning': {
            #             'title': "Invalid Cab's Driver Aadhaar Number",
            #             'message': "PLease enter a 12 digit number!",
            #         },
            #     }

# ====================================================================================================================


# Function for validating 'Driver Contact Number field' ==============================================================
    @api.onchange('cab_m_driver_contact_no')
    def check_contact_no(self):
        for rec in self:
            if not re.match('^[6-9][0-9]{9}$',rec.cab_m_driver_contact_no):
                rec.cab_m_driver_contact_no = False
                return {
                    'warning': {
                        'title': "Invalid Value",
                        'message': "Invalid Cab's Driver Contact Number. PLease enter correct 10 digit number!",
                    },
                }

# ====================================================================================================================








# Below code is been replaced with above code ============================================================================================================

# class HotelCab(models.Model):
#     _name = 'hotel_management.cab'
#     _description = 'Hotel_Cab_Management'


#     cust_id = fields.Many2one('hotel_management.customer',string='Customer Name')
#     cab_id = fields.Integer(string="Cab No  ")
#     book_ids = fields.Integer(string="Booking Id  ")
#     car_type = fields.Selection([('bolero','Bolero'),('audi','Audi'),('bmw','BMW'),('kia','Kia'),('innova','Innova')],'Cab : ',default='bolero')
#     location1 = fields.Text(string="Drop Location ", default=" JW MARRIOTT" ,readonly="1")
#     name= fields.Char(string='Driver Name ')
#     contact = fields.Char(string='Cantact ')

#     contact1 = fields.Char(string='Customer Contact',related='cust_id.contact')
#     address1 = fields.Text(string='Pick-Up Location',related='cust_id.address')
#     booking_id = fields.Many2one('hotel_management.booking')


#     states = fields.Selection([
#         ('accept', 'Accept'),
#         ('reject', 'Reject'),
#     ], string="Status", default="accept")

#     def accept(self):
#         self.states = "accept"

#     def reject(self):
#         self.states = "reject"


