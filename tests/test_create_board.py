import base.base_urls
from base.base_functions import Base
from base.base_urls import BaseUrls
from base.access_token import AccessToken
import json

class TestCreateBoard(Base):

    board_payload = { "name": "Test",
                      "key": base.access_token.AccessToken.API_KEY,
                      "token": base.access_token.AccessToken.ACCESS_TOKEN

    }

    def test_create_board(self):
        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.BOARDS_URL,
                                        payload= self.board_payload)
        formatted_response = json.dumps(response.json(), indent=2)
        print(formatted_response)

        self.assertEqual(response.status_code, 200, "Status code is NOT 200!")
        self.assertEqual(response.headers["Content-Type"], "application/json; charset=utf-8", "Incorrect JSON format!")
        #self.assertEqual(response.json(), self.board_payload, "Response does not match the request!")

        response_json = response.json()

        self.assertTrue(self.check_data_type(dict, response_json), "Response type is not dictionary!")
        print(response_json["name"])
        print(type(response_json["name"]))

        self.assertTrue(self.check_data_type(str, response_json["name"]),"name type is not string")
        self.assertTrue(self.check_data_type(str, response_json["prefs"]["background"]), "background type is not string")

