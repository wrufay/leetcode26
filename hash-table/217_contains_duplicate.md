# 217. Contains Duplicate
### Easy

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

---

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

---

**Example 2:**

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

---

**Example 3:**

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

---

# Method
1. Understand before anything else
- The input is an integer array, and the output is a boolean.
- In own words: We want to return `true` if the array `nums` contains a duplicate number, and `false` otherwise.
2. Extract constraints
- The array is not sorted, not ordered. It contains at least one element

3. Pattern-match from constraints -> data structure
- Hash SET, since we are not dealing with order, and do not need keys and values (only want to see if a value exists or not)
4. Think about steps/algorithm (pseudocode)
- Create an empty hash set
- Loop through the `nums` array
    - At each element, check if that number already exists in the hashmap.
    - If it does - short circuit, return `true`
    - Otherwise, add that element to the hashmap and proceed looping through the array.
    - Once we've looped through the entire array and no duplicate is found, return `false`

## Notes
- Note the difference between hash set and hash map
- Technically don't need an `else` clause.

--- 

# Submission
### O(n) time complexity + O(n) space complexity