
import random
from typing import List, Dict, Union

class Randomizer:
    @staticmethod
    def generate_random_number(min_value, max_value):
        if min_value >= max_value:
            raise ValueError("Invalid range: min_value must be less than max_value.")
        return random.randint(min_value, max_value)

    @staticmethod
    def shuffle_list(input_list):
        random.shuffle(input_list)
        return input_list