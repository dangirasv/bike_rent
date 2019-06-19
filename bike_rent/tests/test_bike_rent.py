from odoo.tests import TransactionCase, tagged


@tagged('bike_rent')
class TestBikeRent(TransactionCase):

    def setUp(self):
        super(TestBikeRent, self).setUp()
        self.sale_order1 = self.env.ref('bike_rent.website_sale_order_rent1_demo')
        self.BikeRent = self.env['bike.rent']

    def test_bike_rent_creation_on_action_confirm(self):
        # Testing if action_confirm creates related bike.rent objects and if object count equals rented products count
        self.sale_order1.action_confirm()
        # Should I use filtered here instead?
        new_bike_rent_records = self.BikeRent.search([('sale_id', '=', self.sale_order1.id)])
        self.assertTrue(new_bike_rent_records)
        self.assertEqual(len(new_bike_rent_records), 2)

        # Testing if rent duration data is recorded correctly
        product_rent_duration = self.sale_order1.order_line.product_id.rent_duration
        self.assertEqual(product_rent_duration, new_bike_rent_records.mapped('rent_time')[0])
