
# for actions, and for separating item name from item state inside lists
SEPARATOR = "|"

# for subfolder-based urls: /shopping-lists/
BASE_URL_PATH = "/"

# recommended to change to something else
LISTS_FOLDER = "data"
# recommended to change, but not a big deal if left as it is
EVENTS_FILENAME = "events.log"
# change to false to disable event logging
LOG_EVENTS = False
# change for production
PASS = "a_fancy_password"
# change for production
COOKIE_KEY = "some_cookie_name"
# change for production
COOKIE_PASS = "some_cookie_paswword_which_really_is_just_a_value"

# set to False for production
DEBUG = True
# set to None for production
HOST_IP = "0.0.0.0"

# valid values: "top", "bottom"
NEW_ITEM_LOCATION = "bottom"
