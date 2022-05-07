# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime

class ActionGaveTime(Action):

    def name(self) -> Text:
        return "action_give_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{datetime.today()}")

        return []

# class ActionSayUserName(Action):

#     def name(self) -> Text:
#         return "action_say_user_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         user_name = tracker.get_slot("user_name")
#         if not user_name:
#             dispatcher.utter_message(text="I don't know your name.")
#         else:
#             dispatcher.utter_message(text=f"Your name is {user_name}!")
#         return []