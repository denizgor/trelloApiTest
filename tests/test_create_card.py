import base.base_urls
from base.base_functions import Base
from base.access_token import AccessToken
from base.base_payloads import BasePayload
import json
import logging


class TestCreateCard(Base):

    def test_create_list(self):
        # BOARD PAYLOAD
        board_payload = {"name": "Test_Card_Board",
                         "key": base.access_token.AccessToken.API_KEY,
                         "token": base.access_token.AccessToken.ACCESS_TOKEN

                         }

        headers = {
            "Accept": "application/json"
        }

        #Create Board
        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.BOARDS_URL, headers=headers,
                                        payload=board_payload)
        formatted_response = json.dumps(response.json(), indent=2)
        print(formatted_response)
        board_id = response.json()["id"]
        print("Board ID: ", board_id)

        self.assertEqual(response.status_code, 200, "Status code is NOT 200!")
        self.assertEqual(response.headers["Content-Type"], "application/json; charset=utf-8", "Incorrect JSON format!")




        # CREATE LIST PAYLOAD
        query = {
            "name": "Test_List_with_Card",
            "idBoard": board_id,
            "key": base.access_token.AccessToken.API_KEY,
            "token": base.access_token.AccessToken.ACCESS_TOKEN
        }

        #log
        #logging.basicConfig(level=logging.DEBUG)

        # Create a new list
        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.LIST_URL, params=query)
        list_id = response.json()["id"]

        print(response)
        print("List ID: ", list_id)
        print("Create List Response Text: ", response.text)

        #Get List

        query = {

            "key": base.access_token.AccessToken.API_KEY,
            "token": base.access_token.AccessToken.ACCESS_TOKEN,
        }
        response = self.general_request(method="GET", url=base.base_urls.BaseUrls.GET_LIST_URL.format(list_id), params=query)
        print("Get List: ", response.json())
        print(response.status_code)
        print(response.text)

        #Create a card in a list
        query = {
            'name': "New Card",
            'idList': list_id,
            'key': base.access_token.AccessToken.API_KEY,
            'token': base.access_token.AccessToken.ACCESS_TOKEN
        }

        response = self.general_request(method="POST", url=base.base_urls.BaseUrls.CARDS_URL, headers=headers, params=query)
        print(response.status_code)
        print(response.text)