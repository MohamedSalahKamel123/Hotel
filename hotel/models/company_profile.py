from openerp import models, fields, api
import re
from openerp.exceptions import ValidationError

class NewModule(models.Model):
    _name = 'company.profile'
    # _rec_name = 'name'
    # _description = 'New Description'

    name = fields.Char(string='Name',required=True)
    food = fields.Selection(string="Food",
                            selection=[('We', 'Without Eating'), ('bl', 'Just breakfast + dinner'),
                                       ('bld', 'Just breakfast + lunch + dinner')], required=False, )
    conference_hall = fields.Selection(string="Conference Hall",
                                       selection=[('Small', '500 people'), ('large', '1000 people'), ],
                                       required=False, )
    wedding_hall = fields.Selection(string="Wedding Hall",
                                    selection=[('Small', '500 people'), ('Large', '1000 people'), ],
                                    required=False, )
    parking = fields.Boolean(string="Parking", )
    hotel_car = fields.Boolean(string="Use the hotel car", )

    gust_domend = fields.Many2one(comodel_name="guests_informations", string="Select Guest",)
    @api.multi
    def ccc(self):
        for x in self:
          obj = x.env['group_booking_rooms'].search([('company_name.id', '=', x.id)])



    address=fields.Char(string="Company Address", required=True )
    email=fields.Char(string="E-mail" )

    @api.constrains('email')
    def validate_email(self):
        for obj in self:

            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", obj.email) == None:
                raise ValidationError("Please Provide valid Email Address: %s" % obj.email)

            return True
    _sql_constraints = [

        ('email_uniq', 'unique(email)', 'Email id is unique change your custom email id'),
        # ('phone_uniq', 'unique(phone)', 'Phone id is unique change your custom Phone id'),

    ]
    _sql_constraints = [

        ('phone_unique', 'unique(phone)', 'Cant be duplicate phone number'),


    ]

    phone=fields.Char(string="Phone", )
    Make_reservation= fields.Boolean(string="Make reservation",readonly=True)

    guest_infor = fields.One2many(comodel_name="guests_informations", inverse_name="many_guest",
                                  string="Guests Informayions", )
    total=fields.Integer(string="Price",)
    # ===========================================================================

    night_nom = fields.Integer(string=" Duration",compute='getnight_nom')
    # @api.one
    def getnight_nom(self):
        obj1 = self.env['group_booking_rooms'].search([('company_name.id', '=', self.id)])
        # for x in obj1:
        self.night_nom=obj1.night_no

    pricsroom = fields.Float(string="Price For Rooms",compute='getpricsroom' )
    def getpricsroom(self):
        obj= self.env['group_booking_rooms'].search([('company_name.id', '=', self.id)])
        self.pricsroom=obj.total
    totalprice = fields.Float(string="Total Price",compute='gettotalprice' )
    def gettotalprice(self):
        obj= self.env['group_booking_rooms'].search([('company_name.id', '=', self.id)])
        self.totalprice=obj.total_price

    roomprice = fields.Many2one(comodel_name="group_booking_rooms",)



        # ========================================================================
    guestlist=fields.One2many(comodel_name="add.guests", inverse_name="guestget", )
class NewModule(models.Model):
    _name = 'guests_informations'
    # _rec_name = 'name'
    # _description = 'New Description'

    name = fields.Char(string='Name')
    id_gest = fields.Integer(string="Guest ID", )
    room = fields.Many2one(string="Room Number", comodel_name='room_hotelmanagement',
                           domain=lambda self: [('state', '=', False)])
    pr=fields.Integer(reiated='room.pirce')
    many_guest = fields.Many2one(comodel_name="group_booking_rooms", )

class NewModule(models.Model):
        _name = 'add.guests'
        # _rec_name = 'name'
        # _description = 'New Description'
        #
        name = fields.Char(string='Name')
        id_identification=fields.Char(string="ID",)
        phone=fields.Char(string="Phone",)
        guestget = fields.Many2one(comodel_name="company.profile",)