"""
========================================
        PYTHON SETS - विस्तृत Tutorial
========================================
"""

# ========== 1. EMPTY DICTIONARY vs EMPTY SET ==========
d = {}      # यह एक EMPTY DICTIONARY बनाता है
print("Empty Dictionary:", d)
print("Type of d:", type(d))  # <class 'dict'>

# सही तरीका - Empty Set बनाना
s = set()   # set() से बनाया जाता है, {} नहीं!
print("Empty Set:", s)
print("Type of s:", type(s))  # <class 'set'>


# ========== 2. SET WITH ELEMENTS ==========
# Set में duplicates automatically हटा दिए जाते हैं
s = {1, 5, 32, 54, 5, 5, 5}
print("\nSet with elements:", s)
# Output: {1, 5, 32, 54}  ← 5 को 4 बार डाला पर सिर्फ 1 बार आया!


# ========== 3. STRINGS का SET ==========
fruit_set = {'apple', 'banana', 'apple', 'orange'}
print("Fruit Set:", fruit_set)
# Output: {'apple', 'banana', 'orange'}  ← 'apple' duplicate हटा दिया गया


# ========== 4. NUMBERS का SET ==========
numbers = {10, 20, 30, 10, 20}
print("Numbers Set:", numbers)
# Output: {10, 20, 30}


# ========== 5. SET OPERATIONS (मुख्य operations) ==========
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\n--- SET OPERATIONS ---")
print("Set1:", set1)
print("Set2:", set2)

# UNION (सभी elements को मिलाना)
union_result = set1 | set2
print("\nUnion (|):", union_result)  # {1, 2, 3, 4, 5, 6}

# INTERSECTION (common elements - जो दोनों में हों)
intersection_result = set1 & set2
print("Intersection (&):", intersection_result)  # {3, 4}

# DIFFERENCE (set1 में हैं पर set2 में नहीं)
difference_result = set1 - set2
print("Difference (-):", difference_result)  # {1, 2}

# SYMMETRIC DIFFERENCE (सिर्फ एक जगह हों, दोनों में नहीं)
sym_diff = set1 ^ set2
print("Symmetric Difference (^):", sym_diff)  # {1, 2, 5, 6}


# ========== 6. ADD और REMOVE OPERATIONS ==========
s = {1, 2, 3}
print("\n--- ADD/REMOVE ---")
print("Original Set:", s)

# Element ADD करना
s.add(4)
print("After add(4):", s)  # {1, 2, 3, 4}

# Element REMOVE करना
s.remove(2)
print("After remove(2):", s)  # {1, 3, 4}

# Multiple elements add करना
s.update([5, 6, 7])
print("After update([5,6,7]):", s)  # {1, 3, 4, 5, 6, 7}


# ========== 7. MEMBERSHIP CHECK (कोई element है या नहीं) ==========
print("\n--- MEMBERSHIP CHECK ---")
my_set = {'apple', 'banana', 'orange'}
print("Set:", my_set)
print("'apple' in my_set:", 'apple' in my_set)  # True
print("'mango' in my_set:", 'mango' in my_set)  # False


# ========== 8. SET LENGTH ==========
print("\n--- LENGTH ---")
my_set = {10, 20, 30, 40}
print("Set:", my_set)
print("Length:", len(my_set))  # 4


# ========== 9. CLEAR और POP ==========
print("\n--- CLEAR & POP ---")
temp_set = {1, 2, 3, 4}
print("Original:", temp_set)

# POP करना (कोई भी एक element निकाल देता है)
removed = temp_set.pop()
print("After pop():", temp_set)
print("Removed element:", removed)

# CLEAR करना (सभी elements हटा देता है)
temp_set.clear()
print("After clear():", temp_set)  # set()


# ========== 10. SET का PRACTICAL USE CASE ==========
print("\n--- PRACTICAL EXAMPLE ---")
# Duplicate numbers निकालना
numbers = [1, 2, 3, 2, 4, 3, 5, 1, 2]
print("Original list:", numbers)

unique_numbers = set(numbers)
print("Unique numbers (set):", unique_numbers)

unique_list = list(unique_numbers)
print("Back to list:", unique_list)


# ========== QUICK SUMMARY ==========
print("\n" + "="*50)
print("DICTIONARY vs SET - फर्क समझो!")
print("="*50)
print("Dictionary: d = {} या d = {'key': 'value'}")
print("Set: s = set() या s = {1, 2, 3}")
print("\nSet की विशेषताएं:")
print("✓ Unordered (कोई fixed order नहीं)")
print("✓ Unique elements (duplicates नहीं)")
print("✓ Mutable (add/remove कर सकते हो)")
print("✓ Fast lookups के लिए बेहतरीन!")
print("="*50)
