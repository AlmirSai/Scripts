## **1. Linear Data Structures**

### **Arrays**
- **Description:** Fixed-size, contiguous blocks of memory.
- **Main Operations:**
  - **Access:** `arr[i]` or using pointer arithmetic (constant time, *O(1)*).
  - **Size:** Typically tracked separately since built-in arrays do not carry size information.
- **Notes:** C-style arrays have no built-in methods. Modern C++ encourages using [`std::array`](https://en.cppreference.com/w/cpp/container/array) for fixed-size arrays, which offers a member function interface.
  
**`std::array` Methods:**
- `at(index)`: Bounds-checked element access.
- `front()`: Returns first element.
- `back()`: Returns last element.
- `data()`: Returns pointer to the underlying array.
- `size()`: Returns number of elements.
- `fill(const T&)`: Fills array with a given value.

**Example:**
```cpp
#include <array>
#include <iostream>

int main() {
    std::array<int, 5> arr = {1, 2, 3, 4, 5};
    std::cout << "Third element: " << arr.at(2) << std::endl;
    std::cout << "Array size: " << arr.size() << std::endl;
    return 0;
}
```

---

### **Vectors (`std::vector`)**
- **Description:** Dynamic array that resizes automatically.
- **Main Methods:**
  - `push_back(const T&)` / `emplace_back(args...)`: Add element at the end.
  - `pop_back()`: Remove the last element.
  - `operator[]` and `at(index)`: Element access (*O(1)*).
  - `front()` / `back()`: Access first/last element.
  - `insert(iterator pos, value)`: Insert at arbitrary position (*O(n)* in worst case).
  - `erase(iterator pos)`: Remove element (*O(n)*).
  - `size()`, `empty()`, `capacity()`, `resize()`, `reserve()`.
  
**Example:**
```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3};
    vec.push_back(4);
    std::cout << "Last element: " << vec.back() << std::endl;
    return 0;
}
```

---

### **Linked Lists**
C++ offers two main linked list types:

#### **(a) Doubly Linked List (`std::list`)**
- **Description:** Each element stores pointers to both next and previous nodes.
- **Main Methods:**
  - `push_back()`, `push_front()`: Insert at back or front.
  - `pop_back()`, `pop_front()`: Remove from back or front.
  - `insert(iterator pos, value)`: Insert before a given iterator.
  - `erase(iterator pos)`: Remove element at the iterator.
  - `begin()`, `end()`: Iterators for traversal.
  - `size()`, `empty()`, `clear()`, `splice()` (move elements between lists).
- **Use Case:** Frequent insertions and deletions anywhere in the list.

#### **(b) Singly Linked List (`std::forward_list`)**
- **Description:** Each element has a pointer only to the next element.
- **Main Methods:**
  - `push_front()`: Insert at the beginning.
  - `pop_front()`: Remove from the beginning.
  - `insert_after(iterator pos, value)`: Insert after a given position.
  - `erase_after(iterator pos)`: Remove element following the iterator.
  - `before_begin()`: Returns an iterator to the element before the first element.
  - `begin()`, `end()`, `empty()`, `clear()`.
- **Use Case:** Lower memory overhead when only one-direction traversal is needed.

**Example (`std::forward_list`):**
```cpp
#include <forward_list>
#include <iostream>

int main() {
    std::forward_list<int> flist = {2, 3, 4};
    flist.push_front(1);  // Now: 1, 2, 3, 4
    for (int num : flist)
        std::cout << num << " ";  // Output: 1 2 3 4 
    return 0;
}
```

---

### **(c) Deque (`std::deque`)**
- **Description:** Double-ended queue that supports fast insertion and deletion at both ends.
- **Main Methods:**
  - `push_back()`, `push_front()`: Insert at back or front.
  - `pop_back()`, `pop_front()`: Remove from back or front.
  - `operator[]`, `at()`: Random access (not as fast as `std::vector` due to segmented memory).
  - `front()`, `back()`, `size()`, `empty()`.
- **Use Case:** When you need fast insertions and deletions at both ends and also require random access.

**Example:**
```cpp
#include <deque>
#include <iostream>

int main() {
    std::deque<int> dq = {10, 20, 30};
    dq.push_front(5);
    dq.push_back(40);
    std::cout << "Front: " << dq.front() << ", Back: " << dq.back() << std::endl;
    return 0;
}
```

---

### **(d) Stack (`std::stack`)**
- **Description:** LIFO (Last-In, First-Out) container adapter.
- **Underlying Container:** Typically uses `std::deque` by default.
- **Main Methods:**
  - `push(const T&)` / `emplace(args...)`: Add element on top.
  - `pop()`: Remove the top element.
  - `top()`: Access the top element.
  - `empty()`, `size()`.
- **Use Case:** When you need a simple LIFO structure (e.g., function call stack, undo mechanisms).

**Example:**
```cpp
#include <stack>
#include <iostream>

int main() {
    std::stack<int> s;
    s.push(10);
    s.push(20);
    std::cout << "Top element: " << s.top() << std::endl;  // Output: 20
    s.pop();
    std::cout << "New top element: " << s.top() << std::endl;  // Output: 10
    return 0;
}
```

---

### **(e) Queue (`std::queue`)**
- **Description:** FIFO (First-In, First-Out) container adapter.
- **Underlying Container:** Typically uses `std::deque`.
- **Main Methods:**
  - `push(const T&)`: Add element at the back.
  - `pop()`: Remove the front element.
  - `front()`: Access the front element.
  - `back()`: Access the last element.
  - `empty()`, `size()`.
- **Use Case:** Task scheduling, breadth-first traversal.

**Example:**
```cpp
#include <queue>
#include <iostream>

int main() {
    std::queue<int> q;
    q.push(1);
    q.push(2);
    std::cout << "Front: " << q.front() << std::endl;  // Output: 1
    q.pop();
    std::cout << "New Front: " << q.front() << std::endl;  // Output: 2
    return 0;
}
```

---

### **(f) Priority Queue (`std::priority_queue`)**
- **Description:** A container adapter that provides a way to retrieve the largest (by default) element first.
- **Main Methods:**
  - `push(const T&)` / `emplace(args...)`: Insert an element.
  - `pop()`: Remove the top (largest) element.
  - `top()`: Access the largest element.
  - `empty()`, `size()`.
- **Notes:** By default, it behaves like a max-heap. You can customize the comparison function to change the ordering (e.g., to create a min-heap).

**Example:**
```cpp
#include <queue>
#include <vector>
#include <iostream>
#include <functional>  // For std::greater

int main() {
    // Min-heap example:
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    minHeap.push(30);
    minHeap.push(10);
    minHeap.push(20);
    std::cout << "Min element: " << minHeap.top() << std::endl;  // Output: 10
    return 0;
}
```

---

## **2. Associative Data Structures**

### **(a) Set (`std::set`)**
- **Description:** Stores unique keys in sorted order.
- **Main Methods:**
  - `insert(const T&)`: Insert element.
  - `erase(iterator pos)`, `erase(const T&)`: Remove element.
  - `find(const T&)`: Search for an element.
  - `count(const T&)`: Check if an element exists (returns 1 or 0).
  - `lower_bound(const T&)`, `upper_bound(const T&)`: Range queries.
  - `begin()`, `end()`, `size()`, `empty()`, `clear()`.
- **Underlying Implementation:** Typically a self-balancing binary search tree (Red-Black Tree).

**Example:**
```cpp
#include <set>
#include <iostream>

int main() {
    std::set<int> s = {20, 10, 30};
    s.insert(25);
    for (int num : s)
        std::cout << num << " ";  // Output: 10 20 25 30 (sorted)
    return 0;
}
```

---

### **(b) Unordered Set (`std::unordered_set`)**
- **Description:** Stores unique keys without any specific order.
- **Main Methods:** Similar to `std::set` but with average *O(1)* time complexity for insertions and lookups.
- **Underlying Implementation:** Hash table.
- **Example:**
```cpp
#include <unordered_set>
#include <iostream>

int main() {
    std::unordered_set<int> us = {10, 20, 30};
    us.insert(25);
    for (int num : us)
        std::cout << num << " ";  // Order is unspecified
    return 0;
}
```

---

### **(c) Map (`std::map`)**
- **Description:** Stores key-value pairs in sorted order by keys.
- **Main Methods:**
  - `operator[](key)`: Access or insert element.
  - `insert(pair<key, value>)`: Insert a key-value pair.
  - `erase(key or iterator)`: Remove an element.
  - `find(key)`, `count(key)`: Lookup.
  - `lower_bound(key)`, `upper_bound(key)`: Range queries.
  - `begin()`, `end()`, `size()`, `empty()`, `clear()`.
- **Underlying Implementation:** Self-balancing binary search tree (Red-Black Tree).

**Example:**
```cpp
#include <map>
#include <iostream>

int main() {
    std::map<int, std::string> mp;
    mp[1] = "one";
    mp.insert({2, "two"});
    for (const auto &p : mp)
        std::cout << p.first << " => " << p.second << std::endl;
    return 0;
}
```

---

### **(d) Unordered Map (`std::unordered_map`)**
- **Description:** Stores key-value pairs in no particular order.
- **Main Methods:** Similar to `std::map`, but with average *O(1)* access.
- **Underlying Implementation:** Hash table.
- **Example:**
```cpp
#include <unordered_map>
#include <iostream>

int main() {
    std::unordered_map<int, std::string> ump;
    ump[1] = "one";
    ump[2] = "two";
    for (const auto &p : ump)
        std::cout << p.first << " => " << p.second << std::endl;
    return 0;
}
```

---

### **(e) Multiset and Multimap**
- **Multiset:**  
  - **Description:** Similar to `std::set` but allows duplicate elements.
  - **Main Methods:** Same as `std::set` (e.g., `insert()`, `erase()`, `find()`) but `count()` can return more than 1.
  
- **Multimap:**  
  - **Description:** Similar to `std::map` but allows duplicate keys.
  - **Main Methods:** Same as `std::map` (e.g., `insert()`, `erase()`, `find()`) but iterating over a key may yield several values.

**Example (Multiset):**
```cpp
#include <set>
#include <iostream>

int main() {
    std::multiset<int> ms = {10, 20, 20, 30};
    ms.insert(20);
    for (int num : ms)
        std::cout << num << " ";  // Duplicates will be preserved and sorted.
    return 0;
}
```

---

## **3. Other Useful Data Structures**

### **(a) Bitset (`std::bitset`)**
- **Description:** Represents a fixed-size sequence of bits.
- **Main Methods:**
  - `set(pos, bool)`: Set a bit.
  - `reset(pos)`: Reset a bit to 0.
  - `flip(pos)`: Toggle a bit.
  - `test(pos)`: Check if a bit is set.
  - `all()`, `any()`, `none()`: Query overall state.
  - `count()`: Number of set bits.
  - `size()`: Total bits.
- **Use Case:** Memory-efficient storage for flags or binary representations.

**Example:**
```cpp
#include <bitset>
#include <iostream>

int main() {
    std::bitset<8> bits;
    bits.set(3);
    std::cout << "Bits: " << bits << std::endl;
    std::cout << "Number of set bits: " << bits.count() << std::endl;
    return 0;
}
```

---

### **(b) String (`std::string`)**
- **Description:** Although primarily used for text, it is a dynamic sequence of characters.
- **Main Methods:**
  - `append()`, `push_back()`: Add characters.
  - `substr(pos, len)`: Get substring.
  - `find(substring)`: Search for a substring.
  - `size()`, `length()`, `empty()`, `clear()`.
  - `operator[]` and `at(index)`: Element access.
- **Use Case:** Text manipulation and storage.

---

### **(c) Graph Representations**
While not provided as ready-to-use STL containers, graphs can be represented using:
- **Adjacency List:**  
  - Typically implemented as a `std::vector<std::vector<int>>` or `std::vector<std::list<int>>` (for weighted graphs, use pairs or custom structures).
  - **Main Operations:** Adding an edge, traversing neighbors.
- **Adjacency Matrix:**  
  - Implemented as a 2D vector (`std::vector<std::vector<int>>`).
  - **Main Operations:** Edge existence check in constant time, but higher space complexity for sparse graphs.
  
**Example (Adjacency List):**
```cpp
#include <vector>
#include <iostream>

int main() {
    // Graph with 5 vertices (0 to 4)
    std::vector<std::vector<int>> graph(5);
    
    // Adding an edge from vertex 0 to 1 and 4, and from vertex 1 to 2
    graph[0].push_back(1);
    graph[0].push_back(4);
    graph[1].push_back(2);
    
    // Display neighbors of vertex 0
    std::cout << "Neighbors of vertex 0: ";
    for (int neighbor : graph[0])
        std::cout << neighbor << " ";
    std::cout << std::endl;
    return 0;
}
```

---

### **(d) Custom Data Structures**
Beyond the STL, you might implement or use libraries for:
- **Segment Trees / Fenwick Trees:**  
  - **Purpose:** Efficient range queries and updates.
  - **Operations:** Build, update, query (typically *O(log n)* per operation).
- **Trie (Prefix Tree):**  
  - **Purpose:** Fast retrieval for strings (e.g., autocomplete).
  - **Operations:** Insert, search, and delete words.
- **Disjoint Set Union (Union-Find):**  
  - **Purpose:** Track a set of elements partitioned into disjoint subsets (commonly used in graph algorithms).
  - **Operations:** `find()`, `union()`.
- **Custom Linked Lists, Trees, or Hash Tables:**  
  - In many competitive programming or system-design scenarios, you may implement your own versions for fine-tuned performance.


Below are several more advanced examples where we build and use custom data structures. These examples illustrate common techniques in competitive programming and systems design. In particular, we’ll cover:

1. **Segment Tree for Range Queries and Updates**  
2. **Fenwick Tree (Binary Indexed Tree) for Prefix Sum Queries**  
3. **Disjoint Set Union (Union-Find) with Path Compression and Union by Rank**  
4. **Trie (Prefix Tree) for Efficient String Search**

## **1. Segment Tree**

A segment tree is a binary tree used for answering range queries (e.g., range sum, range minimum) and performing point updates efficiently.

### **Example: Range Sum Query and Point Update**

```cpp
#include <iostream>
#include <vector>

class SegmentTree {
private:
    int n;
    std::vector<int> tree;

    // Build tree: node at index 'node' covers segment [start, end]
    void build(const std::vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node, start, mid);
            build(arr, 2 * node + 1, mid + 1, end);
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
    }

    // Query sum in range [l, r]
    int query(int node, int start, int end, int l, int r) {
        // If segment completely outside query range
        if (r < start || end < l)
            return 0;
        // If segment completely inside query range
        if (l <= start && end <= r)
            return tree[node];
        // Otherwise, split into two halves
        int mid = (start + end) / 2;
        int p1 = query(2 * node, start, mid, l, r);
        int p2 = query(2 * node + 1, mid + 1, end, l, r);
        return p1 + p2;
    }

    // Point update: set arr[idx] = value
    void update(int node, int start, int end, int idx, int value) {
        if (start == end) {
            // Leaf node; update element.
            tree[node] = value;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid)
                update(2 * node, start, mid, idx, value);
            else
                update(2 * node + 1, mid + 1, end, idx, value);
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
    }

public:
    SegmentTree(const std::vector<int>& arr) {
        n = arr.size();
        tree.resize(4 * n);
        build(arr, 1, 0, n - 1);
    }

    // Public interface for querying the sum in the range [l, r]
    int query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }

    // Public interface for updating element at index idx
    void update(int idx, int value) {
        update(1, 0, n - 1, idx, value);
    }
};

int main() {
    std::vector<int> arr = {2, 1, 5, 3, 4};
    SegmentTree segTree(arr);

    std::cout << "Sum from index 1 to 3: " << segTree.query(1, 3) << std::endl;  // Expected: 1 + 5 + 3 = 9

    segTree.update(2, 2);  // arr[2] becomes 2; new array: {2, 1, 2, 3, 4}
    std::cout << "Sum from index 1 to 3 after update: " << segTree.query(1, 3) << std::endl;  // Expected: 1 + 2 + 3 = 6

    return 0;
}
```

---

## **2. Fenwick Tree (Binary Indexed Tree)**

A Fenwick tree is a data structure that efficiently supports prefix sum queries and point updates with lower memory overhead compared to a segment tree.

### **Example: Prefix Sum Query**

```cpp
#include <iostream>
#include <vector>

class FenwickTree {
private:
    int n;
    std::vector<int> tree;

public:
    FenwickTree(int size) : n(size) {
        tree.assign(n + 1, 0);
    }

    // Build Fenwick Tree from an initial array
    FenwickTree(const std::vector<int>& arr) : n(arr.size()) {
        tree.assign(n + 1, 0);
        for (int i = 0; i < n; ++i)
            update(i, arr[i]);
    }

    // Add 'delta' to index 'i'
    void update(int i, int delta) {
        i++;  // Convert to 1-based index
        while (i <= n) {
            tree[i] += delta;
            i += i & (-i);  // Move to parent
        }
    }

    // Returns the sum of values from index 0 to i
    int prefixSum(int i) {
        i++;  // Convert to 1-based index
        int sum = 0;
        while (i > 0) {
            sum += tree[i];
            i -= i & (-i);  // Move to parent
        }
        return sum;
    }

    // Range sum query from l to r
    int rangeSum(int l, int r) {
        return prefixSum(r) - (l > 0 ? prefixSum(l - 1) : 0);
    }
};

int main() {
    std::vector<int> arr = {2, 1, 5, 3, 4};
    FenwickTree ft(arr);

    std::cout << "Prefix sum up to index 3: " << ft.prefixSum(3) << std::endl;  // Expected: 2 + 1 + 5 + 3 = 11
    std::cout << "Range sum from index 1 to 3: " << ft.rangeSum(1, 3) << std::endl;  // Expected: 1 + 5 + 3 = 9

    ft.update(2, -3);  // Decrease value at index 2 by 3; new array becomes {2, 1, 2, 3, 4}
    std::cout << "Prefix sum up to index 3 after update: " << ft.prefixSum(3) << std::endl;  // Expected: 2 + 1 + 2 + 3 = 8

    return 0;
}
```

---

## **3. Disjoint Set Union (Union-Find)**

The Union-Find data structure is used to track disjoint sets and is particularly useful in graph algorithms (e.g., finding connected components or cycles).

### **Example: Union-Find with Path Compression and Union by Rank**

```cpp
#include <iostream>
#include <vector>

class UnionFind {
private:
    std::vector<int> parent;
    std::vector<int> rank;  // Used for union by rank

public:
    // Initialize n elements (0 to n-1)
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i)
            parent[i] = i;
    }

    // Find the representative (root) of set that element x belongs to
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);  // Path compression
        return parent[x];
    }

    // Union the sets that contain x and y
    bool unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY)
            return false;  // Already in the same set

        // Union by rank: attach smaller tree under root of larger tree
        if (rank[rootX] < rank[rootY])
            parent[rootX] = rootY;
        else if (rank[rootX] > rank[rootY])
            parent[rootY] = rootX;
        else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        return true;
    }
};

int main() {
    UnionFind uf(5);  // Create 5 disjoint sets: 0, 1, 2, 3, 4

    uf.unionSets(0, 1);
    uf.unionSets(1, 2);
    uf.unionSets(3, 4);

    std::cout << "Are 0 and 2 connected? " << (uf.find(0) == uf.find(2) ? "Yes" : "No") << std::endl;
    std::cout << "Are 0 and 3 connected? " << (uf.find(0) == uf.find(3) ? "Yes" : "No") << std::endl;

    uf.unionSets(2, 3);  // Connect the two components
    std::cout << "After union, are 0 and 4 connected? " << (uf.find(0) == uf.find(4) ? "Yes" : "No") << std::endl;

    return 0;
}
```

---

## **4. Trie (Prefix Tree)**

A trie is a tree-like data structure that is very efficient for storing and searching strings (especially when dealing with prefixes).

### **Example: Trie for Inserting and Searching Words**

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <memory>

// Trie Node definition
struct TrieNode {
    bool isEndOfWord;
    std::unordered_map<char, std::unique_ptr<TrieNode>> children;

    TrieNode() : isEndOfWord(false) {}
};

class Trie {
private:
    std::unique_ptr<TrieNode> root;

public:
    Trie() : root(std::make_unique<TrieNode>()) {}

    // Insert a word into the trie
    void insert(const std::string& word) {
        TrieNode* current = root.get();
        for (char ch : word) {
            if (current->children.find(ch) == current->children.end())
                current->children[ch] = std::make_unique<TrieNode>();
            current = current->children[ch].get();
        }
        current->isEndOfWord = true;
    }

    // Search for a word in the trie
    bool search(const std::string& word) const {
        TrieNode* current = root.get();
        for (char ch : word) {
            if (current->children.find(ch) == current->children.end())
                return false;
            current = current->children.at(ch).get();
        }
        return current->isEndOfWord;
    }

    // Check if there is any word in the trie that starts with the given prefix
    bool startsWith(const std::string& prefix) const {
        TrieNode* current = root.get();
        for (char ch : prefix) {
            if (current->children.find(ch) == current->children.end())
                return false;
            current = current->children.at(ch).get();
        }
        return true;
    }
};

int main() {
    Trie trie;
    trie.insert("hello");
    trie.insert("world");
    trie.insert("helium");

    std::cout << std::boolalpha;
    std::cout << "Search 'hello': " << trie.search("hello") << std::endl;     // true
    std::cout << "Search 'hel': " << trie.search("hel") << std::endl;         // false
    std::cout << "Starts with 'hel': " << trie.startsWith("hel") << std::endl;  // true

    return 0;
}
```

## **1. Sorting and Related Algorithms**

### **`std::sort`**
- **Purpose:** Sorts elements in a range in ascending order (by default) or using a custom comparator.
- **Complexity:** Average-case *O(n log n)*.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {5, 2, 9, 1, 5, 6};
      std::sort(vec.begin(), vec.end());  // Default: ascending order
  
      for (int v : vec)
          std::cout << v << " ";  // Output: 1 2 5 5 6 9
      return 0;
  }
  ```

### **`std::stable_sort`**
- **Purpose:** Like `std::sort`, but maintains the relative order of equivalent elements.
- **Complexity:** *O(n log n)*, but may be slower in practice than `std::sort` due to stability guarantees.

### **`std::partial_sort`**
- **Purpose:** Rearranges the range such that the first *k* elements are the smallest (or largest, with a custom comparator) in sorted order.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {5, 2, 9, 1, 5, 6};
      size_t k = 3;
      std::partial_sort(vec.begin(), vec.begin() + k, vec.end());
  
      // The first 3 elements are sorted (the smallest), but the rest are not guaranteed to be sorted.
      for (int v : vec)
          std::cout << v << " ";
      return 0;
  }
  ```

### **`std::nth_element`**
- **Purpose:** Rearranges the elements such that the element at the nth position is the one that would be in that position in a fully sorted array. All elements before it are less than or equal to it, and all elements after are greater than or equal.
- **Complexity:** Average-case *O(n)*.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {5, 2, 9, 1, 5, 6};
      size_t n = 3;
      std::nth_element(vec.begin(), vec.begin() + n, vec.end());
  
      std::cout << "Element at index " << n << " is " << vec[n] << std::endl;
      return 0;
  }
  ```

