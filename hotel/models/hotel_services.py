from openerp import models, fields, api


class NewModule(models.Model):
    _name = 'hotel_services'
    # _rec_name = 'name'
    _description = 'New Description'

    image = fields.Binary(string="Image", )
    # name = fields.Many2one(comodel_name="customers_profile", string="Guest Name", required=True, )
    spa = fields.Selection(string="Spa", selection=[('s', 'special'), ('n', 'Normal'), ], )
    room_services = fields.Char(string="Room Services", )
    conference_hall = fields.Selection(string="Conference Hall",
                                       selection=[('s', '500 people'), ('b', '1000 people'), ], required=False, )
    wedding_hall = fields.Selection(string="Wedding Hall", selection=[('s', '500 people'), ('b', '1000 people'), ],
                                    required=False, )
    parking = fields.Boolean(string="Parking", )
    hotel_car = fields.Boolean(string="Use the hotel car", )

    serv_custom = fields.Many2one(comodel_name="customers_profile")
    subtotal = fields.Float(string="Subtotal",)
    getprice = fields.Many2one(comodel_name="services_cost_hotel", )

    # @api.onchange('spa', 'conference_hall', 'wedding_hall', 'parking', 'hotel_car')
    # def getsubtotal(self):
    #     x=0
    #     y=0
    #     pa=0
    #     sp=0
    #     ca=0
    #     for q in self.getprice:
    #         if (q.conference_hall == 's'):
    #             x += q.getprice.conferencehall_sprice
    #         elif (q.conference_hall == 'b'):
    #             x += q.getprice.conferencehall_bprice
    #             # ====================================================================
    #         if (q.wedding_hall == 's'):
    #             y += q.getprice.weddinghall_sprice
    #         elif (q.wedding_hall == 'b'):
    #             y += q.getprice.weddinghall_bprice
    #         # ===================================================================================
    #         if (q.spa == 's'):
    #             sp += q.getprice.spa_spcial
    #         elif (q.spa == 'n'):
    #             sp += q.getprice.spa_normal
    #         # =========================================================================================
    #
    #         if (q.parking == True):
    #             pa += q.getprice.parking_price
    #         if (q.hotel_car == True):
    #             ca += q.getprice.hotel_carprice
    #
    #         q.subtotal = x + y + sp + pa + ca
