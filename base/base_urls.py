class BaseUrls:
    MAIN_URL = "https://api.trello.com/1"
    BOARDS_URL = MAIN_URL + "/boards"
    CREATE_LIST_URL = BOARDS_URL + "/{}/lists".format("")
    LISTS_URL = MAIN_URL + "/lists{}".format("")
    CARDS_URL = MAIN_URL + "/cards"
