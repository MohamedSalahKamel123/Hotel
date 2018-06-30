from openerp import models, fields, api
from openerp.exceptions import ValidationError
class NewModule(models.Model):
    _name = 'services_cost_hotel'
    # _rec_name = 'name'
    _description = 'New Description'

    spa_spcial=fields.Float(string='Spa Spcial', )
    spa_normal=fields.Float(string='Spa Normal',)
    roomservices_price = fields.Float(string="Room Services Price",)
    conferencehall_sprice = fields.Float(string="Small Conference  Price", )
    conferencehall_bprice = fields.Float(string="Large Conference  Price",  )
    weddinghall_sprice = fields.Float(string="Small Wedding Price" )
    weddinghall_bprice = fields.Float(string="Large Wedding Price",)
    parking_price = fields.Float(string="Parking Price", )
    hotel_carprice = fields.Float(string="Hotel Car Price", )
    state = fields.Selection(string="List Services", selection=[('e', 'Edit List'), ('c', 'Confirm List'), ],default='c' )
# =====================================================================================================================
    spa = fields.Boolean(string="Spa")
    room_services = fields.Boolean(string="Room Services", )
    conference_hall = fields.Boolean(string="Conference Hall",)
    wedding_hall = fields.Boolean(string="Wedding Hall", )
    parking = fields.Boolean(string="Parking", )
    hotel_car = fields.Boolean(string="Use the hotel car", )
    subtotal = fields.Float(string="Subtotal",)

    serv_custom = fields.Many2one(comodel_name="customers_profile")
    getprice = fields.Many2one(comodel_name="services_cost_hotel", )

# ========================================================================================================================
    @api.one
    def edit_list(self):
        self.state='e'


    # @api.one
    # def confirm_list(self):
    #     self.state = 'c'

    # @api.depends('conference_hall')
    # def jj(self):
    #     print '---------------------------mmmmmmmmmmmmmmmmmmmmmm--'
    #     x = 0
    #     # y = 0
    #     # pa = 0
    #     # sp = 0
    #     # ca = 0
    #     for q in self:
    #         if (q.conference_hall == 's'):
    #             x = q.conferencehall_sprice
    #
    #         q.subtotal=x