---

## **2. Searching Algorithms**

### **`std::find`**
- **Purpose:** Finds the first occurrence of a given value in a range.
- **Complexity:** *O(n)*.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {10, 20, 30, 40};
      auto it = std::find(vec.begin(), vec.end(), 30);
      if (it != vec.end())
          std::cout << "Found 30 at index " << std::distance(vec.begin(), it) << std::endl;
      else
          std::cout << "30 not found." << std::endl;
      return 0;
  }
  ```

### **`std::binary_search`**
- **Purpose:** Checks if an element exists in a sorted range.
- **Complexity:** *O(log n)*.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 5};
      if (std::binary_search(vec.begin(), vec.end(), 3))
          std::cout << "3 is present in the vector." << std::endl;
      else
          std::cout << "3 is not present." << std::endl;
      return 0;
  }
  ```

### **`std::find_if` and `std::find_if_not`**
- **Purpose:** Finds the first element that satisfies (or does not satisfy) a predicate.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {10, 15, 20, 25};
      // Find the first even number.
      auto it = std::find_if(vec.begin(), vec.end(), [](int n) { return n % 2 == 0; });
      if (it != vec.end())
          std::cout << "First even number: " << *it << std::endl;
      return 0;
  }
  ```

### **`std::search` and `std::find_end`**
- **Purpose:** `std::search` finds the first occurrence of a sequence (subrange) within a range. `std::find_end` finds the last occurrence.
- **Example (`std::search`):**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 2, 3, 5};
      std::vector<int> pattern = {2, 3};
      auto it = std::search(vec.begin(), vec.end(), pattern.begin(), pattern.end());
      if (it != vec.end())
          std::cout << "Pattern found at index " << std::distance(vec.begin(), it) << std::endl;
      else
          std::cout << "Pattern not found." << std::endl;
      return 0;
  }
  ```

