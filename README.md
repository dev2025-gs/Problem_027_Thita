# Valid Parentheses

## 🔗 Problem Link
https://leetcode.com/problems/valid-parentheses/

## 🧩 Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every closing bracket has a corresponding open bracket of the same type.

---

## 🧪 Examples

### Example 1
**Input:**

s = "()"

**Output:**

true


### Example 2
**Input:**

s = "()[]{}"

**Output:**

true


### Example 3
**Input:**

s = "(]"

**Output:**

false

---

## ⚙️ Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of characters `'()[]{}'`

---

## 💡 Approach

This problem can be efficiently solved using a **stack**.

### Key Idea:
- Use a stack to keep track of opening brackets.
- When encountering an opening bracket (`(`, `{`, `[`), push it onto the stack.
- When encountering a closing bracket (`)`, `}`, `]`):
  - Check if the stack is empty → invalid.
  - Pop the top element and verify it matches the corresponding opening bracket.
- At the end:
  - If the stack is empty → valid.
  - Otherwise → invalid.

---

## 🧠 Algorithm

1. Initialize an empty stack.
2. Create a mapping of closing brackets to their corresponding opening brackets.
3. Iterate through each character in the string:
   - If it's an opening bracket → push to stack.
   - If it's a closing bracket:
     - Check if stack is empty or top doesn't match → return `false`.
     - Otherwise, pop from stack.
4. After iteration:
   - Return `true` if stack is empty, else `false`.

---

## 🧮 Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each character is processed once.

- **Space Complexity:** `O(n)`
  - In the worst case, all characters are opening brackets stored in the stack.
