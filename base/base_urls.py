class BaseUrls:
    MAIN_URL = "https://api.trello.com/1"
    BOARDS_URL = MAIN_URL + "/boards"
    CREATE_LIST_URL = BOARDS_URL + "/{}/lists".format(id)
    LISTS_URL = BOARDS_URL + "/lists/{}".format(id)
    CARDS_URL = MAIN_URL + "/cards"
