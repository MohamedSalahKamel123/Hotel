import re
from datetime import datetime
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import time


class NewModule(models.Model):
    _name = 'hotel_booking_room'
    _rec_name = 'guest_name'

    employee_res = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    image = fields.Binary(string="Image")

    @api.onchange('employee_res')
    def onchange_method(self):
        obj = self.env['hr.employee'].search([('id', '=', self.employee_res.id)])
        if (obj):
            self.image = obj.image
    booking_type = fields.Selection(string="Booking Type", selection=[('Single', 'Single'), ], required=True, )

    guest_name = fields.Many2one(comodel_name="customers_profile", string="Guest Name", required=True, )

    age = fields.Char(string="Age", readonly=True, related='guest_name.age')

    arrival_date = fields.Date(string="Arrival Date", required=True, )
    departure_date = fields.Date(string="Departure Date", required=True, )

    # nationalty = fields.Selection(string="Nationalty", selection=[('e', 'Egyptian'), ('f', 'Foreigner'), ],
    #                               required=True)

    # group_res = fields.One2many(comodel_name="booking_booking_group", inverse_name="booking_group",
    #                             string="Group Reservation", )
    # no_group = fields.Integer(string="Group Number", required=True, )

    check_room = fields.Many2one(comodel_name="room_hotelmanagement", string="Select Room",
                                 required=True, )

    cost = fields.Float(string="Price per night", related='check_room.price', readonly=True, )
    total_cost = fields.Float(string="Total Cost", readonly=True, compute='getTotalPrice', )
    money_paid = fields.Float(string="Money Paid", required=True, )
    remaining_money = fields.Float(string="", readonly=True,)
    image = fields.Binary()
    email = fields.Char(string="E-mail", )
    night_no = fields.Integer(string="Night Nomber", compute='get_day_no', )

    workflow = fields.Selection(string="Reservation",
                                selection=[('c', 'Reservation Confirmation'),('f', 'Reservation Form'),
                                           ('x', 'Reservation Cancel')], default='f')

    filo = fields.Char(string="Reservation number", compute='reservtion')

    book_date = new_field = fields.Date(string="Booking Date", )

    # ====================================================================================================
    dat = fields.Char(string="Date", )
    _sql_constraints = [

        ('email_uniq', 'unique(email)', 'Email id is unique change your custom email id'),

    ]

    @api.constrains('email')
    def validate_email(self):
        for obj in self:

            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", obj.email) == None:
                raise ValidationError("Please Provide valid Email Address: %s" % obj.email)

            return True

    @api.constrains('departure_date', 'arrival_date')
    def validate_date(self):

        if (self.night_no < 0 or self.arrival_date == self.departure_date):
            raise ValidationError("Departure date must be greater than arrival date")
        return True

    @api.onchange('arrival_date', 'departure_date')
    def get_day_no(self):
        fmt = '%Y-%m-%d'
        d1 = False
        d2 = False
        if self.arrival_date:
            d1 = datetime.strptime(self.arrival_date, '%Y-%m-%d')
        if self.departure_date:
            d2 = datetime.strptime(self.departure_date, '%Y-%m-%d')

        total_no = str((relativedelta(d2, d1)).days)
        self.night_no = total_no

    @api.onchange('cost', 'night_no')
    def getTotalPrice(self):
        self.total_cost = self.night_no * self.cost

    @api.onchange('money_paid', 'total_cost', 'night_no')
    def countmoney(self):
        self.remaining_money = self.total_cost - self.money_paid
        if self.night_no >= 10:
            self.remaining_money = (self.total_cost - self.money_paid)

    @api.one
    def confirm_booking(self):
        self.workflow = 'c'
        print "======================================", self.check_room.id
        obj1 = self.env['room_hotelmanagement'].search([])
        for x in obj1:
            print "===========================================", x.id
        obj = self.env['room_hotelmanagement'].search([('id', '=', self.check_room.id)])
        print "------------------------------", obj
        obj.state = True
        # self.getdate()

        obj = self.env['customers_profile'].search([('id', '=', self.guest_name.id)])
        print "------------------------------", obj
        obj.Make_reservation = True











    @api.one
    def cancel_booking(self):

        self.workflow = 'x'
        self.frist_name = ''
        self.second_name = ''
        print "======================================", self.check_room.id
        obj1 = self.env['room_hotelmanagement'].search([])
        for x in obj1:
            print "===========================================", x.id
        obj = self.env['room_hotelmanagement'].search([('id', '=', self.check_room.id)])
        print "------------------------------", obj

        obj.state = False

    @api.onchange('guest_name')
    def siglestone_guest_name(self):
        for x in self:
            obj=x.env['customers_profile'].search([('id', '=',x.guest_name.id)])

    @api.multi
    def getdate_final(self):
        print '----------------------'
        today = date.today()
        d1 = datetime.strptime(str(today), "%Y-%m-%d")
        print "=========================================", today, d1
        d2 = datetime.strptime(self.departure_date, "%Y-%m-%d")
        obj = self.env['room_hotelmanagement'].search([('id', '=', self.check_room.id)])
        print today, '-------------------------------------------------------------------------------------------'
        if d1 >= d2:
            obj.state = False
            self.workflow = 'f'

    @api.one
    def reservtion(self):
        self.filo = self.id

        # @api.model
        # def reservtion_aa(self):
        #     today = date.today()
        #     # d1 = datetime.strptime(str(today), "%Y-%m-%d")
        #     # print "=========================================",today , d1
        #     # d2 = datetime.strptime(str(self.departure_date), "%Y-%m-%d")
        #     obj = self.env['room_hotelmanagement'].search([('id', '=', self.check_room.id)])
        #     print today, '-------------------------------------------------------------------------------------------'
        #     if today >= self.departure_date:
        #         obj.state = False
        #         print 'okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
        #




        # ============================================================================================================
        # ====================================================================================================
        # @api.one
        # def clear_record_data(self):
        #     self.write({
        #         'name': '',
        #         'booking_type': '',
        #         'frist_name': '',
        #         'second_name': '',
        #         # 'date_of_birth': '',
        #         'age': '',
        #         # 'arrival_date': '',
        #         # 'departure_date': '',
        #         'nationalty': '',
        #         'guest_iD': '',
        #         'group_res': '',
        #         'no_group': '',
        #         # 'check_room': '',
        #         'image': '',
        #         # 'email': '',
        #
        #
        #     })
        # ====================================================================================================

        # @api.one
        # def confirm(self):
        #     obj = [x.arrival_date for x in self.search([('check_room', '=', self.check_room.id)])]
        #     print "===========================================", obj
        #     for x in obj:
        #         print "===========================", x
        # -------------------------
        # compute = 'get_day_no',
        # serv = fields.Boolean(compute='get_room_register',)
        # //--------------------------------------------------------------------------------


        # @api.one
        # def clear_record_data(self):
        #     z=datetime.now()
        #     d1 = False
        #     # d2 = False
        #     if self.departure_date:
        #         d1 = datetime.strptime(self.departure_date, '%Y-%m-%d')
        #         # d2=  datetime.strptime(z, '%Y-%m-%d')
        #     if z>=d1:
        #
        #         print "------------------------------mmmmmmmmmmmmmmmmmmmmmmmm----------------------------------------"
        #         return {
        #
        #             'self.check_room.state':False,
        #
        #         }

        # @api.onchange('date_of_birth')

        # @api.onchange('date_of_birth')
        # @api.onchange('date_of_birth')
        # def get_age(self):
        #     res = {}
        #     dt = False
        #     age_calc = False
        #     if self.date_of_birth:
        #         dt = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        #         age_calc = (datetime.today() - dt).days / 365
        #     age = str(age_calc) + ' Years'
        #     self.age = age
