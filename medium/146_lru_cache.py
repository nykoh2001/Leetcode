"""https:#leetcode.com/problems/lru-cache/description/

- LRU Cache 구현
- Least Recently Used
- KVS: Default Dict
"""

from collections import defaultdict, OrderedDict
from datetime import datetime


# 1st Try: 22/24, Timeout
class _LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(int)
        # timestp: key
        self.cache_history = defaultdict(int)

    def _get_history_timestp_by_key(self, key: int) -> datetime | None:
        timestp_list = [
            timestp for timestp, k in self.cache_history.items() if k == key
        ]
        if len(timestp_list) > 1:
            msg = f"Duplicate history timestp for the same key - key={key}"
            raise ValueError(msg)

        if not timestp_list:
            return None

        return timestp_list[0]

    def _update_used_key_history(self, key: int) -> None:
        timestp_to_delete = self._get_history_timestp_by_key(key)
        if timestp_to_delete:
            del self.cache_history[timestp_to_delete]

        timestp_now = datetime.now()
        self.cache_history[timestp_now] = key

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val < 0:
            return val

        self._update_used_key_history(key)
        return val

    def _get_lru_key(self) -> tuple | None:
        cache_history_list = [
            (timestp, key) for timestp, key in self.cache_history.items()
        ]
        sorted_cache_history = sorted(cache_history_list, key=lambda x: x[0])

        if not sorted_cache_history:
            return None

        lru_timestp, lru_key = sorted_cache_history[0]
        return (lru_timestp, lru_key)

    def put(self, key: int, value: int) -> None:
        # If cache is already full & given key is new
        if len(self.cache) >= self.capacity and key not in self.cache.keys():
            lru_item = self._get_lru_key()
            if lru_item:
                lru_timestp, lru_key = lru_item
                del self.cache[lru_key]
                del self.cache_history[lru_timestp]

        self.cache[key] = value
        self._update_used_key_history(key)


# 2nd Try: OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value < 0:
            return value

        self.cache.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        # If cache is already full and given key is new, evict one
        if len(self.cache) >= self.capacity and key not in self.cache.keys():
            item_to_evict = next(iter(self.cache))
            del self.cache[item_to_evict]

        self.cache[key] = value
        self.cache.move_to_end(key)


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
