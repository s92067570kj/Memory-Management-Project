# memory_block.py

class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.is_allocated = False
        self.process_id = None

    def __str__(self):
        status = "Free" if not self.is_allocated else f"Allocated to Process {self.process_id}"
        return f"Size: {self.size}, Status: {status}"
