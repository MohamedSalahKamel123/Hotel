from openerp import models, fields, api


class NewModule(models.Model):
    _name = 'wizerard_serv'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()
