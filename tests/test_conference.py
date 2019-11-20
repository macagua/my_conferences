# -*- coding: utf-8 -*-

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestConference(common.TransactionCase):

    def setUp(self):
        super(TestConference, self).setUp()
        # 'myconferences.conference' instance model
        self.conference = self.env['myconferences.conference']

        # create an 'conference' record
        self.conference1 = self.conference.create({
            'name': 'PloneConf 2020',
            'indexed': True,
            'start_date': '2020-10-01',
            'end_date': '2020-10-07',
            'fee': 96.0,
        })

        self.conference2 = self.conference.create({
            'name': 'PyConf US 2020',
            'indexed': True,
            'start_date': '2020-07-06',
            'end_date': '2020-07-11',
            'fee': 196.0,
        })

        self.conference3 = self.conference.create({
            'name': 'Odoo Experience 2020',
            'indexed': True,
            'start_date': '2020-11-12',
            'end_date': '2020-11-16',
            'fee': 396.0,
        })

    def test_conferences_creation(self):
        # This function test the 'myconferences.conference' instances creation functionality

        # check 'name' of the 'conference1'
        self.assertEqual(self.conference1.name, 'PloneConf 2020')
        _logger.info('Created the {0} Conference!'.format(self.conference1.name))

        # check 'name' of the 'conference2'
        self.assertEqual(self.conference2.name, 'PyConf US 2020')
        _logger.info('Created the {0} Conference!'.format(self.conference2.name))

        # check 'name' of the 'conference3'
        self.assertEqual(self.conference3.name, 'Odoo Experience 2020')
        _logger.info('Created the {0} Conference!'.format(self.conference3.name))

        # Do a little print to show it visually for this demo - in production you don't really need this.
        _logger.info("Your 'TestConference' test was successful!")
