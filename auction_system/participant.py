import uuid
from bid import Bid

__author__ = "Landsapp <boris.houenou@landsapp.com>"


# A participant can submit bids to an auction
class Participant:
    def __init__(self, name):
        self.id = uuid.uuid1()
        self.name = name

    def bid(self, auction, amount):
        Bid(self, auction, amount)



