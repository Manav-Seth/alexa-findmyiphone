#!/usr/bin/env python

import os, sys
from pyicloud import PyiCloudService
from pyicloud.exceptions import PyiCloudFailedLoginException
import difflib
from users import USERS

def findIphone(event):
    try:
        intent = event['request']['intent']
        if intent['name'] == 'FindIphone':
            user = intent['slots']['User']['value']
            return findUserIphone(user)
    except PyiCloudFailedLoginException:
        return response("Invalid icloud email or password for " + user);
    except Exception as e:
        return response("Whoops, something broke: " + str(e))

    return response(
        "No idea what you asked for. Try saying, Find My iPhone, John.")

def findUserIphone(user):
    user = user.lower()

    found_user = difflib.get_close_matches(user, USERS.keys(), n=1)

    if len(found_user) == 0:
        return response("I don't know who " + user + " is.")
    
    user = found_user[0]
    email, passwd = USERS[user]
    api = PyiCloudService(email, passwd)   

    phones = [d for d in api.devices if d.content['deviceClass'] == 'iPhone']

    if len(phones) < 1:
        return response("Sorry, couldn't find any iPhones for " + user)

    for p in phones:
        p.play_sound()

    return response("Calling " + user + "'s iPhone.")


def response(msg):
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": msg,
            },
            "shouldEndSession": True
        }
    }


def lambda_handler(event, context):
    return findIphone(event)
