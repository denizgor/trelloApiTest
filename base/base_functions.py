import unittest
import requests
import re


class Base(unittest.TestCase, object):

    def general_request(self, method, url, payload=None, **kwargs):
        request_response = requests.request("{}".format(method), url, json=payload, **kwargs)
        return request_response

    # def check_data_type(self, data_type, value):
    #     return type(value) == data_type

    def check_key_and_value(self, key_in_response, response, payload_variable = None):
        self.assertTrue(key_in_response in response, "Error! {} is not in the response.".format(key_in_response))
        self.assertTrue(key_in_response is not None and key_in_response != "", "{} is null".format(key_in_response))

        if payload_variable is not None:
            self.assertEqual(payload_variable, key_in_response, "{} and the {} do not match!"
                             .format(payload_variable, key_in_response))

        print("The key is present in the response and the value for the key is valid and correct.")
    def check_data_type(self, data_type, key_in_response):
        try:
            return type(key_in_response) == data_type
        except AssertionError as error:
            print("Assertion error: {}".format(error))

    def check_all_keys(self, reference_payload, response):
        for key in reference_payload:
            self.assertTrue(key in response)