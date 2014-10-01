import unittest

from livefyre import Livefyre
from livefyre.tests import LfTest
from livefyre.src.factory.cursorfactory import CursorFactory


class TimelineCursorTestCase(LfTest, unittest.TestCase):
    def test_api_calls(self):
        network = Livefyre.get_network(self.NETWORK_NAME, self.NETWORK_KEY)
        cursor = CursorFactory.get_personal_stream_cursor(network, self.USER_ID)
        
        json = cursor.next()
        self.assertTrue(json)
        
        
if __name__ == '__main__':
    unittest.main()