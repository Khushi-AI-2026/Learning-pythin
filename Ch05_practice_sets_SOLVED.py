# ==========================================
# CHAPTER 5 - PRACTICE SETS - SOLUTIONS
# ==========================================

# ==========================================
# PROBLEM 1: Hindi words dictionary banao with English translation
# ==========================================
print("===== PROBLEM 1 =====")
print("Hindi words ka dictionary banao with English translation\n")

# GALAT CODE (Original mein):
# words = (
#     "madad": "help"      # ← Syntax error! Brackets galat hain
#     "kursi": "chair"     # ← Commas missing hain
#     "billi": "cat"
# )

# SAHI CODE:
words = {
    "madad": "help",        # Dictionary ke liye curly braces {} use karo
    "kursi": "chair",       # Aur har item ke baad comma lagao
    "billi": "cat"
}

word = input("Enter the word you want meaning of (madad/kursi/billi): ")

if word in words:
    print(f"'{word}' ka matlab: {words[word]}")
else:
    print(f"'{word}' dictionary mein nahi hai!")

# ==========================================
# PROBLEM 2: Input 8 numbers aur unique numbers display karo
# ==========================================
print("\n===== PROBLEM 2 =====")
print("8 numbers input karo aur unique numbers display karo\n")

# Step 1: 8 numbers user se input lo
numbers = set()
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.add(num)

# Step 2: Unique numbers already set mein hote hain (duplicates automatically remove ho jaate hain)
print(f"\nYe unique numbers hain: {numbers}")
print(f"Total unique numbers: {len(numbers)}")

# ==========================================
# PROBLEM 3: Kya set mein 18(int) aur "18"(str) dono ho sakte hain?
# ==========================================
print("\n===== PROBLEM 3 =====")
print("Kya set mein 18(int) aur '18'(str) dono ho sakte hain?\n")

# Answer: HAAN! Bilkul ho sakte hain kyunki dono different types hain
s = {18, "18"}
print(f"Set: {s}")
print(f"18 (integer) aur '18' (string) dono alag-alag elements hain")
print(f"Kyunki: type(18) = {type(18)} aur type('18') = {type('18')}")
print(f"Set ki length: {len(s)} (dono different hain)")

# ==========================================
# PROBLEM 4: Set S ki length kya hogi?
# ==========================================
print("\n===== PROBLEM 4 =====")
print("Set S ki length kya hogi?\n")

# Note: Problem mein 'add' method galat likha hai, sahi syntax hota hai 'add()'
s = set()
print(f"s = set() → s = {s}, length = {len(s)}")

s.add(20)
print(f"s.add(20) → s = {s}, length = {len(s)}")

s.add(20.0)
print(f"s.add(20.0) → s = {s}, length = {len(s)}")
# Note: 20 aur 20.0 mathematically equal hote hain, to set mein duplicate nahi hoga

s.add("20")
print(f"s.add('20') → s = {s}, length = {len(s)}")

print(f"\nFinal answer: Set S ki length = {len(s)}")
print("Kyunki:")
print("  - 20 aur 20.0 dono same hain (mathematically equal)")
print("  - '20' (string) alag element hai")
print(f"  - Total unique elements: {len(s)}")

# ==========================================
# PROBLEM 5: s = 0 to s ki type kya hogi?
# ==========================================
print("\n===== PROBLEM 5 =====")
print("s = 0 to s ki type kya hogi?\n")

s = 0
print(f"s = {s}")
print(f"Type of s: {type(s)}")
print(f"Answer: s ki type '<class 'int'>' hai, 'set' nahi!")
print("Note: Empty set banane ke liye set() use karo, 0 nahi!")

# ==========================================
# PROBLEM 6: Empty dictionary banao - 4 friends ka favorite language
# ==========================================
print("\n===== PROBLEM 6 =====")
print("4 friends ka favorite language dictionary mein store karo\n")

# Method 1: Manual entry
# languages = {}
# languages["Alice"] = "Python"
# languages["Bob"] = "JavaScript"
# languages["Charlie"] = "Java"
# languages["Diana"] = "C++"

