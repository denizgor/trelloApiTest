import base.base_urls
from base.base_functions import Base
from base.access_token import AccessToken
from base.base_payloads import BasePayload
import json


class TestCreateList(Base):
    #BOARD PAYLOAD
    board_payload = {"name": "Test_List",
                     "key": base.access_token.AccessToken.API_KEY,
                     "token": base.access_token.AccessToken.ACCESS_TOKEN

                     }

    headers = {
        "Accept": "application/json"
    }


    def test_create_list(self):
        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.BOARDS_URL,
                                        payload=self.board_payload)
        formatted_response = json.dumps(response.json(), indent=2)
        print(formatted_response)
        board_id = str( response.json()["id"])
        print("Board ID: ", board_id)


        # CREATE LIST PAYLOAD
        query = {
            "name": "Test_List3",
            "idBoard": board_id,
            "key": base.access_token.AccessToken.API_KEY,
            "token": base.access_token.AccessToken.ACCESS_TOKEN
        }
        # Create a new list
        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.CREATE_LIST_URL.format(board_id),  params=query)

        print(response)
        print(response.text)

        query = {

            "key": base.access_token.AccessToken.API_KEY,
            "token": base.access_token.AccessToken.ACCESS_TOKEN,
            "idBoard": board_id
        }
        response = self.general_request(method="GET", url=base.base_urls.BaseUrls.LISTS_URL, params=query)
        print("Get List: ", response.json)
        print(response.status_code)
        print(response.text)

    query = {
        "name": "Test_List2",
        "idBoard": "65c568118c53a0b61181904a",
        "key": base.access_token.AccessToken.API_KEY,
        "token": base.access_token.AccessToken.ACCESS_TOKEN
    }
