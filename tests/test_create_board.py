import base.base_urls
from base.base_functions import Base
from base.access_token import AccessToken
from base.base_payloads import BasePayload
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

        response_json = response.json()
        board_name = response_json["name"]
        board_id = response_json["id"]

        self.check_data_type(dict, response_json)

        self.check_data_type(str, board_name)
        self.check_key_and_value(board_name,self.board_payload["name"])

        self.assertEqual(response_json["name"], self.board_payload["name"], "Board name doesn't match!")

        # print("Board Variable Name:", self.board_payload["name"], "Created Board Name: ", response_json["name"])
        # print(type(response_json["name"]))

        self.check_key_and_value("id", response_json)
        # self.assertTrue("id" in response_json, "Board id is not present in the response!")
        # self.assertTrue(response_json["id"] is not None, "Error: Board id is null!")

        self.check_all_keys(BasePayload.default_payload, response_json)

        self.assertTrue(response_json["closed"] is False, "Error: Board is closed!")

        self.assertTrue(self.check_data_type(str, response_json["prefs"]["background"]), "background type is not string")


