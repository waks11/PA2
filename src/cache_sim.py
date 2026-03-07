from collections import deque, OrderedDict


def fifo(k, m, requests):
    # Return early if there are no requests
    if m == 0: return 0

    # Set to track main values, Queue to keep track of FIFO
    cache, queue = set(), deque()
    misses = 0
    for r in requests:
        if r in cache:
            continue

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


def lru(k, m, requests):
    if m == 0: return 0

    # OrderedDict keeps track of LRU, end = newest
    cache = OrderedDict()
    misses = 0
    for r in requests:
        if r in cache:
            cache.move_to_end(r)
            continue

        misses += 1
        if len(cache) >= k:
            cache.popitem(last=False)

        cache[r] = True

    return misses


def optff(k, m, requests):
    if m == 0: return 0

    cache, misses = set(), 0
    for i, r in enumerate(requests):
        if r in cache:
            continue

        misses += 1
        if len(cache) < k:
            cache.add(r)
            continue

        farthest, evict = -1, None
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
