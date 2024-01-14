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
        self.assertTrue(response_json["name"] is not None)
        self.assertTrue(self.check_data_type(str, response_json["name"]),"name type is not string")
        self.assertEqual(response_json["name"], self.board_payload["name"], "Board name doesn't match!")

        print("Board Variable Name:", self.board_payload["name"], "Created Board Name: ", response_json["name"])
        print(type(response_json["name"]))

        self.assertTrue("id" in response_json, "Board id is not present in the response!")
        self.assertTrue(response_json["id"] is not None, "Error: Board id is null!")

        self.assertTrue(response_json["closed"] is False, "Error: Board is closed!")

        self.assertTrue(self.check_data_type(str, response_json["prefs"]["background"]), "background type is not string")


#
# {
#   "id": "659b19552aa427f06c079e2a",
#   "name": "Test4",
#   "desc": "",
#   "descData": null,
#   "closed": false,
#   "idOrganization": "65904fdb10984513ce794021",
#   "idEnterprise": null,
#   "pinned": false,
#   "url": "https://trello.com/b/quyAhk3V/test4",
#   "shortUrl": "https://trello.com/b/quyAhk3V",
#   "prefs": {
#     "permissionLevel": "private",
#     "hideVotes": false,
#     "voting": "disabled",
#     "comments": "members",
#     "invitations": "members",
#     "selfJoin": true,
#     "cardCovers": true,
#     "cardCounts": false,
#     "isTemplate": false,
#     "cardAging": "regular",
#     "calendarFeedEnabled": false,
#     "hiddenPluginBoardButtons": [],
#     "switcherViews": [
#       {
#         "viewType": "Board",
#         "enabled": true
#       },
#       {
#         "viewType": "Table",
#         "enabled": true
#       },
#       {
#         "viewType": "Calendar",
#         "enabled": false
#       },
#       {
#         "viewType": "Dashboard",
#         "enabled": false
#       },
#       {
#         "viewType": "Timeline",
#         "enabled": false
#       },
#       {
#         "viewType": "Map",
#         "enabled": false
#       }
#     ],
#     "background": "blue",
#     "backgroundColor": "#0079BF",
#     "backgroundImage": null,
#     "backgroundTile": false,
#     "backgroundBrightness": "dark",
#     "backgroundImageScaled": null,
#     "backgroundBottomColor": "#0079BF",
#     "backgroundTopColor": "#0079BF",
#     "canBePublic": true,
#     "canBeEnterprise": true,
#     "canBeOrg": true,
#     "canBePrivate": true,
#     "canInvite": true
#   },
#   "labelNames": {
#     "green": "",
#     "yellow": "",
#     "orange": "",
#     "red": "",
#     "purple": "",
#     "blue": "",
#     "sky": "",
#     "lime": "",
#     "pink": "",
#     "black": "",
#     "green_dark": "",
#     "yellow_dark": "",
#     "orange_dark": "",
#     "red_dark": "",
#     "purple_dark": "",
#     "blue_dark": "",
#     "sky_dark": "",
#     "lime_dark": "",
#     "pink_dark": "",
#     "black_dark": "",
#     "green_light": "",
#     "yellow_light": "",
#     "orange_light": "",
#     "red_light": "",
#     "purple_light": "",
#     "blue_light": "",
#     "sky_light": "",
#     "lime_light": "",
#     "pink_light": "",
#     "black_light": ""
#   },
#   "limits": {}
#}