---

## **3. Modification Algorithms**

### **`std::copy` and `std::copy_if`**
- **Purpose:** Copies elements from one range to another.
- **Example (`std::copy`):**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> source = {1, 2, 3, 4, 5};
      std::vector<int> dest(source.size());
      std::copy(source.begin(), source.end(), dest.begin());
  
      for (int n : dest)
          std::cout << n << " ";  // Output: 1 2 3 4 5
      return 0;
  }
  ```

### **`std::transform`**
- **Purpose:** Applies a function to a range and stores the result in another range.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 5};
      std::vector<int> squared(vec.size());
      std::transform(vec.begin(), vec.end(), squared.begin(), [](int n) { return n * n; });
  
      for (int n : squared)
          std::cout << n << " ";  // Output: 1 4 9 16 25
      return 0;
  }
  ```

### **`std::fill` and `std::fill_n`**
- **Purpose:** Fills a range with a specific value.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec(5);
      std::fill(vec.begin(), vec.end(), 7);
      for (int n : vec)
          std::cout << n << " ";  // Output: 7 7 7 7 7
      return 0;
  }
  ```

### **`std::replace` and `std::replace_if`**
- **Purpose:** Replaces occurrences of a value (or elements satisfying a predicate) with a new value.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 2, 4};
      std::replace(vec.begin(), vec.end(), 2, 5);
  
      for (int n : vec)
          std::cout << n << " ";  // Output: 1 5 3 5 4
      return 0;
  }
  ```

