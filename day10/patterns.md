# SDE II Coding Interview Preparation Roadmap — 30 Days

## Objective

Become interview-ready in 30 days by mastering the most common coding patterns used in SDE II interviews.

### Target Outcome

By the end of 30 days, you should be able to:

* Identify the coding pattern within 5–10 minutes.
* Explain brute-force and optimized solutions.
* Analyze time and space complexity.
* Implement solutions without depending on memorized code.
* Solve medium-level problems independently.
* Handle common hard-level variations.
* Explain your approach clearly during an interview.

---

# Daily Study Structure

Recommended daily time: **3–4 hours**

## Daily Routine

### 1. Learn the Pattern — 30 minutes

Understand:

* What problem does this pattern solve?
* When should you use it?
* What clues indicate this pattern?
* What is the standard template?
* What are common variations?

### 2. Implement the Template — 30 minutes

Implement the pattern from scratch.

Examples:

* Sliding Window template
* Binary Search template
* DFS/BFS template
* Backtracking template
* Dynamic Programming template

### 3. Solve Problems — 2 hours

Solve:

* 1 Easy problem
* 2 Medium problems
* 1 Variation or Hard problem when applicable

### 4. Interview Simulation — 30 minutes

For one problem:

1. Clarify the problem.
2. Explain brute force.
3. Identify the pattern.
4. Explain the optimized approach.
5. Write code.
6. Dry run with an example.
7. Explain complexity.

### 5. Review — 15 minutes

Record:

```text
Problem:
Pattern:
Key Insight:
Mistake:
Time Complexity:
Space Complexity:
What I Should Remember:
```

---

# WEEK 1 — Core Array and String Patterns

---

## Day 1 — HashMap and HashSet

### Learn

* Frequency counting
* Constant-time lookup
* Duplicate detection
* Complement lookup
* HashMap as a cache

### Hands-on

Implement from scratch:

* Frequency counter
* Two Sum
* Duplicate detector
* Character frequency counter

### Problems

1. Two Sum
2. Contains Duplicate
3. Group Anagrams
4. Longest Consecutive Sequence

### Interview Goal

Recognize:

> "I need fast lookup or frequency tracking."

---

## Day 2 — Two Pointers

### Learn

* Opposite-direction pointers
* Same-direction pointers
* Sorted array optimization

### Hands-on

Implement:

```text
left = 0
right = n - 1
```

Practice:

* Move left
* Move right
* Move both pointers

### Problems

1. Valid Palindrome
2. Two Sum II
3. 3Sum
4. Container With Most Water

### Interview Goal

Recognize:

> Sorted array + pair/triplet relationship = Two Pointers

---

## Day 3 — Sliding Window

### Learn

* Fixed-size window
* Variable-size window
* Frequency map inside a window

### Hands-on

Implement:

```text
left = 0

for right in range(n):
    add right element

    while condition is invalid:
        remove left element
        left++

    update answer
```

### Problems

1. Maximum Average Subarray I
2. Longest Substring Without Repeating Characters
3. Longest Repeating Character Replacement
4. Minimum Window Substring

### Interview Goal

Recognize:

> Contiguous subarray or substring + optimization = Sliding Window

---

## Day 4 — Prefix Sum

### Learn

* Prefix sum arrays
* Range sum
* Prefix sum + HashMap

### Hands-on

Implement:

```text
prefix[i] = prefix[i - 1] + nums[i]
```

### Problems

1. Range Sum Query
2. Subarray Sum Equals K
3. Product of Array Except Self
4. Continuous Subarray Sum

### Interview Goal

Recognize:

> Repeated range calculations or subarray sum conditions.

---

## Day 5 — Binary Search

### Learn

* Standard binary search
* First and last occurrence
* Search space reduction

### Hands-on

Implement:

```text
while left <= right:
    mid = left + (right - left) / 2
```

### Problems

1. Binary Search
2. Search in Rotated Sorted Array
3. Find Minimum in Rotated Sorted Array
4. Koko Eating Bananas

### Interview Goal

Ask:

> Can I eliminate half of the possible answers?

---

## Day 6 — Binary Search on Answer

### Learn

* Minimum possible answer
* Maximum possible answer
* Feasibility function

### Hands-on

Implement:

```text
low = minimum_possible_answer
high = maximum_possible_answer

while low <= high:
    mid = ...

    if feasible(mid):
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
```

### Problems

