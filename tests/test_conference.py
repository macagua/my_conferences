# -*- coding: utf-8 -*-

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestConference(common.TransactionCase):

    def setUp(self):
        super(TestConference, self).setUp()
        # 'myconferences.conference' instance model
        self.conference = self.env['myconferences.conference']

        # create an conference record
        self.conference1 = self.conference.create({
            'confname': 'PloneConf 2020',
            'indexed': True,
            'startdate': '2020-10-01',
            'enddate': '2020-10-07',
            'fee': 96.0,
        })

        self.conference2 = self.conference.create({
            'confname': 'PyConf US 2020',
            'indexed': True,
            'startdate': '2020-07-06',
            'enddate': '2020-07-11',
            'fee': 196.0,
        })

        self.conference3 = self.conference.create({
            'confname': 'Odoo Experience 2020',
            'indexed': True,
            'startdate': '2020-11-12',
            'enddate': '2020-11-16',
            'fee': 396.0,
        })

    def test_conferences_creation(self):
        # This function test the 'myconferences.conference' instances creation functionality

        # check confname of the conference1
        self.assertEqual(self.conference1.confname, 'PloneConf 2020')
        _logger.info('Created the {0} Conference!'.format(self.conference1.confname))

        # check confname of the conference2
        self.assertEqual(self.conference2.confname, 'PyConf US 2020')
        _logger.info('Created the {0} Conference!'.format(self.conference2.confname))

        # check confname of the conference3
        self.assertEqual(self.conference3.confname, 'Odoo Experience 2020')
        _logger.info('Created the {0} Conference!'.format(self.conference3.confname))

        # Do a little print to show it visually for this demo - in production you don't really need this.
        _logger.info('Your test was succesfull!')