### **`std::remove` and `std::remove_if`**
- **Purpose:** Reorders a range so that elements to be removed are moved to the end, and returns an iterator to the new end. Often used with container’s `erase` method.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 2, 4};
      // Remove all 2's from the vector.
      auto newEnd = std::remove(vec.begin(), vec.end(), 2);
      vec.erase(newEnd, vec.end());
  
      for (int n : vec)
          std::cout << n << " ";  // Output: 1 3 4
      return 0;
  }
  ```

---

## **4. Set Algorithms**

### **`std::set_union`, `std::set_intersection`, `std::set_difference`**
- **Purpose:** These algorithms operate on sorted ranges to compute the union, intersection, or difference between two sets.
- **Example (`std::set_intersection`):**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> a = {1, 2, 3, 4, 5};
      std::vector<int> b = {3, 4, 5, 6, 7};
      std::vector<int> intersection(std::min(a.size(), b.size()));
  
      auto it = std::set_intersection(a.begin(), a.end(), b.begin(), b.end(), intersection.begin());
      intersection.resize(std::distance(intersection.begin(), it));
  
      std::cout << "Intersection: ";
      for (int n : intersection)
          std::cout << n << " ";  // Output: 3 4 5
      return 0;
  }
  ```

---

## **5. Heap Algorithms**

