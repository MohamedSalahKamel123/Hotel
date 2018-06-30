from openerp import models, fields, api
class NewModule(models.Model):
    _name = 'employee_hotel'
    _inherit = 'hr.employee'

    name = fields.Char()
