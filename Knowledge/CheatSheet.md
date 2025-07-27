# Python Cheatsheet for Distributed Backend Web Development

This cheatsheet provides a quick reference for Python's essential data structures and synchronization primitives, crucial for building robust and scalable backend web applications.

## 1. Core Python Data Structures

### 1.1. Lists (`list`) - Ordered, Mutable, Heterogeneous

* **Definition:** `[item1, item2, ...]`

* **Purpose:** General-purpose dynamic arrays.

* **Common Operations:**

    ```python
    my_list = [1, "hello", 3.14]
    my_list.append(4)         # Add to end: [1, 'hello', 3.14, 4]
    my_list.insert(1, "new")  # Insert at index: [1, 'new', 'hello', 3.14, 4]
    item = my_list.pop()      # Remove from end (LIFO): 4
    item = my_list.pop(0)     # Remove from specific index: 1
    my_list.remove("hello")   # Remove first occurrence of value
    print(my_list[0])         # Access by index
    print(my_list[1:3])       # Slicing: ['hello', 3.14]
    print(len(my_list))       # Length
    print("hello" in my_list) # Membership test
    ```

### 1.2. Tuples (`tuple`) - Ordered, Immutable, Heterogeneous

* **Definition:** `(item1, item2, ...)` or `item1, item2` (packing)

* **Purpose:** Fixed collections of related items, often used for function returns or dictionary keys.

* **Common Operations:**

    ```python
    my_tuple = (1, "world", 2.7)
    print(my_tuple[0])       # Access by index
    print(my_tuple[1:])      # Slicing: ('world', 2.7)
    x, y, z = my_tuple       # Unpacking
    # my_tuple[0] = 5        # TypeError: 'tuple' object does not support item assignment
    ```

### 1.3. Dictionaries (`dict`) - Key-Value Pairs, Insertion-Ordered (Python 3.7+), Mutable

* **Definition:** `{key1: value1, key2: value2, ...}`

* **Purpose:** Hash maps/associative arrays for fast lookups by key.

* **Common Operations:**

    ```python
    my_dict = {"name": "Alice", "age": 30}
    my_dict["city"] = "New York" # Add/Update
    print(my_dict["name"])       # Access: 'Alice'
    print(my_dict.get("email", "N/A")) # Safe access with default
    del my_dict["age"]           # Delete by key
    print("name" in my_dict)     # Check if key exists
    for key, value in my_dict.items(): # Iterate
        print(f"{key}: {value}")
    ```

### 1.4. Sets (`set`) - Unordered, Mutable, Unique Elements

* **Definition:** `{item1, item2, ...}` (for non-empty), `set()` (for empty)

* **Purpose:** Store unique elements, perform set operations (union, intersection).

* **Common Operations:**

    ```python
    my_set = {1, 2, 3, 2}     # {1, 2, 3} (duplicates removed)
    my_set.add(4)             # Add
    my_set.remove(1)          # Remove (raises KeyError if not found)
    my_set.discard(5)         # Remove (no error if not found)
    print(2 in my_set)        # Membership test
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    print(set_a.union(set_b))       # {1, 2, 3, 4, 5}
    print(set_a.intersection(set_b))# {3}
    ```

### 1.5. `collections` Module Enhancements

* **`collections.deque` (Double-Ended Queue):** Efficient appends/pops from both ends. Ideal for queues and stacks.
    ```python
    from collections import deque
    d = deque([1, 2, 3])
    d.appendleft(0) # [0, 1, 2, 3]
    d.pop()         # 3 (from right)
    d.popleft()     # 0 (from left)
    # Also useful for fixed-size circular queues: deque(maxlen=N)
    ```
* **`collections.defaultdict` (Default Dictionary):** Automatically initializes values for missing keys. Great for multimaps.
    ```python
    from collections import defaultdict
    multi_map = defaultdict(list)
    multi_map['users'].append('Alice')
    multi_map['users'].append('Bob')
    print(multi_map['users']) # ['Alice', 'Bob']
    ```
* **`collections.Counter`:** Counts hashable objects.
    ```python
    from collections import Counter
    counts = Counter("abracadabra")
    print(counts) # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
    ```
* **`heapq` (Heap Queue Algorithm):** Implements the min-heap data structure on a list. Useful for priority queues.
    ```python
    import heapq
    my_heap = []
    heapq.heappush(my_heap, 3)
    heapq.heappush(my_heap, 1)
    heapq.heappush(my_heap, 4)
    print(heapq.heappop(my_heap)) # 1 (smallest)
    ```

## 2. Concurrent Data Structures (Thread-Safe)

These are designed for safe use across multiple threads.

### 2.1. `queue` Module (Thread-Safe Queues)

* **`queue.Queue` (FIFO):** Standard thread-safe queue.
    ```python
    from queue import Queue
    q = Queue(maxsize=10) # Optional size limit
    q.put(item)           # Add item (blocks if full)
    item = q.get()        # Remove item (blocks if empty)
    q.task_done()         # Mark task as done (for join())
    q.join()              # Block until all items in queue are processed
    ```
