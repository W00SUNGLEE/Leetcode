class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = f'{n:032b}'
        return int(n[::-1], 2)
        #bin_rep = f'{n:032b}' # format n into binary bit string of length 32
        #print(bin_rep)
        #return int(bin_rep[::-1], 2) # reverse bit string and cast into int