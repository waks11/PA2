import sys
from parser import parse_input
from cache_sim import *

def main():
    # Take and parse input into variables
    fileInput = sys.stdin.readlines()
    k_val, m_val, requests = parse_input(fileInput)

    fifo_misses = fifo(k_val, m_val, requests)
    lru_misses = lru(k_val, m_val, requests)
    optff_misses = optff(k_val, m_val, requests)

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {optff_misses}")

if __name__ == "__main__":
    main()