The `<algorithm>` header provides functions for working with heaps (which are underlying structures for priority queues):

### **`std::make_heap`, `std::push_heap`, `std::pop_heap`, `std::sort_heap`**
- **Purpose:** Manage a range of elements as a heap.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> heap = {3, 1, 4, 1, 5, 9, 2, 6};
  
      // Create a max-heap.
      std::make_heap(heap.begin(), heap.end());
      std::cout << "Max element (top of heap): " << heap.front() << std::endl;
  
      // Add an element
      heap.push_back(7);
      std::push_heap(heap.begin(), heap.end());
      std::cout << "New max element: " << heap.front() << std::endl;
  
      // Remove the maximum element
      std::pop_heap(heap.begin(), heap.end());
      heap.pop_back();
      std::cout << "Max element after pop: " << heap.front() << std::endl;
  
      // Heap sort (destroys the heap property)
      std::sort_heap(heap.begin(), heap.end());
      std::cout << "Sorted array: ";
      for (int n : heap)
          std::cout << n << " ";
  
      return 0;
  }
  ```

---

## **6. Other Useful Algorithms**

### **`std::accumulate`** (from `<numeric>`)
- **Purpose:** Computes the sum (or another accumulation) over a range.
- **Example:**
  ```cpp
  #include <numeric>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 5};
      int sum = std::accumulate(vec.begin(), vec.end(), 0);
      std::cout << "Sum: " << sum << std::endl;  // Output: 15
      return 0;
  }
  ```

### **`std::for_each`**
- **Purpose:** Applies a function to each element in a range.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 5};
      std::for_each(vec.begin(), vec.end(), [](int n) {
          std::cout << n << " ";
      });
      return 0;
  }
  ```

