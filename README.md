#Alexa Find My iPhone

This is an Amazon Echo app that will use the "find my iPhone" feature of iCloud to find your iPhone.

Most of the magic is done by [pyicloud](https://github.com/picklepete/pyicloud).

## About
This is a Python 3.9 script that can be packaged to Lambda for use as an Alexa skill.

## Requirements
* Python 3.9
* Bash (for build, OS X, Linux, Cygwin)
* pip-installed and configured awscli (uses the `aws lambda update-function-code` function)

## Virtual Envornment
Create your virtual environment in a directory named `venv`. The wsgi script depends on this. Install requirements in `requirements.txt`
```
cd [clone_directory]
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Lambda Config on Amazon AWS's end
**Trigger:** Alexa Skills Kit

**Name:** alexaFindMyIphone

**Runtime:** Python 3.9

Leave the "Edit Code Inline" option selected as it will be replaced with the zipped package on build.

**Handler:** `lambda_function.lambda_handler`

**Advanced Settings / Timeout:** 1 minute

## Alexa Skill Config on Amazon's end
**Name:** FindMyIPhone

**Invocation Name:** find my iphone

**Intent Schema:**

```
{
  "intents": [
    {
      "intent": "FindIphone",
      "slots": [
        {
          "name": "User",
          "type": "AMAZON.US_FIRST_NAME"
        }
      ]
    }
  ]
}
```

**Utterances:**

```
FindIphone {User}
FindIphone to call {User}
```

## User Config

Copy `users.example.py` to `users.py` to configure users' iCloud accounts. There is a `USERS` dictionary where each key is the name of the user, and each value is a trtupleie of iCloud username, password and devicename. example of devicename is iPhone 13 Pro.

## How to use

If you configured your app with the given Amazon config, you should be able to say to Alexa: `Alexa, tell Find My iPhone, John` where `John` is the user whose iPhone you are trying to find. It will then find the iPhone matching the devicename for the user `John`

## License
Code licensed under the unlicense. View `LICENSE.txt` for more information.

TL;DR; Code is public domain.

## TODO
* Clean up README
* Convert build.sh into Makefile
* Accept parameters for lambda function name in build/Makefile

