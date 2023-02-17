"""
Task 3

TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following
commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers
start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last
one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is
the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and
returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the
other case.


The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels_list):

        self.channels = channels_list
        self.curr_chan = self.channels[0]

    def first_channel(self):
        self.curr_chan = self.channels[0]
        return  self.curr_chan

    def last_channel(self):
        self.curr_chan = self.channels[-1]
        return self.curr_chan

    def turn_channel(self) -> object:
        while True:
            chan = input("Enter the channel number\n")

            if chan.isnumeric():
                chan = int(chan)
                if chan not in range(len(self.channels)):
                    print("Error channel")
                    continue
                else:
                    break
            else:
                print("Invalid enter")
                continue

        self.curr_chan = self.channels[chan-1]
        return self.curr_chan

    def next_channel(self):
        x = self.channels.index(self.curr_chan) + 1
        if x > (len(self.channels)-1):
            self.curr_chan = self.channels[0]
            x = 0
        else:
            self.curr_chan = self.channels[x]
        return self.curr_chan

    def previous_channel(self):
        x = self.channels.index(self.curr_chan) - 1
        if x < 0:
            self.curr_chan = self.channels[-1]
            x = -1
        else:
            self.curr_chan = self.channels[x]
        return self.curr_chan

    def current_chanel(self):
        return f"Current channel is {self.curr_chan}"

    def is_exist(self):
        chan = input("Enter channel`s name or number of channel to check\n")

        if chan.isnumeric():
            chan = int(chan)
            if chan in range(1, len(self.channels)+1):
                print("Yes")
        elif chan in self.channels:
            print("Yes")
        else:
            print("No")

    def controller(self):
        while True:

            x = input("Enter to:\n"
                      "1 - first channel.\n"
                      "2 - last channel.\n"
                      "3 - turn channel.\n"
                      "4 - next channel.\n"
                      "5 - previous channel.\n"
                      "6 - current channel.\n"
                      "7 - to check does channel exists."
                      "quit - to exit.")
            if x.isnumeric():
                x = int(x)
            elif x == "quit":
                break
            else:
                print("Invalid enter")
                continue

            if x == 1:
                print(self.first_channel())
            elif x == 2:
                print(self.last_channel())
            elif x == 3:
                print(self.turn_channel())
            elif x == 4:
                print(self.next_channel())
            elif x == 5:
                print(self.previous_channel())
            elif x == 6:
                print(self.current_chanel())
            elif x == 7:
                self.is_exist()
            else:
                print("Invalid enter!")


my_controller = TVController(CHANNELS)

my_controller.controller()
