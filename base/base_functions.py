import unittest
import requests
import re


class Base(unittest.TestCase, object):

    def general_request(self, method, url, payload=None, **kwargs):
        request_response = requests.request("{}".format(method), url, json=payload, **kwargs)
        return request_response

    def check_data_type(self, data_type, value):
        return type(value) == data_type
