from odoo import models, fields, api

class RoomType(models.Model):
    _name = "hotel_management.roomtype"
    _description = "room.type"

    image= fields.Binary(string="Room Image",required=True)
    name = fields.Char(string="Name", required=True)
    room_no = fields.Integer(string="room No",required=True)
    no_beds = fields.Integer(string="No of Beds")
    price = fields.Float(string="Price", required=True)
    guest = fields.Integer(string="Guest",required=True)


