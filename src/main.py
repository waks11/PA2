import sys
from parser import parse_input

def main():
    # Take and parse input into variables
    fileInput = sys.stdin.readlines()
    k_val, m_val, requests = parse_input(fileInput)
    print(k_val, m_val, requests)

    # if len(sys.argv) != 2:
    #     print(f"Usage: python {sys.argv[0]} <input_file>")
    #     sys.exit(1)

    # with open(sys.argv[1]) as f:
    #     first_line = f.readline().split()
    #     k = int(first_line[0])
    #     requests = list(map(int, f.readline().split()))

    # fifo_misses = fifo(k, requests)
    # lru_misses = lru(k, requests)
    # optff_misses = optff(k, requests)

    # print(f"FIFO  : {fifo_misses}")
    # print(f"LRU   : {lru_misses}")
    # print(f"OPTFF : {optff_misses}")

if __name__ == "__main__":
    main()