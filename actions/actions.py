# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('tracker')
        print(tracker.get_slot('image_url'))
        print(tracker.get_slot('screenshot'))
        # print(tracker.events)
        # print(tracker.out_channel)

        dispatcher.utter_message(text="Hello World!")

        return []
class ActionUploadImage(Action):

    def name(self) -> Text:
        return "action_upload_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # print('tracker')
        # print(tracker.events)
        # print(tracker.out_channel)

        dispatcher.utter_message(text="Uploaded Successfully")

        return [AllSlotsReset()]
