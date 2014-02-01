#!/usr/bin/python

from SEChatWrapperAsync import SEChatAsyncWrapper
import getpass
import os

#Run `. setp.sh` to set the below testing environment variables
if "ChatExchangeU" in os.environ:
  username = os.environ["ChatExchangeU"]
else:
  print "Username: "
  username = raw_input()
if("ChatExchangeP" in os.environ):
  password = os.environ["ChatExchangeP"]
else:
  password = getpass.getpass("Password: ")

LAZERS_TRAINING_GROUND = "12779"
THE_BRIDGE = "35"

a = SEChatAsyncWrapper("SE")
a.login(username, password)
a.sendMessage(LAZERS_TRAINING_GROUND,
              "Please do not adjust your receiver.")
for i in range(10):
  a.sendMessage(LAZERS_TRAINING_GROUND, ":(")
a.logout()
