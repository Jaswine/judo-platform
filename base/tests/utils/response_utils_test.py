from django.test import TestCase
from django.http import JsonResponse
from base.api.utils.response_utils import create_response
import json


class CreateResponseTestCase(TestCase):
    def test_create_response_success(self):
        response = create_response("Success message", 200)
        response_container = response.__dict__['_container']
        response_data = json.loads(response_container[0].decode('utf-8'))

        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], "success")
        self.assertEqual(response_data['message'], "Success message")

    def test_create_response_error(self):
        response = create_response("Error message", 404)
        response_container = response.__dict__['_container']
        response_data = json.loads(response_container[0].decode('utf-8'))

        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data['status'], "error")
        self.assertEqual(response_data['message'], "Error message")

    def test_create_response_info(self):
        response = create_response("Info message", 300)
        response_container = response.__dict__['_container']
        response_data = json.loads(response_container[0].decode('utf-8'))

        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 300)
        self.assertEqual(response_data['status'], "info")
        self.assertEqual(response_data['message'], "Info message")
