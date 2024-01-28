import base.base_urls
from base.base_functions import Base
from base.access_token import AccessToken
from base.base_payloads import BasePayload
import json

class TestCreateList(Base):

    board_payload = { "name": "Test",
                      "key": base.access_token.AccessToken.API_KEY,
                      "token": base.access_token.AccessToken.ACCESS_TOKEN

    }

    def test_create_board(self):
        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.BOARDS_URL,
                                        payload= self.board_payload)
        formatted_response = json.dumps(response.json(), indent=2)
        print(formatted_response)
        board_id = response.json()["id"]
        print(board_id)
        return str(board_id)

    headers = {
        "Accept": "application/json"
    }

    query = {
        "name": "Test_List2",
        "key": base.access_token.AccessToken.API_KEY,
        "token": base.access_token.AccessToken.ACCESS_TOKEN
    }

    def test_create_new_list(self):
        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.CREATE_LIST_URL.format(board_id= self.test_create_board()),
                                        headers=self.headers, payload=self.query)

        print(response)


    def test_get_lists(self):
        response = self.general_request(method="POST", url="https://api.trello.com/1/boards/65b6cfef61edf7fc0a32fea2/lists", headers=self.headers, payload=self.query)
        print(response.json)