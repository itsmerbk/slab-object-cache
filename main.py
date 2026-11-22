class SlabCache:
    def __init__(self, slots): self.pool, self.free = [None]*slots, list(range(slots))
    def alloc(self, obj):
        if not self.free: raise MemoryError("Slab exhausted")
        idx = self.free.pop(); self.pool[idx] = obj; return idx
    def free_slot(self, idx): self.pool[idx] = None; self.free.append(idx)

if __name__ == "__main__":
    sc = SlabCache(2); i = sc.alloc({"fd": 3}); sc.free_slot(i); assert len(sc.free) == 2
    print("[PASS] 067_slab_object_cache")
