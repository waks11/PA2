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
