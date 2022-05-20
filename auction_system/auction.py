import uuid
import logging

__author__ = "Landsapp <boris.houenou@landsapp.com>"

logging.getLogger().setLevel(logging.INFO)
 # Here we parametrize each auction session namely the start and  stop 

class Auction:
    def __init__(self, item):
        if item.is_sold:
            logging.error("Land {} already sold".format(item.name))
        else:
            self.id = uuid.uuid1()
            self.item = item
            self.is_started = False
            self.has_failed = None
            self.highest_bid = None

    # An auction can be started if it has not already failed
    def start(self):
        if self.has_failed is not None:
            logging.error("Auction {} already performed "
                          "on this Land.".format(self.id))
        else:
            self.is_started = True
            logging.info("Auction on this land {} has been started".format(self.id))

    # An auction can be stopped if it's started
    # If the reserved price is not met, the auction is tagged as failed
    # Technically the reserve price is too high. Maybe we shoud then advised the auctionner to lower 
    # their reserve price or re-enter or open another bid on the item
    def stop(self):
        if self.is_started:
            highest_bid = self.highest_bid
            if (highest_bid is None or
                    (highest_bid is not None and
                     self.item.reserved_price > highest_bid.amount)):
                self.has_failed = True
                logging.warning("Land {} did not reach "
                                "the reserved price"
                                "You could consider lowering the reserve price or open another auction".format(self.id))
            else:
                self.has_failed = False
                self.item.is_sold = True
            self.is_started = False
            logging.info("Auction on this land {} has been stopped".format(self.id))
        else:
            logging.error("Auction on this land {} is not started. "
                          "You can't stop it.".format(self.id))
