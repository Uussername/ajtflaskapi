#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    #add two more tests please
    def test_get_one(self):
        rv = self.app.get("/get_one_temp_api")
        self.assertEqual(rv.status, '200 OK')

    def test_get_ten(self):
        rv = self.app.get("/get_ten_temps_api")
        self.assertEqual(rv.status, '200 OK')



if __name__ == '__main__':
    unittest.main()
