from openerp import models, fields, api
from datetime import date

class NewModule(models.Model):
    _name = 'room_hotelmanagement'
    _rec_name = 'room_no'
    name=fields.Selection(string="Name", selection=[('r', 'Standard Room'), ('s', 'Suite'), ], required=True, )
    image = fields.Binary()
    room_no=fields.Integer("Room Number",required=True)
    room_type=fields.Selection(string="Room Type", selection=[('s', 'Stander Room (1 to 2 person)'), ('f', 'Family Room (1 to 4 person)'),('p', 'Private Room (1 to 3 person)'),('m', 'Mix Dorm Room (6 person)'),('f', 'Female Dorm Room (6 person)'),('m', 'Male Dorm Room (6 person)'), ], required=False, )
    room_view=fields.Selection(string="", selection=[('s', 'street'), ('p', 'Swimming pool'),('n', 'Nothing'), ], required=False, )
    price= fields.Float(string="Price",required=True, )
    reserv = fields.Many2one(comodel_name="hotel_booking_room")
    state = fields.Boolean(string="Reserved",default=False,readonly=True)
    floor=fields.Selection(string="Floor", selection=[('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5') ], required=True, )
    notes=fields.Char(string="Notes", required=False, )


    _sql_constraints = [
        ('room_no_unique', 'unique(room_no)', 'Cant be duplicate Room number'),
    ]



