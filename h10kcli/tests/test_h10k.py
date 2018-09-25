from unittest import TestCase

import h10kcli
from h10kcli.h10kparser import ParseConfig


class TestH10K(TestCase):
    def test_t010(self):
        test = ParseConfig('', 'h10k.yml')
        self.assertTrue(test.status() == 10)

    def test_t020(self):
        data = {
            'foo': 'bar'
        }
        test = ParseConfig(data, 'h10k.yml')
        self.assertTrue(test.status() == 20)

    def test_t030(self):
        data = {
            'ambari': {
                'foo': 'bar',
                'cluster_name': 'h10kdemo',
                'instance_type': 't2.micro'
            }
        }
        test = ParseConfig(data, 'h10k.yml')
        self.assertTrue(test.status() == 30)

    def test_t041(self):
        data = {
            'ambari': {
                'cluster_name': 'h10kdemo',
                'instance_type': 42
            }
        }
        test = ParseConfig(data, 'h10k.yml')
        self.assertTrue(test.status() == 40)

    def test_t042(self):
        data = {
            'ambari': {
                'cluster_name': 'h10kdemo',
                'instance_type': 't2.grunt'
            }
        }
        test = ParseConfig(data, 'h10k.yml')
        self.assertTrue(test.status() == 40)
