from openerp import models, fields, api
from openerp.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date


class NewModule(models.Model):
    _name = 'group_booking_rooms'
    # _rec_name = 'name'
    # _description = 'New Description'

    emp_name = fields.Many2one(comodel_name="hr.employee", string="Employee Name", required=True, )
    image = fields.Binary(string="Image", )

    @api.onchange('emp_name')
    def onchange_method(self):
        obj = self.env['hr.employee'].search([('id', '=', self.emp_name.id)])
        if (obj):
            self.image = obj.image

    workflow = fields.Selection(string="Reservation", selection=[('f', 'Reservation Form'), ('d', 'Check Date'),
                                                                 ('c', 'Reservation Confirmation'),
                                                                 ('x', 'Reservation Cancel')], default='f')
    filo = fields.Char(string="Reservation number", compute='reservtion')
    book_date = fields.Date(string="Booking Date", required=True)
    booking_type = fields.Selection(string="Booking Type", selection=[('Group', 'Group'), ], required=True)
    arrive_date = fields.Date(string="Arrived Date", required=True, )
    departure_date = fields.Date(string="Departure Date", required=True, )
    # guest_infor = fields.One2many(comodel_name="guests_informations", inverse_name="many_guest",
    #                               string="Guests Informayions", )
    selectrooms = fields.Many2many(comodel_name="room_hotelmanagement",string='Select Rooms',required=True)

    # group_num = fields.Integer(string="Group Number", required=True, )
    # duration = fields.Integer(string="Duration", )

    night_no = fields.Integer(string=" Duration", compute='get_day_no', )

    company_name = fields.Many2one(comodel_name="company.profile", string="Compane Name", required=True, )
    gettotal = fields.Many2one(comodel_name="room_hotelmanagement" )
    total=fields.Float(string="Price For Rooms",)
    total_price=fields.Float(string="Total Price",)

    # =============================================================================
    # @api.depends('guest_infor')
    def cucluteguest(self):
        print '==============================================================================='

# =========================================================================================
    @api.one
    def reservtion(self):
        self.filo = self.id
    # ==============================================================================================

    @api.onchange('arrive_date', 'departure_date')
    def get_day_no(self):
        fmt = '%Y-%m-%d'
        d1 = False
        d2 = False
        if self.arrive_date:
            d1 = datetime.strptime(self.arrive_date, '%Y-%m-%d')
        if self.departure_date:
            d2 = datetime.strptime(self.departure_date, '%Y-%m-%d')

        total_no = str((relativedelta(d2, d1)).days)
        self.night_no = total_no

    @api.constrains('arrive_date', 'departure_date')
    def comperdate(self):
       if(self.arrive_date >= self.departure_date):
           raise ValidationError("Departure date must be greater than arrival date")
       return True


# ===============================================================================================

    @api.multi
    def getdate_final(self):
        # self.workflow = 'd'
        print '----------------------'
        today = date.today()
        d1 = datetime.strptime(str(today), "%Y-%m-%d")
        print "=========================================", today, d1
        d2 = datetime.strptime(self.departure_date, "%Y-%m-%d")
        # obj = self.env['room_hotelmanagement'].search([('id', '=', self.selectrooms.id)])
        print today, '-------------------------------------------------------------------------------------------'
        if d1 >= d2:
            for x in self.selectrooms :
                x.state = False
            self.workflow = 'd'


    @api.multi
    def confirm_booking(self):
        self.company_name.Make_reservation=True
        self.workflow = 'c'
        if(self.workflow == 'c'):
            for x in self.selectrooms:
                x.state=True

    @api.multi
    def cancel_booking(self):
        self.workflow = 'x'
        if (self.workflow == 'x'):
            for x in self.selectrooms:
                x.state = False
            self.selectrooms=''
            for z in self.company_name:
                z.Make_reservation=False
            # self.company_name=''


    # ===============================================================================================


    @api.onchange('selectrooms')
    def rooms_price(self):
        print '-----------------------------------'
        y=0
        for x in self.selectrooms:
            y+=x.price
        self.total=y

    @api.onchange('total','night_no')
    def totalprice(self):
        self.total_price=self.total*self.night_no
















# class NewModule(models.Model):
#     _name = 'guests_informations'
#     _rec_name = 'name'
#     _description = 'New Description'
#
#     name = fields.Char()
#     id_gest = fields.Char(string="Guest ID", )
#     room = fields.Many2one(string="Room Number", comodel_name='room_hotelmanagement',
#                            domain=lambda self: [('state', '=', False)])
#     pr=fields.Integer(reiated='room.pirce')
#     many_guest = fields.Many2one(comodel_name="group_booking_rooms", )