1. Koko Eating Bananas
2. Capacity to Ship Packages Within D Days
3. Split Array Largest Sum

### Interview Goal

Recognize:

> Minimize the maximum or maximize the minimum.

---

## Day 7 — Week 1 Review and Mock Interview

### Hands-on

Without looking at templates, implement:

* HashMap solution
* Two Pointers
* Sliding Window
* Prefix Sum
* Binary Search

### Mock Problems

1. 3Sum
2. Longest Substring Without Repeating Characters
3. Search in Rotated Sorted Array

### Goal

Solve:

* 2 Medium problems in 90 minutes
* Explain the pattern before coding

---

# WEEK 2 — Linked Lists, Stacks, Heaps, and Intervals

---

## Day 8 — Linked List Fundamentals

### Learn

* Node manipulation
* Dummy nodes
* Pointer reassignment
* In-place modification

### Hands-on

Implement:

* Insert node
* Delete node
* Reverse linked list
* Merge two linked lists

### Problems

1. Reverse Linked List
2. Merge Two Sorted Lists
3. Remove Nth Node From End
4. Reorder List

---

## Day 9 — Fast and Slow Pointers

### Learn

* Cycle detection
* Finding the middle
* Finding cycle entry point

### Problems

1. Linked List Cycle
2. Linked List Cycle II
3. Middle of the Linked List
4. Palindrome Linked List

### Interview Goal

Recognize:

> Different pointer speeds can reveal structure.

---

## Day 10 — Stack

### Learn

* LIFO
* Matching parentheses
* Expression processing
* Stack-based state tracking

### Problems

1. Valid Parentheses
2. Min Stack
3. Evaluate Reverse Polish Notation
4. Decode String

---

## Day 11 — Monotonic Stack

### Learn

* Increasing stack
* Decreasing stack
* Next greater element
* Previous smaller element

### Hands-on

Implement:

```text
while stack is not empty
and current > stack.top:
    process stack.top
    pop
```

### Problems

1. Daily Temperatures
2. Next Greater Element
3. Largest Rectangle in Histogram
4. Trapping Rain Water

---

## Day 12 — Heap / Priority Queue

### Learn

* Min Heap
* Max Heap
* Top K pattern
* K-way merge

### Problems

1. Kth Largest Element
2. Top K Frequent Elements
3. K Closest Points to Origin
4. Find Median from Data Stream

### Interview Goal

Recognize:

> I repeatedly need the minimum, maximum, or top K items.

---

## Day 13 — Intervals

### Learn

* Sorting intervals
* Overlap detection
* Merge intervals
* Sweep-line thinking

### Problems

1. Merge Intervals
2. Insert Interval
3. Non-overlapping Intervals
4. Meeting Rooms II

### Standard Strategy

```text
Sort by start time
↓
Compare current interval with previous interval
↓
Merge or process overlap
```

---

## Day 14 — Week 2 Review and Mock Interview

### Mock Problems

1. Reorder List
2. Daily Temperatures
3. Merge Intervals
4. Top K Frequent Elements

### Target

Solve 2 medium problems within 75–90 minutes.

---

# WEEK 3 — Trees, Graphs, and Backtracking

---

## Day 15 — Binary Tree DFS

### Learn

* Preorder
* Inorder
* Postorder
* Recursive tree thinking

### Problems

1. Maximum Depth of Binary Tree
2. Diameter of Binary Tree
3. Path Sum
4. Lowest Common Ancestor

---

## Day 16 — Binary Tree BFS

### Learn

* Queue-based traversal
* Level-order processing
* Level-specific state

### Problems

1. Binary Tree Level Order Traversal
2. Binary Tree Right Side View
3. Binary Tree Zigzag Level Order Traversal
4. Minimum Depth of Binary Tree

---

## Day 17 — Binary Search Tree

### Learn

```text
Left < Root < Right
```

### Problems

1. Validate Binary Search Tree
2. Kth Smallest Element in a BST
3. Lowest Common Ancestor of BST
4. Delete Node in a BST

---

## Day 18 — Graph DFS and BFS

### Learn

* Adjacency list
* Visited set
* Connected components
* Grid traversal

### Problems

1. Number of Islands
2. Clone Graph
3. Pacific Atlantic Water Flow
4. Word Ladder

### Hands-on

Implement:

```text
graph = Map<Node, List<Node>>
visited = Set<Node>
```

---

## Day 19 — Topological Sort

### Learn