### **`std::count` and `std::count_if`**
- **Purpose:** Counts the number of elements equal to a value or satisfying a predicate.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 2, 4};
      int count2 = std::count(vec.begin(), vec.end(), 2);
      std::cout << "Number of 2's: " << count2 << std::endl;
      return 0;
  }
  ```

### **`std::max_element` and `std::min_element`**
- **Purpose:** Finds the maximum or minimum element in a range.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {7, 2, 8, 1, 9};
      auto maxIt = std::max_element(vec.begin(), vec.end());
      auto minIt = std::min_element(vec.begin(), vec.end());
      std::cout << "Max: " << *maxIt << ", Min: " << *minIt << std::endl;
      return 0;
  }
  ```

Let's continue exploring additional standard algorithms and techniques that you might find useful in C++. We'll cover some more algorithms from various categories such as partitioning, merging, unique operations, and even algorithms that work on ranges (introduced in C++20).

---

## **7. Partitioning Algorithms**

Partitioning algorithms reorder elements based on a predicate.

### **`std::partition`**
- **Purpose:** Rearranges elements in a range so that elements satisfying a given predicate come before those that do not.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {7, 2, 8, 1, 9, 4, 6};
      // Partition: even numbers come first, odds later.
      auto it = std::partition(vec.begin(), vec.end(), [](int n) { return n % 2 == 0; });
  
      std::cout << "After partitioning (evens then odds):\n";
      for (int n : vec)
          std::cout << n << " ";
      std::cout << "\nPartition point: " << std::distance(vec.begin(), it) << std::endl;
      return 0;
  }
  ```
  > **Note:** The partitioned range is not sorted; it only guarantees that all elements for which the predicate returns `true` precede the others.

### **`std::stable_partition`**
- **Purpose:** Similar to `std::partition`, but it preserves the relative order of elements in each group.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {7, 2, 8, 1, 9, 4, 6};
      std::stable_partition(vec.begin(), vec.end(), [](int n) { return n % 2 == 0; });
  
      std::cout << "After stable partitioning (evens then odds):\n";
      for (int n : vec)
          std::cout << n << " ";
      std::cout << std::endl;
      return 0;
  }
  ```