# Method 2: User input (Better approach)
languages = {}
for i in range(4):
    name = input(f"Enter friend {i+1}'s name: ")
    language = input(f"Enter {name}'s favorite programming language: ")
    languages[name] = language

print(f"\nFriends aur unki favorite languages:")
print(languages)

# ==========================================
# PROBLEM 7: Agar 2 friends ke naam same ho to kya hoga?
# ==========================================
print("\n===== PROBLEM 7 =====")
print("Agar 2 friends ke naam same ho to kya hoga?\n")

languages = {}
languages["Alice"] = "Python"
languages["Bob"] = "JavaScript"
languages["Alice"] = "Java"  # Same name Alice, but different language

print(f"Dictionary: {languages}")
print("\nJo hota hai:")
print("  - Dictionary mein keys unique hoti hain")
print("  - Agar same key se naya value assign karo, to PURANA VALUE replace ho jaata hai")
print(f"  - Islie Alice ki value 'Java' ho gayi (Python replace ho gaya)")

# ==========================================
# PROBLEM 8: Agar 2 friends ki language same ho to kya hoga?
# ==========================================
print("\n===== PROBLEM 8 =====")
print("Agar 2 friends ki language same ho to kya hoga?\n")

languages = {}
languages["Alice"] = "Python"
languages["Bob"] = "Python"      # Same language, different names
languages["Charlie"] = "Python"

print(f"Dictionary: {languages}")
print("\nJo hota hai:")
print("  - Values ko repetition ho sakti hai, koi problem nahi!")
print("  - Dictionary sirf keys ko unique rakhta hai")
print("  - Multiple people ek hi language prefer kar sakte hain")
print(f"  - Islie kisi ko problem nahi hota")

# ==========================================
# PROBLEM 9: Kya list ko change kar sakte ho jo set mein ho?
# ==========================================
print("\n===== PROBLEM 9 =====")
print("Kya list ko change kar sakte ho jo set mein ho?\n")

a = {8, 7, 17, "khushi", (1, 2)}
print(f"Original set: {a}")

# List set mein directly nahi ho sakti kyunki list MUTABLE hai
# Par tuple ho sakti hai kyunki tuple IMMUTABLE hai

print("\nJavab: NAHI! Nahi kar sakte:")
print("  - Set mein sirf IMMUTABLE objects ho sakte hain")
print("  - List MUTABLE hai, to set mein nahi ho sakti")
print("  - Agar list add karne ki koshish karo to ERROR aayega")

# Yeh GALAT hoga:
# a.add([1, 2])  # ERROR: unhashable type: 'list'

# Lekin TUPLE (jo immutable hai) already set mein ho sakti hai:
print(f"  - (1, 2) tuple set mein hai aur ye immutable hai")
print(f"  - Tuple ke values change nahi ho sakte")

# Demonstrate:
print("\nExample:")
t = (1, 2)
print(f"Tuple: {t} - Immutable, set mein use ho sakta hai ✓")

l = [1, 2]
print(f"List: {l} - Mutable, set mein use NAHI ho sakta ✗")

# ==========================================
# SUMMARY
# ==========================================
print("\n" + "="*50)
print("SUMMARY - IMPORTANT POINTS")
print("="*50)
print("""
1. DICTIONARY:
   - Curly braces {} use karo
   - Key: Value pairs hote hain
   - Keys unique hoti hain

2. SET:
   - Curly braces {} ya set() use karo
   - Duplicates automatically remove ho jaate hain
   - Unordered collection

3. IMMUTABLE vs MUTABLE:
   - IMMUTABLE (set mein use ho sakte hain): int, str, tuple
   - MUTABLE (set mein nahi ho sakte): list, dict

4. SET OPERATIONS:
   - add(): element add karne ke liye
   - remove(): element remove karne ke liye
   - len(): size check karne ke liye

5. MATHEMATICAL EQUALITY IN SETS:
   - 20 == 20.0 (both same in set)
   - 20 != "20" (different types, different elements)
""")
print("="*50)
