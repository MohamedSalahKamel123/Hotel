from openerp import models, fields, api
from datetime import datetime
from openerp.exceptions import ValidationError

class NewModule(models.Model):
    _name = 'wizer.gust'
    start_date = fields.Date(string="Start Date", required=True, )
    end_date = fields.Date(string="End Date", required=True, )

    @api.constrains('start_date', 'end_date')
    def validate_date(self):

        if (self.start_date > self.end_date or self.start_date == self.end_date):
            raise ValidationError("Start Date must be greater than End Date")
        return True

    @api.multi
    def print_report(self):
        for y in self:
            obj = self.env['hotel_booking_room'].search(
                [('book_date', '>=', y.start_date), ('book_date', '<=', y.end_date)])
        # obj.dat = datetime.now()
        return self.env['report'].get_action(obj, 'hotel.report_hotel_folio')
