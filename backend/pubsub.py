import time
import os

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

# we need to get the keys from a file for safety
# do not add the file to github
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'pubnub_keys.txt'))
lines = file.read().split()
file.close()

pnconfig = PNConfiguration()
pnconfig.subscribe_key = lines[0]
pnconfig.publish_key = lines[1]
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())

def main():
    time.sleep(0.5)

    pubnub.publish().channel(TEST_CHANNEL).message({'foo' : 'bar'}).sync()

if __name__ == '__main__':
    main()

