### 🧠 What is **Memcached**?

**Memcached** is a **high-performance, in-memory key-value store** used primarily for **caching** data to reduce the load on databases or expensive computations.

> It’s designed for **speed**, **simplicity**, and **scalability** — and is widely used in web applications.

---

## 🚀 Key Features

| Feature        | Description                                       |
| -------------- | ------------------------------------------------- |
| 🧠 In-memory   | All data is stored in RAM (no persistence)        |
| 🧩 Key-value   | Simple structure: keys mapped to arbitrary values |
| ⚡ Super fast   | Sub-millisecond read/write latency                |
| 🧹 Volatile    | Data is **not persistent** — lost if restarted    |
| 📦 Lightweight | Minimal dependencies, easy to install             |

---

## 🔧 How It’s Used

Imagine your web app frequently queries user profile data from a slow database:

1. First request → not in cache → fetch from DB → **store in Memcached**
2. Subsequent requests → hit Memcached → return in milliseconds

```python
# Example in Python (using `pymemcache`)
from pymemcache.client import base

client = base.Client(('localhost', 11211))
client.set('user:123', '{"name": "Alice", "age": 30}')
user_data = client.get('user:123')  # Fast!
```

---

## 📍 Common Use Cases

| Use Case               | Description                               |
| ---------------------- | ----------------------------------------- |
| ✅ Page caching         | Cache entire rendered pages               |
| ✅ Session storage      | Temporarily store user session data       |
| ✅ Database query cache | Cache frequent or heavy query results     |
| ✅ API rate limiting    | Store per-user request counters           |
| ✅ Computation results  | Cache expensive results (e.g., ML models) |

---

## 🆚 Memcached vs Redis

| Feature        | Memcached      | Redis                              |
| -------------- | -------------- | ---------------------------------- |
| 🧠 In-memory   | Yes            | Yes                                |
| 🗄 Data types  | Strings only   | Strings, lists, sets, hashes, etc. |
| 💾 Persistence | ❌ No           | ✅ Optional                         |
| 🔐 Auth        | ❌ Minimal      | ✅ Yes                              |
| 📊 Use Case    | Simple caching | Caching, queues, pub/sub, etc.     |

---

## 📦 Installation

**On Ubuntu:**

```bash
sudo apt install memcached
```

**Start with:**

```bash
memcached -m 64 -p 11211 -d
```

---

## 🔒 Notes

* Memcached is not secure by default — use behind firewalls.
* Does **not support complex data structures** or persistence like Redis.
* Evicts older data when memory limit is reached (Least Recently Used - LRU).

---

## ✅ Summary

| 🔹 Feature                | ✔️ Description                              |
| ------------------------- | ------------------------------------------- |
| Fast in-memory cache      | Yes                                         |
| Volatile (non-persistent) | Yes                                         |
| Key-value only            | Yes                                         |
| Use for                   | Reducing DB load, speeding up web responses |

---

Would you like help setting up Memcached with **Flask**, **Django**, or **FastAPI**?