* Directed graphs
* Indegree
* Dependency resolution
* Cycle detection

### Implement

1. BFS + Kahn's Algorithm
2. DFS + Cycle Detection

### Problems

1. Course Schedule
2. Course Schedule II
3. Alien Dictionary

### Interview Goal

Recognize:

> Prerequisites, dependencies, ordering, build systems.

---

## Day 20 — Union Find

### Learn

* Parent array
* Path compression
* Union by rank
* Connected components

### Implement

```text
find(x)
union(x, y)
```

### Problems

1. Number of Provinces
2. Redundant Connection
3. Accounts Merge
4. Number of Connected Components

---

## Day 21 — Backtracking

### Learn

```text
choose
explore
undo
```

### Problems

1. Subsets
2. Permutations
3. Combination Sum
4. Word Search
5. N-Queens

### Interview Goal

Recognize:

> Generate all valid possibilities.

---

# WEEK 4 — Dynamic Programming, Greedy, Trie, and Design Patterns

---

## Day 22 — 1D Dynamic Programming

### Learn

1. Define the state.
2. Find the recurrence.
3. Define the base case.
4. Determine traversal order.

### Problems

1. Climbing Stairs
2. House Robber
3. House Robber II
4. Coin Change

### Template

```text
dp[i] = best answer using first i elements
```

---

## Day 23 — 2D Dynamic Programming

### Learn

* Grid DP
* State transitions
* Memoization
* Tabulation

### Problems

1. Unique Paths
2. Minimum Path Sum
3. Longest Common Subsequence
4. Edit Distance

---

## Day 24 — Knapsack and Subset DP

### Learn

* 0/1 Knapsack
* Subset selection
* Target sum
* Boolean DP

### Problems

1. Partition Equal Subset Sum
2. Target Sum
3. Coin Change II
4. 0/1 Knapsack

### Interview Goal

Recognize:

> Choose or don't choose each item.

---

## Day 25 — Greedy Algorithms

### Learn

* Local optimal decisions
* Sorting + greedy
* Proof of correctness

### Problems

1. Jump Game
2. Jump Game II
3. Gas Station
4. Partition Labels
5. Non-overlapping Intervals

---

## Day 26 — Trie

### Learn

* Prefix tree
* Insert
* Search
* Prefix matching

### Implement

```text
insert(word)
search(word)
startsWith(prefix)
```

### Problems

1. Implement Trie
2. Design Add and Search Words
3. Word Search II
4. Replace Words

---

## Day 27 — Data Structure Design

### Learn

How to combine data structures.

### Implement from Scratch

#### LRU Cache

```text
HashMap
+
Doubly Linked List
```

#### Time-Based Key-Value Store

```text
HashMap
+
Binary Search
```

### Problems

1. LRU Cache
2. LFU Cache
3. Time-Based Key-Value Store
4. Insert Delete GetRandom O(1)

---

## Day 28 — Advanced Pattern Review

Review:

* Monotonic Stack
* Binary Search on Answer
* Topological Sort
* Union Find
* Trie
* Backtracking
* Advanced DP

### Hands-on

Implement all templates without reference.

### Solve

1. Largest Rectangle in Histogram
2. Course Schedule
3. Word Search II
4. Split Array Largest Sum

---

# DAY 29 — Full SDE II Mock Interview

## Mock Round 1 — 45 Minutes

Choose one:

* Minimum Window Substring
* Number of Islands
* LRU Cache
* Course Schedule

## Mock Round 2 — 45 Minutes

Choose one:

* Coin Change
* Merge K Sorted Lists
* Word Search
* Kth Largest Element

## Mock Round 3 — 45 Minutes

Choose one:

* Trapping Rain Water
* Longest Increasing Subsequence
* Accounts Merge
* Design Twitter

### Interview Evaluation

For every problem, evaluate:

```text
Problem Understanding: /10
Pattern Recognition: /10
Approach Explanation: /10
Coding: /10
Complexity Analysis: /10
Edge Cases: /10
Communication: /10
```

---

# DAY 30 — Final Revision and Interview Readiness

## Morning — Pattern Recognition

Look at problem descriptions only.

Identify the pattern:

