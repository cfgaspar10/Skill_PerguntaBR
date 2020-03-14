# -*- coding: utf-8 -*-

import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type

from . import data


def get_random_state(states_list):
    return random.choice(states_list)