---

## **8. Merging and Set Operations**

These algorithms are very useful when dealing with sorted ranges.

### **`std::merge`**
- **Purpose:** Merges two sorted ranges into a single sorted range.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> a = {1, 3, 5, 7};
      std::vector<int> b = {2, 4, 6, 8};
      std::vector<int> merged(a.size() + b.size());
  
      std::merge(a.begin(), a.end(), b.begin(), b.end(), merged.begin());
  
      std::cout << "Merged array: ";
      for (int n : merged)
          std::cout << n << " ";
      std::cout << std::endl;
      return 0;
  }
  ```

### **`std::inplace_merge`**
- **Purpose:** Merges two consecutive sorted ranges within a single container into one sorted range.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 3, 5, 2, 4, 6};
      // Here, [vec.begin(), vec.begin() + 3) and [vec.begin() + 3, vec.end()) are both sorted.
      std::inplace_merge(vec.begin(), vec.begin() + 3, vec.end());
  
      std::cout << "After inplace_merge: ";
      for (int n : vec)
          std::cout << n << " ";
      std::cout << std::endl;
      return 0;
  }
  ```

### **`std::set_symmetric_difference`**
- **Purpose:** Computes the symmetric difference of two sorted ranges.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> a = {1, 2, 3, 4, 5};
      std::vector<int> b = {4, 5, 6, 7, 8};
      std::vector<int> symDiff(std::max(a.size(), b.size()));
  
      auto it = std::set_symmetric_difference(a.begin(), a.end(), b.begin(), b.end(), symDiff.begin());
      symDiff.resize(std::distance(symDiff.begin(), it));
  
      std::cout << "Symmetric difference: ";
      for (int n : symDiff)
          std::cout << n << " ";
      std::cout << std::endl;
      return 0;
  }
  ```

---

## **9. Unique and Removing Duplicates**

### **`std::unique`**
- **Purpose:** Removes consecutive duplicate elements in a sorted or grouped range.
- **Note:** It doesn’t actually change the container size; it returns an iterator to the new end of the "unique" range.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 2, 3, 3, 3, 4, 4, 5};
      auto newEnd = std::unique(vec.begin(), vec.end());
      vec.erase(newEnd, vec.end());  // Erase the non-unique part
  
      std::cout << "Unique elements: ";
      for (int n : vec)
          std::cout << n << " ";
      std::cout << std::endl;
      return 0;
  }
  ```

