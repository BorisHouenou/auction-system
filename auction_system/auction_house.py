import uuid
import logging

__author__ = "Landaspp <boris.houenou@landsapp.com>"

logging.getLogger().setLevel(logging.INFO)
 # Define the class for the auction house which then allows many prime users of our services to open and 
 # run the auction on Landsapp.com
 # We allow those users to add and  see latest auctions 

class AuctionHouse:
    def __init__(self):
        self.id = uuid.uuid1()
        self.auctions = []

    def add_auction(self, auction):
        existing_auctions = filter(lambda a: a.id == auction.id, self.auctions)
        if existing_auctions:
            logging.error("Land {} has already been "
                          "added to the land portfolio of this auction house".format(auction.id))
        else:
            self.auctions.append(auction)

    def latest_auction_by_item_name(self, name):
        auction = filter(lambda a: a.item.name == name, self.auctions)[-1]
        if auction is None:
            status = "The Land {} is not currently run through an auction".format(name)
        else:
            status = "The latest auction for the land {} is \n".format(name)
            if auction.has_failed:
                status += "Auction for the land {} did not " \
                          "reach the reserved price {}" \
                    .format(name, auction.item.reserved_price)
            else:
                if auction.highest_bid is None:
                    status += "No bidder for auction {} of item {}"\
                        .format(auction, name)
                else:
                    if auction.is_started:
                        status += "{} leads the auction with " \
                                  "the amount {}" \
                            .format(auction.highest_bid.bidder.name,
                                    auction.highest_bid.amount)
                    else:
                        status += "{} has been sold to {} " \
                                  "for the amount {}" \
                            .format(name,
                                    auction.highest_bid.bidder.name,
                                    auction.highest_bid.amount)
        return status
