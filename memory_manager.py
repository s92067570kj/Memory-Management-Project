# memory_manager.py

from memory_block import MemoryBlock

class FirstFitMemoryManager:
    def __init__(self, memory_sizes):
        """Initialize memory blocks based on the given sizes."""
        self.memory_blocks = [MemoryBlock(size) for size in memory_sizes]

    def allocate(self, process_id, size):
        """Allocate memory using the First Fit algorithm."""
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= size:
                block.is_allocated = True
                block.process_id = process_id
                print(f"Process {process_id} allocated {size} units of memory.")
                return
        print("Allocation failed: Not enough memory available.")

    def deallocate(self, process_id):
        """Deallocate memory assigned to a specific process."""
        for block in self.memory_blocks:
            if block.is_allocated and block.process_id == process_id:
                block.is_allocated = False
                block.process_id = None
                print(f"Memory block for Process {process_id} has been deallocated.")
                return
        print(f"No memory block found for Process {process_id}.")

    def display(self):
        """Display the current memory layout."""
        print("\nCurrent Memory Layout:")
        for idx, block in enumerate(self.memory_blocks, start=1):
            print(f"Block {idx}: {block}")
