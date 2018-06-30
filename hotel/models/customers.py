from openerp import models, fields, api
from datetime import datetime
from datetime import date
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning


class NewModule(models.Model):
    _name = 'customers_profile'
    _rec_name = 'name'
    image = fields.Binary(string="Image")
    name = fields.Char(string="Name",required=True )
    first_name = fields.Char(string="First Name", )
    last_name = fields.Char(string="Last Name", )
    birth_of_date = fields.Date(string="Birth Of Date", )
    address = fields.Char(string="Address", )
    phone = fields.Integer(string='Phone Number', )
    identification_id = fields.Char(string="Identification No ", )
    passport_id = fields.Char(string="Passport No ", )
    gender = fields.Selection(string="Gender ", selection=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')],
                              )

    marital = fields.Selection(string="Marital Status",
                               selection=[('s', 'Single'), ('m', 'married'), ('w', 'Widower'), ('d', 'divorced')],
                               )
    notes = fields.Char()
    state = fields.Selection(string="Nationality", selection=[('e', 'Egyption'), ('f', 'Forigen'), ], default='e')
    age = fields.Char(string="Age",compute='get_age')
    # =============================================================================
    reser_Id = fields.Many2one(comodel_name="hotel_booking_room")
    # filo2 = fields.Char(string="Reservation number")
    room_no = fields.Char(string="Room Number", compute='rooms_numbers')
    night_price = fields.Float(string="Room Price", compute='roomprice')
    days_no = fields.Integer(string='Days Number', compute='days_number')
    total_price = fields.Float(string='Total Price', compute='total_priceroom')
    paid_money = fields.Float(string="Paid money", compute='Paid_money')
    remaining_money = fields.Float(string='Remaining money',compute='Remaining_moneyroom')

    # services_price=fields.Char(string="Price",)
    serv_total = fields.One2many(comodel_name="services_cost_hotel", inverse_name="serv_custom", )

    Make_reservation = fields.Boolean(string="Make a Reservation", readonly=True)

    _sql_constraints = [
        ('phone_unique', 'unique(phone)', 'Cant be duplicate phone number'),
        ('name_unique', 'unique(name)', 'Cant be duplicate Neme number'),
        ('identification_id_unique', 'unique(identification_id)', 'Cant be duplicate Identification Id'),
        ('passport_id_unique', 'unique(passport_id)', 'Cant be duplicate Passport No')
    ]

    @api.onchange('birth_of_date')
    def get_age(self):
        res = {}
        dt = False
        age_calc = False
        if self.birth_of_date:
            dt = datetime.strptime(self.birth_of_date, "%Y-%m-%d")
            age_calc = (datetime.today() - dt).days / 365
        age = str(age_calc) + ' Years'
        self.age = age

    @api.model
    def rooms_numbers(self):
        print "============================================"
        obj = self.env['hotel_booking_room'].search([('guest_name.id', '=', self.id)])
        print obj.guest_name.id, '********************************************************'
        for x in self:
            if obj.guest_name.id == self.id:
                x.room_no = obj.check_room.room_no

    @api.model
    def roomprice(self):
        print '----------------------------------------------------------'
        obj1 = self.env['hotel_booking_room'].search([('guest_name.id', '=', self.id)])
        for x in self:
            if obj1.guest_name.id == self.id:
                x.night_price = obj1.cost

    @api.one
    def days_number(self):
        print '----------------------------------------------------------'
        obj1 = self.env['hotel_booking_room'].search([('guest_name.id', '=', self.id)])
        for x in self:
            if obj1.guest_name.id == self.id:
                x.days_no = obj1.night_no

    @api.model
    def total_priceroom(self):
        print '----------------------------------------------------------'
        obj1 = self.env['hotel_booking_room'].search([('guest_name.id', '=', self.id)])
        for x in self:
            if obj1.guest_name.id == self.id:
                x.total_price = obj1.total_cost

    @api.model
    def Paid_money(self):
        print '----------------------------------------------------------'
        obj1 = self.env['hotel_booking_room'].search([('guest_name.id', '=', self.id)])
        for x in self:
            if obj1.guest_name.id == self.id:
                x.paid_money = obj1.money_paid

    @api.model
    def Remaining_moneyroom(self):
        print '----------------------------------------------------------'

        # self.remaining_money=self.total_price-self.paid_money
        obj1 = self.env['hotel_booking_room'].search([('guest_name.id', '=', self.id)])
        for x in self:
            if obj1.guest_name.id == self.id:
                x.remaining_money = obj1.remaining_money

    # =====================================================================================================
    Total= fields.Float(string="Total",compute='getsubtotal')
    def getsubtotal(self):
        y = 0.0
        for x in self.serv_total:
            y += x.subtotal
        self.Total = y