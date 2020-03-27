from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

import requests
import logging
import random

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):

    speech = "Hi, welcome to Today I Learned."
    asktext = "Would you like to hear one?"
    handler_input.response_builder.speak(speech + " " + asktext).ask(asktext)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("GetTILIntent"))
def whats_my_color_intent(handler_input):

    url = "https://www.reddit.com/r/todayilearned.json?limit=100"
    response = requests.get(url,headers={"User-agent":"todayilearned"})
    r = random.randint(1, 100)
    til = response.json()["data"]["children"][r]["data"]["title"]

    if(til[:3] == 'TIL'):
        til = til[4:]
        if(til[:4] == "that"):
            til = til[5:]

    asktext = "Wanna hear one more?"
    handler_input.response_builder.speak(til).ask(asktext)

    return handler_input.response_builder.response