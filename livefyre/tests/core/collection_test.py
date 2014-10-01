import datetime, unittest, jwt, pytest

from jwt import DecodeError
from livefyre import Livefyre
from livefyre.tests import LfTest
from livefyre.src.entity.topic import Topic


class CollectionTestCase(LfTest, unittest.TestCase):
    CHECKSUM = '3631759a11c4e0671d9ab5c1c90153c9'
    
    def setUp(self):
        super(CollectionTestCase, self).setUp()
        self.network = Livefyre.get_network(self.NETWORK_NAME, self.NETWORK_KEY)
        self.site = self.network.get_site(self.SITE_ID, self.SITE_KEY)
        
    
    @pytest.mark.integration
    def test_create_update_collection(self):
        name = 'PythonCreateCollection' + str(datetime.datetime.now())
        
        collection = self.site.build_collection(name, name, self.URL).create_or_update()
        other_id = collection.get_collection_content()['collectionSettings']['collectionId']
        self.assertEquals(collection.get_collection_id(), other_id)
        
        collection.options = {'tags': 'super'}
        collection.create_or_update()
        self.assertEquals('super', collection.options['tags'])
        
    @pytest.mark.unit
    def test_build_collection_token(self):
        collection = self.site.build_collection('title', 'articleId', 'https://livefyre.com', {'tags': 'tags', 'type': 'reviews'})
        token = collection.build_collection_meta_token()
         
        self.assertIsNotNone(token)
        self.assertEquals(jwt.decode(token, self.SITE_KEY)['type'], 'reviews')
        
        collection = self.site.build_collection('title', 'articleId', 'https://livefyre.com', {'type': 'liveblog'})
        token = collection.build_collection_meta_token()
        self.assertEquals(jwt.decode(token, self.SITE_KEY)['type'], 'liveblog')
        
        topics = [Topic.create(self.network, '1', '1')]
        collection = self.site.build_collection(self.TITLE, self.ARTICLE_ID, self.URL, {'topics': topics})
        self.assertTrue(collection.network_issued)
        
        token = collection.build_collection_meta_token()
        
        with self.assertRaisesRegexp(DecodeError, 'Signature verification failed'):
            jwt.decode(token, self.site.key)
        
        decoded_token = jwt.decode(token, self.network.key)
        self.assertEquals(self.network.get_urn(), decoded_token['iss'])
    
    @pytest.mark.unit
    def test_build_checksum(self):
        collection = self.site.build_collection('title', 'articleId', 'http://livefyre.com', {'tags': 'tags'})
        checksum = collection.build_checksum()
        self.assertEquals(self.CHECKSUM, checksum, 'checksum is not correct.')
        

if __name__ == '__main__':
    unittest.main()