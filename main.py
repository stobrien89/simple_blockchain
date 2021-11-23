import hashlib

class NeuralCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data =  "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest

t1 = "x sends 2.5 NC to y"
t2 = "a sends 1.5 NC to z" 
t3 = "w sends .5 NC to r" 
t4 = "s sends 3 NC to t" 
t5 = "e sends .75 NC to f"        

initial_block = NeuralCoinBlock("let's pretend this is a prior transaction", [t1, t2])


