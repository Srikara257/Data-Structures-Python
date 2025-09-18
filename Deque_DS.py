"""
Feature					collections.deque											queue.Queue

Primary Use Case	Single-threaded applications (general-purpose queues)	Multi-threaded applications (inter-thread communication)

Speed							Faster											Slower (due to thread-safe locks)

Memory						More memory-efficient								Less memory-efficient (due to overhead)

Thread Safety			Not thread-safe by default											Thread-safe

Operations				append(), pop(), appendleft(), popleft()							put(), get()
"""

"""
we can implement queue or stack usign 1.List 2.collections.deque 3 queue.Queue

1. List : General purpose O(n) time complexity for append and pop
2. collecitons.deque : Higly optimized O(1) time complexity for basic operations
3. queue.Queue : Must and should use this in Multi-threaded applications 
				 Slower than collections.dequw due to thread-safe Locks 
				 
"""
"""

The underscore before _deque in self._deque is a naming convention in Python, not a strict rule enforced by the language. It signifies that the variable is intended for internal use within the class.

Purpose of the Underscore
Indication of Privacy: In languages like Java or C++, you can declare a variable as private, which strictly prevents outside code from accessing it. Python doesn't have a true private keyword. Instead, the single leading underscore acts as a hint to other developers, saying, "Hey, don't mess with this variable directly from outside the class."

Preventing Name Clashes: The underscore also helps to prevent naming conflicts with subclasses. If a subclass creates a method or variable with the same name as a parent's "private" variable, the underscore helps avoid unintended overwrites.

Best Practice: Following this convention is considered good practice for creating clear and maintainable code. When someone reads your code, they'll immediately understand that _deque is part of the class's internal implementation and should be interacted with only through the public methods you've provided (like append(), pop(), to_list(), etc.).

In the DequeManager example, the public methods like append() and to_list() are the official way to interact with the deque. The _deque variable itself is the internal data store that these methods operate on. This separation of public interface and private implementation is a core principle of object-oriented programming.


"""

import collections

class DequeManager:
    """
    A class that manages a collections.deque object and provides
    methods to interact with it.
    """

    def __init__(self, iterable=None):
        """Initializes the DequeManager with an optional iterable."""
        self._deque = collections.deque(iterable if iterable is not None else [])

    def append(self, x):
        """Appends an element to the right side of the deque."""
        self._deque.append(x)

    def appendleft(self, x):
        """Appends an element to the left side of the deque."""
        self._deque.appendleft(x)

    def pop(self):
        """Removes and returns an element from the right side of the deque."""
        return self._deque.pop()

    def popleft(self):
        """Removes and returns an element from the left side of the deque."""
        return self._deque.popleft()

    def remove(self, value):
        """Removes the first occurrence of a value from the deque."""
        self._deque.remove(value)

    def clear(self):
        """Removes all elements from the deque."""
        self._deque.clear()

    def count(self, x):
        """Counts the number of occurrences of an element."""
        return self._deque.count(x)
    
    def extend(self, iterable):
        """Extends the deque by appending elements from the iterable."""
        self._deque.extend(iterable)

    def extendleft(self, iterable):
        """Extends the deque by prepending elements from the iterable."""
        self._deque.extendleft(iterable)

    def rotate(self, n=1):
        """Rotates the deque n steps to the right."""
        self._deque.rotate(n)

    def to_list(self):
        """Converts the deque to a standard Python list."""
        return list(self._deque)

    def __len__(self):
        """Returns the number of elements in the deque."""
        return len(self._deque)

    def __repr__(self):
        """Provides a string representation of the DequeManager."""
        return f"DequeManager({self._deque})"

# Example Usage
if __name__ == "__main__":
    dm = DequeManager([1, 2, 3])
    print(f"Initial deque: {dm}")

    # Using various methods
    dm.append(4)
    print(f"After append(4): {dm}")

    dm.appendleft(0)
    print(f"After appendleft(0): {dm}")

    popped_right = dm.pop()
    print(f"Popped from right: {popped_right}, Deque: {dm}")

    popped_left = dm.popleft()
    print(f"Popped from left: {popped_left}, Deque: {dm}")
	
    dm.extend([8,9])
    print(f"After extend([8,9]): {dm}")
    
    dm.extendleft([5, 6])
    print(f"After extendleft([5, 6]): {dm}")
    
    dm.rotate(2)
    print(f"After rotate(2): {dm}")

    # Converting to a list
    my_list = dm.to_list()
    print(f"Converted to list: {my_list}")
    print(f"Type of converted object: {type(my_list)}")