---

## **10. Partitioning and Searching with Ranges (C++20)**

With C++20, the Standard Library introduces ranges and views, which allow you to write more expressive and concise code. Here are a few examples:

### **Using Ranges for Filtering and Transformation**

You can use the `<ranges>` header to filter and transform ranges:
  
```cpp
#include <iostream>
#include <vector>
#include <ranges>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5, 6};

    // Filter even numbers and then square them.
    auto evenSquares = vec 
                     | std::ranges::views::filter([](int n) { return n % 2 == 0; })
                     | std::ranges::views::transform([](int n) { return n * n; });

    std::cout << "Even squares: ";
    for (int n : evenSquares)
        std::cout << n << " ";  // Output: 4 16 36
    std::cout << std::endl;
    return 0;
}
```

### **Using `std::ranges::sort`**

Sorting can also be done with ranges:
  
```cpp
#include <algorithm>
#include <iostream>
#include <vector>
#include <ranges>

int main() {
    std::vector<int> vec = {5, 2, 9, 1, 5, 6};
    // Use ranges to sort
    std::ranges::sort(vec);
  
    std::cout << "Sorted vector: ";
    for (int n : vec)
        std::cout << n << " ";
    std::cout << std::endl;
    return 0;
}
```

---

## **11. Miscellaneous Algorithms**

### **`std::rotate`**
- **Purpose:** Rotates the elements in a range so that a given element becomes the first element.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 5};
      // Rotate so that element at index 2 (the value 3) becomes the first element.
      std::rotate(vec.begin(), vec.begin() + 2, vec.end());
  
      std::cout << "After rotation: ";
      for (int n : vec)
          std::cout << n << " ";  // Output: 3 4 5 1 2
      std::cout << std::endl;
      return 0;
  }
  ```

### **`std::reverse`**
- **Purpose:** Reverses the order of elements in a range.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 5};
      std::reverse(vec.begin(), vec.end());
  
      std::cout << "Reversed vector: ";
      for (int n : vec)
          std::cout << n << " ";  // Output: 5 4 3 2 1
      std::cout << std::endl;
      return 0;
  }
  ```

### **`std::rotate_copy`**
- **Purpose:** Similar to `std::rotate`, but it copies the result to a new range instead of modifying in place.
- **Example:**
  ```cpp
  #include <algorithm>
  #include <vector>
  #include <iostream>
  
  int main() {
      std::vector<int> vec = {1, 2, 3, 4, 5};
      std::vector<int> rotated(vec.size());
      // Rotate so that element at index 3 (the value 4) becomes the first.
      std::rotate_copy(vec.begin(), vec.begin() + 3, vec.end(), rotated.begin());
  
      std::cout << "Rotated copy: ";
      for (int n : rotated)
          std::cout << n << " ";  // Output: 4 5 1 2 3
      std::cout << std::endl;
      return 0;
  }
  ```
