from openerp import models, fields, api
class NewModule(models.Model):
    _name = 'booking_booking_group'

    guest_name = fields.Char("Gest Name")
    room_no=fields.Integer("Room Number")
    booking_group= fields.Many2one(comodel_name="hotel_booking_room", string="booking_group", required=False, )
    nom=fields.Integer(string="Number",)