* **`queue.LifoQueue` (LIFO - Stack):** Thread-safe stack.
    ```python
    from queue import LifoQueue
    stack = LifoQueue()
    stack.put(item)
    item = stack.get()
    ```
* **`queue.PriorityQueue`:** Thread-safe priority queue (lowest value retrieved first).
    ```python
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((priority_value, item)) # e.g., (1, 'high_priority_task')
    item = pq.get()
    ```

### 2.2. Making Standard DS Thread-Safe (Manual Locking)

For `list`, `dict`, `set`, `deque` (when not used as a simple queue/stack), you must manually use `threading.Lock` to protect concurrent modifications.

```python
import threading
import collections

class ThreadSafeList:
    def __init__(self):
        self._list = []
        self._lock = threading.Lock()

    def append(self, item):
        with self._lock: # Acquire lock, release on exit
            self._list.append(item)

    def pop(self):
        with self._lock:
            return self._list.pop()

# Similar patterns for ThreadSafeDict, ThreadSafeSet, ThreadSafeDeque
```

### 2.3. `multiprocessing.Queue` (Inter-Process Communication)

  * **Purpose:** For passing data safely between separate processes (bypasses GIL).
    ```python
    from multiprocessing import Queue
    mp_q = Queue()
    mp_q.put(item)
    mp_q.get()
    ```

## 3\. Thread Synchronization Primitives (from `threading` module)

These are fundamental tools for coordinating threads.

### 3.1. `threading.Lock` (Mutex)

  * **Purpose:** Ensures only one thread can access a critical section at a time.
  * **Usage:**
    ```python
    import threading
    my_lock = threading.Lock()
    # ...
    with my_lock: # Acquire lock, ensures exclusive access
        # Critical section of code
        pass
    # Lock automatically released
    ```
  * **When to use:** Protecting shared variables, lists, dictionaries, database connections, file I/O within a single process.

### 3.2. `threading.RLock` (Reentrant Lock)

  * **Purpose:** Allows the *same thread* to acquire the lock multiple times without deadlocking itself.
  * **Usage:**
    ```python
    import threading
    my_rlock = threading.RLock()
    def recursive_func():
        with my_rlock:
            # ...
            if condition:
                recursive_func() # Can re-acquire the same RLock
    ```
  * **When to use:** In recursive functions or nested method calls where a single thread might need to re-acquire a lock it already holds.

### 3.3. `threading.Semaphore`

  * **Purpose:** Limits the number of threads that can access a resource concurrently.
  * **Usage:**
    ```python
    import threading
    # Allow max 3 concurrent accesses
    my_semaphore = threading.Semaphore(3)
    # ...
    with my_semaphore: # Acquire a permit (blocks if no permits available)
        # Access limited resource
        pass
    # Permit automatically released
    ```
  * **When to use:** Managing resource pools (e.g., database connections, API rate limits), controlling concurrent downloads.

### 3.4. `threading.Event`

  * **Purpose:** Simple signaling mechanism. One thread sets an event, others wait for it.
  * **Usage:**
    ```python
    import threading
    my_event = threading.Event()
    # Thread A:
    my_event.wait() # Blocks until event is set
    # Thread B:
    my_event.set()  # Signals all waiting threads
    my_event.clear() # Resets the event
    ```
  * **When to use:** Coordinating startup/shutdown, signaling task completion.

### 3.5. `threading.Condition`

  * **Purpose:** Allows threads to wait for a specific condition to be met, often in conjunction with a shared resource.
  * **Usage:**
    ```python
    import threading
    my_condition = threading.Condition()
    # Producer thread:
    with my_condition:
        # Modify shared resource
        my_condition.notify()      # Wake one waiting thread
        my_condition.notify_all()  # Wake all waiting threads
    # Consumer thread:
    with my_condition:
        while not condition_met: # Always check condition in a loop
            my_condition.wait()  # Release lock and wait
        # Condition met, process resource
    ```
  * **When to use:** Complex producer-consumer scenarios, implementing custom blocking queues.

## 4\. Asynchronous Programming (`asyncio`)

For high-performance I/O-bound operations in a single thread, `asyncio` is key.

### 4.1. Basics (`async def`, `await`)

  * **`async def`:** Defines a coroutine (asynchronous function).
  * **`await`:** Pauses the execution of the current coroutine until the awaited operation completes, yielding control back to the event loop.
    ```python
    import asyncio
    import httpx # For async HTTP requests

    async def fetch_data(url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url) # Await I/O operation
            return response.json()

    async def main():
        data = await fetch_data("[https://api.example.com/data](https://api.example.com/data)")
        print(data)

    if __name__ == "__main__":
        asyncio.run(main()) # Run the top-level async function
    ```

