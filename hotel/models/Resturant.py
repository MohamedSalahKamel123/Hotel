from openerp import models, fields, api
# import smtplib
class NewModule(models.Model):
    _name = 'hotel_resturant_serv'
    # _rec_name = 'Resturant'
    # _description = 'New Description'

    name = fields.Char()
    #
    # sender = 'username'
    # receivers = 'username'
    #
    # message = """hai da
    #                """

    # @api.one
    # def send_email(self):
    #
    #     smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    #     smtpObj.ehlo()
    #     smtpObj.starttls()
    #     smtpObj.ehlo()
    #     smtpObj.login(user="username", password="password")
    #     smtpObj.sendmail(self.sender,self.receivers,self.message)
    #     print "Successfully sent email"