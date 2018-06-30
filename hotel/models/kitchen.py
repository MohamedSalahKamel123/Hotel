from openerp import models, fields, api


class NewModule(models.Model):
    _name = 'kitchen.kitchen'
    # _rec_name = 'name'
    _description = 'the kitchen Offers Food and Drinks'

    employee_kitchn = fields.Many2one(comodel_name="hr.employee", string="Employee Name", required=True)
    image = fields.Binary(string="Image")

    @api.onchange('employee_kitchn')
    def onchange_method(self):

        obj = self.env['hr.employee'].search([('id', '=', self.employee_kitchn.id)])
        if (obj):
            self.image = obj.image

    today_date = fields.Date(string="Today's Date", required=True)
    breakfas = fields.One2many(comodel_name="breakfast.clas", inverse_name="get_brek")
    lunch = fields.One2many(comodel_name="lunch.clas", inverse_name="get_lunch")
    dinner = fields.One2many(comodel_name="dinner.clas", inverse_name="get_dinner")


class NewModule(models.Model):
    _name = 'breakfast.clas'
    # _rec_name = 'name'
    # _description = 'New Description'

    food = fields.Selection(string="Food",
                            selection=[('eggs', 'Eggs'), ('Bean', 'Bean'), ('cheese', 'Cheese'), ('bread', 'Bread'),
                                       ('Cake', 'Cake'), ('olive', 'Olive'), ], )
    hot_drinks = fields.Selection(string="Hot Drinks",
                                  selection=[('Tea', 'Tea'), ('coffee', 'Coffee'), ('anise', 'Anise'),
                                             ('cacao', 'Cacao')], )
    cold_drinks = fields.Selection(string="Cold Drinks",
                                   selection=[('cocacola', 'Coca Cola'), ('Pepsi', 'Pepsi'), ('icecream', 'Ice Cream'),
                                              ('juice', 'Juice'), ], )
    # state = fields.Selection(string="Food", selection=[('a', 'meet'), ('b', 'food'), ('p', 'food'), ('l', 'food'), ('o', 'food'), ('w', 'food'), ], )


    get_brek = fields.Many2one(comodel_name="kitchen.kitchen", )


class NewModule(models.Model):
    _name = 'lunch.clas'
    # _rec_name = 'name'
    # _description = 'New Description'

    food = fields.Selection(string="Food",
                            selection=[('Meet', 'Meet'), ('Potatos', 'Potatos'), ('Molokhia', 'Molokhia'),
                                       ('Pasta', 'Pasta'), ('chickens', 'chickens'), ], )
    hot_drinks = fields.Selection(string="Hot Drinks",
                                  selection=[('Tea', 'Tea'), ('coffee', 'Coffee'), ('anise', 'Anise'),
                                             ('cacao', 'Cacao')], )
    cold_drinks = fields.Selection(string="Cold Drinks",
                                   selection=[('cocacola', 'Coca Cola'), ('Pepsi', 'Pepsi'), ('icecream', 'Ice Cream'),
                                              ('juice', 'Juice')], )
    # state = fields.Selection(string="Food", selection=[('a', 'meet'), ('b', 'food'), ('p', 'food'), ('l', 'food'), ('o', 'food'), ('w', 'food'), ], )


    get_lunch = fields.Many2one(comodel_name="kitchen.kitchen", )


class NewModule(models.Model):
    _name = 'dinner.clas'
    # _rec_name = 'name'
    # _description = 'New Description'

    food = fields.Selection(string="Food",
                            selection=[('Meet', 'Meet'), ('Potatos', 'Potatos'), ('Molokhia', 'Molokhia'),
                                       ('Pasta', 'Pasta'), ('chickens', 'chickens')], )
    hot_drinks = fields.Selection(string="Hot Drinks",
                                  selection=[('Tea', 'Tea'), ('coffee', 'Coffee'), ('anise', 'Anise'),
                                             ('cacao', 'Cacao')], )
    cold_drinks = fields.Selection(string="Cold Drinks",
                                   selection=[('cocacola', 'Coca Cola'), ('Pepsi', 'Pepsi'), ('icecream', 'Ice Cream'),
                                              ('juice', 'Juice')])
    # state = fields.Selection(string="Food", selection=[('a', 'meet'), ('b', 'food'), ('p', 'food'), ('l', 'food'), ('o', 'food'), ('w', 'food'), ], )


    get_dinner = fields.Many2one(comodel_name="kitchen.kitchen", )