### 4.2. Running Multiple Coroutines Concurrently

  * **`asyncio.gather(*coros)`:** Runs multiple coroutines concurrently and waits for all of them to complete.
    ```python
    import asyncio
    async def task_a():
        await asyncio.sleep(1)
        return "Result A"
    async def task_b():
        await asyncio.sleep(0.5)
        return "Result B"

    async def run_concurrent_tasks():
        results = await asyncio.gather(task_a(), task_b())
        print(results) # ['Result A', 'Result B']

    asyncio.run(run_concurrent_tasks())
    ```

### 4.3. Async Synchronization Primitives (from `asyncio` module)

These are similar in concept to `threading` primitives but are designed to work with `await`/`async` and the event loop.

  * **`asyncio.Lock`:** Asynchronous mutex.
    ```python
    import asyncio
    async_lock = asyncio.Lock()
    async def protected_resource_access():
        async with async_lock: # Acquire lock, release on exit
            # Asynchronous critical section
            await asyncio.sleep(0.1)
    ```
  * **`asyncio.Semaphore`:** Asynchronous semaphore.
    ```python
    import asyncio
    async_semaphore = asyncio.Semaphore(5) # Max 5 concurrent
    async def limited_async_task():
        async with async_semaphore:
            await asyncio.sleep(0.5)
    ```
  * **`asyncio.Event`:** Asynchronous event.
    ```python
    import asyncio
    async_event = asyncio.Event()
    async def waiter():
        await async_event.wait()
        print("Event set!")
    async def setter():
        await asyncio.sleep(1)
        async_event.set()
    ```
  * **`asyncio.Condition`:** Asynchronous condition variable.
    ```python
    import asyncio
    async_condition = asyncio.Condition()
    async def producer_async():
        async with async_condition:
            # Add item
            async_condition.notify_all()
    async def consumer_async():
        async with async_condition:
            await async_condition.wait()
            # Consume item
    ```
  * **`asyncio.Queue`:** Asynchronous, thread-safe queue (for `async` coroutines).
    ```python
    import asyncio
    async_q = asyncio.Queue()
    async def producer_async_q():
        await async_q.put("data")
    async def consumer_async_q():
        data = await async_q.get()
    ```

## 5\. Distributed Backend Specifics

### 5.1. Database Interaction (SQLAlchemy + FastAPI)

  * **Session Management:** Use FastAPI's `Depends` for managing SQLAlchemy database sessions.
    ```python
    from sqlalchemy.orm import Session
    from fastapi import Depends
    from .database import SessionLocal # Your DB session factory

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @app.get("/items/")
    async def read_items(db: Session = Depends(get_db)):
        # Use db session here
        pass
    ```
  * **Asynchronous DB Drivers:** For true async performance with databases, use async-compatible drivers and ORMs (e.g., `asyncpg` for PostgreSQL, `SQLAlchemy` 2.0+ with `asyncio` support).
    ```python
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy import select # Added import for select
    # ...
    async_engine = create_async_engine("postgresql+asyncpg://user:pass@host/db")
    AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession)

    async def get_async_db():
        async with AsyncSessionLocal() as session:
            yield session

    @app.get("/users/{user_id}")
    async def get_user(user_id: int, session: AsyncSession = Depends(get_async_db)):
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        return user
    ```

### 5.2. Distributed Task Queues (Celery + Redis)

  * **Purpose:** Offload long-running, non-blocking tasks from your web server.
  * **Broker:** Redis or RabbitMQ.
  * **Celery Task Definition:**
    ```python
    from celery import Celery
    celery_app = Celery('my_app', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

    @celery_app.task
    def process_image(image_id):
        # Long-running image processing logic
        pass
    ```
  * **Dispatching from FastAPI:**
    ```python
    from .celery_app import process_image
    @app.post("/process-image/{image_id}")
    async def trigger_image_processing(image_id: str):
        task = process_image.delay(image_id) # Non-blocking dispatch
        return {"message": "Image processing started", "task_id": task.id}
    ```
  * **Running Worker:** `celery -A celery_app worker --loglevel=info`

### 5.3. Caching (Redis)

  * **Purpose:** Improve read performance, reduce DB load.
  * **Strategy:** Cache-Aside (Lazy Loading) is common.
  * **Usage:**
    ```python
    import redis.asyncio as aioredis
    import json

    # Assuming redis_client is initialized globally or via dependency injection
    redis_client = None # Placeholder - initialize this in your app startup code

    @app.get("/cached-data/{key}")
    async def get_cached_data(key: str):
        cached_value = await redis_client.get(f"my_cache:{key}")
        if cached_value:
            return json.loads(cached_value)
        
        # Fetch from DB
        data = {"value": "from_db"} # Replace with actual DB fetch
        await redis_client.setex(f"my_cache:{key}", 3600, json.dumps(data)) # Cache for 1 hour
        return data

    @app.post("/update-data/{key}")
    async def update_data(key: str, new_value: str):
        # Update DB
        # ...
        await redis_client.delete(f"my_cache:{key}") # Invalidate cache
        return {"message": "Data updated and cache invalidated"}
    ```

This cheatsheet should serve as a solid reference as you continue to build and scale your Python backend applications. Remember to always consider the implications of concurrency and distribution in your designs.

```
```