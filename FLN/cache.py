import time
import hashlib
import json
from typing import Dict, Any, Optional, Tuple, List
from dataclasses import dataclass, field
from collections import OrderedDict


@dataclass
class CacheEntry:
    value: Any
    timestamp: float
    access_count: int = 0
    size: int = 0


class LRUCache:
    def __init__(self, max_size: int = 1000, ttl: int = 3600):
        self.max_size = max_size
        self.ttl = ttl
        self.cache: OrderedDict[str, CacheEntry] = OrderedDict()
        self.stats = {
            "hits": 0,
            "misses": 0,
            "evictions": 0,
            "expirations": 0
        }

    def _generate_key(self, *args, **kwargs) -> str:
        key_parts = []
        
        for arg in args:
            if isinstance(arg, (dict, list, tuple)):
                key_parts.append(json.dumps(arg, sort_keys=True))
            else:
                key_parts.append(str(arg))
        
        if kwargs:
            sorted_kwargs = sorted(kwargs.items())
            for key, value in sorted_kwargs:
                if isinstance(value, (dict, list, tuple)):
                    key_parts.append(f"{key}:{json.dumps(value, sort_keys=True)}")
                else:
                    key_parts.append(f"{key}:{value}")
        
        key_string = "|".join(key_parts)
        return hashlib.md5(key_string.encode()).hexdigest()

    def get(self, key: str) -> Optional[Any]:
        if key not in self.cache:
            self.stats["misses"] += 1
            return None
        
        entry = self.cache[key]
        
        if self.ttl > 0 and time.time() - entry.timestamp > self.ttl:
            del self.cache[key]
            self.stats["expirations"] += 1
            self.stats["misses"] += 1
            return None
        
        entry.access_count += 1
        self.cache.move_to_end(key)
        
        self.stats["hits"] += 1
        return entry.value

    def put(self, key: str, value: Any) -> None:
        if key in self.cache:
            del self.cache[key]
        
        entry = CacheEntry(
            value=value,
            timestamp=time.time(),
            access_count=1,
            size=self._estimate_size(value)
        )
        
        self.cache[key] = entry
        
        if len(self.cache) > self.max_size:
            self._evict_oldest()

    def _evict_oldest(self) -> None:
        if self.cache:
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
            self.stats["evictions"] += 1

    def _estimate_size(self, value: Any) -> int:
        try:
            return len(str(value))
        except:
            return 100

    def clear(self) -> None:
        self.cache.clear()

    def get_stats(self) -> Dict[str, Any]:
        total_requests = self.stats["hits"] + self.stats["misses"]
        hit_rate = self.stats["hits"] / total_requests if total_requests > 0 else 0
        
        return {
            **self.stats,
            "size": len(self.cache),
            "max_size": self.max_size,
            "hit_rate": hit_rate,
            "total_requests": total_requests
        }

    def __len__(self) -> int:
        return len(self.cache)


class ExpressionCache:
    def __init__(self, max_size: int = 500):
        self.ast_cache = LRUCache(max_size // 2, ttl=7200)
        self.evaluation_cache = LRUCache(max_size // 2, ttl=3600)
        self.formula_cache = LRUCache(max_size // 4, ttl=1800)

    def get_cached_ast(self, expression: str) -> Optional[Any]:
        return self.ast_cache.get(expression)

    def cache_ast(self, expression: str, ast: Any) -> None:
        self.ast_cache.put(expression, ast)

    def get_cached_evaluation(self, expression: str, variables: Dict[str, float] = None) -> Optional[Any]:
        key = self._make_evaluation_key(expression, variables)
        return self.evaluation_cache.get(key)

    def cache_evaluation(self, expression: str, variables: Dict[str, float], result: Any) -> None:
        key = self._make_evaluation_key(expression, variables)
        self.evaluation_cache.put(key, result)

    def get_cached_formulas(self, expression: str) -> Optional[List[Any]]:
        return self.formula_cache.get(expression)

    def cache_formulas(self, expression: str, formulas: List[Any]) -> None:
        self.formula_cache.put(expression, formulas)

    def _make_evaluation_key(self, expression: str, variables: Dict[str, float] = None) -> str:
        if variables is None:
            variables = {}
        
        sorted_vars = sorted(variables.items())
        var_str = json.dumps(sorted_vars, sort_keys=True)
        
        return f"{expression}|{var_str}"

    def clear_all(self) -> None:
        self.ast_cache.clear()
        self.evaluation_cache.clear()
        self.formula_cache.clear()

    def get_stats(self) -> Dict[str, Any]:
        return {
            "ast_cache": self.ast_cache.get_stats(),
            "evaluation_cache": self.evaluation_cache.get_stats(),
            "formula_cache": self.formula_cache.get_stats()
        }


class LazyEvaluator:
    def __init__(self, cache: ExpressionCache):
        self.cache = cache
        self.evaluation_queue: List[Tuple[str, Dict[str, float], Any]] = []
        self.partial_results: Dict[str, Any] = {}

    def add_to_queue(self, expression: str, variables: Dict[str, float] = None, priority: int = 0) -> str:
        queue_id = hashlib.md5(f"{expression}{variables}{priority}".encode()).hexdigest()
        
        self.evaluation_queue.append((queue_id, expression, variables or {}, priority))
        self.evaluation_queue.sort(key=lambda x: x[3], reverse=True)
        
        return queue_id

    def evaluate_next(self, evaluator_func) -> Optional[Tuple[str, Any]]:
        if not self.evaluation_queue:
            return None
        
        queue_id, expression, variables, priority = self.evaluation_queue.pop(0)
        
        cached_result = self.cache.get_cached_evaluation(expression, variables)
        if cached_result is not None:
            self.partial_results[queue_id] = cached_result
            return queue_id, cached_result
        
        result = evaluator_func(expression, variables)
        self.cache.cache_evaluation(expression, variables, result)
        self.partial_results[queue_id] = result
        
        return queue_id, result

    def get_partial_result(self, queue_id: str) -> Optional[Any]:
        return self.partial_results.get(queue_id)

    def clear_queue(self) -> None:
        self.evaluation_queue.clear()
        self.partial_results.clear()

    def get_queue_status(self) -> Dict[str, Any]:
        return {
            "queue_length": len(self.evaluation_queue),
            "partial_results_count": len(self.partial_results),
            "next_priority": self.evaluation_queue[0][3] if self.evaluation_queue else None
        }


_global_cache = ExpressionCache()


def get_global_cache() -> ExpressionCache:
    return _global_cache


def clear_global_cache() -> None:
    _global_cache.clear_all()


def get_cache_stats() -> Dict[str, Any]:
    return _global_cache.get_stats()
