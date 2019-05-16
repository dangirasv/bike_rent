from odoo import exceptions
from odoo.tests import TransactionCase, tagged


@tagged('standard')
class TestBikeRent(TransactionCase):

    def setUp(self):
        super(TestBikeRent, self).setUp()

    def test_verify_stop_date(self):
        rent0 = self.env['bike.rent'].create({
            'bike_id': self.env['product.product'].search([('is_bike', '=', True)], limit=1).id,
            'partner_id': self.env['res.partner'].search([('name', '=', 'Versada')]).id,
            'rent_start': '2019-04-30 18:00:00',
            'rent_stop': '2019-04-20 18:00:00',
        })
        with self.assertRaises(exceptions.UserError):
            rent0._onchange_verify_stop_date()
