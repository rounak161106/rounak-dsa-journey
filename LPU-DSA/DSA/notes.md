A comprehensive breakdown of time complexities, underlying behaviors, and technical differences between standard `arrays`, `ArrayList`, and `LinkedList` in Java.

---

| Operation | Array | ArrayList | LinkedList | Technical Notes |
| :--- | :---: | :---: | :---: | :--- |
| **Access by Index** (`get(i)`) | **O(1)** | **O(1)** | **O(N)** | Arrays jump directly using math. `LinkedList` must crawl node-by-node. |
| **Search by Value** (contains `X`) | **O(N)** | **O(N)** | **O(N)** | Requires a linear loop scan across the data until a matching element is found. |
| **Search by Value (Sorted)** | **O(log N)** | **O(log N)** | **O(N)** | Arrays support Binary Search. `LinkedList` cannot efficiently perform it. |
| **Insert / Delete at Front** | N/A | **O(N)** | **O(1)** | `ArrayList` shifts every element right/left. `LinkedList` re-links 2 pointers. |
| **Insert / Delete at End** | N/A | **O(1)** amortized | **O(1)** | `ArrayList` is O(1) unless it triggers a resize. `LinkedList` holds a tail pointer. |
| **Insert / Delete in Middle** | N/A | **O(N)** | **O(N)** | `ArrayList` spends time shifting data. `LinkedList` spends time traversing to the spot. |

---
if we write int[] arr = {1,2,3}, array(not arraylist) is created with size 3(fixed size). if we want to create arryalist we have to create that explicitly. 


we have 2 different things, abstract data types and data structures. ADT are the interfaces which defines the behaviour and its actual implementation of that concept is called as the DS. eg. queue is an interface but its actual implementation using linked list or arrays are called data structures. so eg. of ADT are list, stack, queue. eg. of DS are Array, Linked List, Binary Search Tree, Hash Table.

## Stack
- we have push(), pop(), peek(), isEmpty(), search(element) -> searches position starting from top with 1, if not found returns -1
- if we try to `push` or `pop` and completely filled or empty stack, we get `StackOverflowException` or `StackUnderflowException` resp.
- stack is a class and not an interface in java.
- to define we write : 
stack<Integer> stack = new Stack();
stack<String> stack = new Stack();
stack<Person> stack = new Stack(); // if we have a class Person and want a stack of class person type