class Blockchain(object):
    def __init__(self):
        self.chain = [] 
        self.current_transactions = []

    def new_block(self): 
        # Creates a new block and adds it to the chain 
        pass 

    def new_transaction(self):
        # Adds a new transacion to the list of transactions 
        pass 

    @staticmethod 
    def hash(block):
        # Hashes a block 
        pass 

    @property 
    def last_block(self):
        # Returns the last Block in the chain 
        pass 

    