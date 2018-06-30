from openerp import models, fields, api
class NewModule(models.Model):
    _name = 'company_rooms_hotel'
    # _rec_name = 'name'
    # _description = 'New Description'

    name = fields.Char()

