import sys
from collections import deque, OrderedDict


def fifo(k, requests):
    cache = set()
    queue = deque()
    misses = 0
    for r in requests:
        if r not in cache:
            misses += 1
            if len(cache) < k:
                cache.add(r)
                queue.append(r)
            else:
                evicted = queue.popleft()
                cache.remove(evicted)
                cache.add(r)
                queue.append(r)
    return misses


def lru(k, requests):
    cache = OrderedDict()
    misses = 0
    for r in requests:
        if r in cache:
            cache.move_to_end(r)
        else:
            misses += 1
            if len(cache) >= k:
                cache.popitem(last=False)
            cache[r] = True
    return misses


def optff(k, requests):
    cache = set()
    misses = 0
    for i, r in enumerate(requests):
        if r not in cache:
            misses += 1
            if len(cache) < k:
                cache.add(r)
            else:
                farthest = -1
                evict = None
                for item in cache:
                    try:
                        next_use = requests.index(item, i + 1)
                    except ValueError:
                        evict = item
                        break
                    if next_use > farthest:
                        farthest = next_use
                        evict = item
                cache.remove(evict)
                cache.add(r)
    return misses


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <input_file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        first_line = f.readline().split()
        k = int(first_line[0])
        requests = list(map(int, f.readline().split()))

    fifo_misses = fifo(k, requests)
    lru_misses = lru(k, requests)
    optff_misses = optff(k, requests)

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {optff_misses}")


if __name__ == "__main__":
    main()