| Problem Clue                           | Pattern                 |
| -------------------------------------- | ----------------------- |
| Longest substring                      | Sliding Window          |
| Sorted array + pair                    | Two Pointers            |
| Kth largest                            | Heap                    |
| Next greater element                   | Monotonic Stack         |
| Prerequisites                          | Topological Sort        |
| Connected components                   | Union Find              |
| All combinations                       | Backtracking            |
| Optimal result from previous decisions | DP                      |
| Minimum possible maximum               | Binary Search on Answer |
| Prefix matching                        | Trie                    |

---

## Afternoon — Coding Templates

Implement from memory:

* HashMap
* Two Pointers
* Sliding Window
* Prefix Sum
* Binary Search
* Linked List Reversal
* Fast/Slow Pointers
* Stack
* Monotonic Stack
* Heap
* Tree DFS
* Tree BFS
* Graph DFS
* Graph BFS
* Topological Sort
* Union Find
* Backtracking
* 1D DP
* 2D DP
* Trie
* LRU Cache

---

## Evening — Final Interview Simulation

Solve 3 unseen problems:

### Problem 1 — Array/String

45 minutes

### Problem 2 — Tree/Graph

45 minutes

### Problem 3 — DP/Design

45 minutes

---

# Problem-Solving Framework

Use this framework for every interview problem.

## Step 1 — Clarify

Ask:

* What are the input constraints?
* Can input be empty?
* Are duplicates allowed?
* Is the input sorted?
* Is the result unique?
* Can I modify the input?

---

## Step 2 — Identify the Pattern

Ask:

```text
Is this about:

Subarray / substring?
→ Sliding Window

Sorted data?
→ Two Pointers / Binary Search

Top K?
→ Heap

Next greater/smaller?
→ Monotonic Stack

Dependencies?
→ Topological Sort

Connected components?
→ Union Find / DFS / BFS

All possible combinations?
→ Backtracking

Optimal decisions?
→ Dynamic Programming
```

---

## Step 3 — Explain Brute Force

Always explain:

```text
The straightforward solution is...
Its time complexity is...
The bottleneck is...
```

---

## Step 4 — Optimize

Explain:

```text
The repeated work is...
We can avoid it using...
Therefore the optimized complexity is...
```

---

## Step 5 — Code

Write clean code.

Prioritize:

* Meaningful variable names
* Small functions
* Correct edge case handling
* No unnecessary cleverness

---

## Step 6 — Dry Run

Use:

* Normal case
* Edge case
* Empty input
* Duplicate values
* Single element

---

## Step 7 — Complexity

Always finish with:

```text
Time Complexity: O(...)
Space Complexity: O(...)
```

---

# Daily Tracking Template

Create one file per day:

```text
day-01-hashmap.md
day-02-two-pointers.md
day-03-sliding-window.md
```

Use this format:

```markdown
# Day X — Pattern Name

## Pattern

## When to Use

## Recognition Signals

## Template

## Problems Solved

### Problem 1

- Link:
- Difficulty:
- Approach:
- Pattern:
- Time Complexity:
- Space Complexity:
- Mistake:

## Problems I Could Not Solve

## Key Learnings

## Interview Explanation

## Revisit Date
```

---

# 30-Day Target

## Minimum Target

```text
75–90 Problems
20+ Core Patterns
20+ Implemented Templates
8–10 Mock Interviews
```

## Recommended Distribution

| Category                | Target |
| ----------------------- | -----: |
| Arrays / Strings        |     15 |
| Linked Lists            |      6 |
| Stack / Monotonic Stack |      6 |
| Heap                    |      5 |
| Intervals               |      5 |
| Trees                   |     10 |
| Graphs                  |     10 |
| Backtracking            |      5 |
| Dynamic Programming     |     12 |
| Trie                    |      3 |
| Data Structure Design   |      5 |

---

# Final SDE II Readiness Checklist

You are ready to start interviewing when you can:

* Identify the pattern in 5–10 minutes.
* Solve common medium problems in 25–35 minutes.
* Explain brute force and optimized solutions.
* Write code without looking at templates.
* Handle edge cases proactively.
* Analyze complexity correctly.
* Solve unfamiliar variations.
* Explain your solution clearly.
* Complete two coding problems in a 60–90 minute interview.

---

# Most Important Rule

Do not ask:

> "Have I solved this exact problem before?"

Ask:

> "What underlying pattern does this problem use?"

The objective of this 30-day roadmap is not to memorize 100 solutions.

The objective is to build the ability to recognize:

```text
Problem
   ↓
Pattern
   ↓
Template
   ↓
Variation
   ↓
Optimized Solution
```

That is the skill required for SDE II coding interviews.
