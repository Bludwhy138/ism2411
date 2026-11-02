"""
Self-Assessment

1. The first bug I noticed in broken_sales.py was the missing colon in the for-loop.
I caught it by reading the traceback and then checking the loop line. It showed me
I’m getting better at spotting basic syntax issues before asking for help. Sort of...
we may or may not have talked about it in class.

2. apply_discount(price, tier) takes a price and a customer tier, checks which tier
they are, and returns the correct discounted price. Someone else could use it easily
because the inputs and output are straightforward.

3. AI Disclosure: I used AI to help explain the bugs and to help me write cleaner
comments. The debugging steps and final fixes were done by me. Also when writing the 
self assesment questions it was interfering with my code, and so i asked copilot why 
this was happening, and im pretty sure it wasn't understanding what i was trying to say
and mentioned my vs code color theme, and to add three quotes to each side, and I suppose
whatever works works.
"""

# Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")

# Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

# Step by step trace
price = 200
tier = "gold"
tax_rate = 0.07

discounted = apply_discount(price, tier)
print(f"After gold discount: ${discounted:.2f}")

taxed_total = discounted + calculate_tax(discounted, tax_rate)
print(f"After tax: ${taxed_total:.2f}")

print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# Exercise 5 ---
# Debug First, Then Ask — corrected version of broken_sales.py

sales = [100, 200, 50, 300, 90]

total = 0

# Bug 1: The for-loop was missing a colon.
# Python requires a colon to mark the beginning of the loop’s block.
# Without it, the interpreter stops immediately with a SyntaxError.
for sale in sales:
    
    # Bug 2: The original code replaced the running total instead of adding to it.
    # Using total = sale throws away all previous values.
    # The correct behavior is to accumulate the sum using +=.
    total += sale

print("Total sales:", total)


# Bug 3: The while-loop used <= len(sales), which goes one step too far.
# When i equals len(sales), the code tries to access sales[len(sales)],
# but the last valid index is len(sales) - 1.
# Changing the condition to < len(sales) keeps the index in bounds.
i = 0
while i < len(sales):
    print("Sale:", sales[i])
    i += 1


# Exercise 6 ---
# Scope experiment

x = 100  # global variable

def double_it():
    x = 999
    # This x is LOCAL to the function. It does NOT change the global x.
    return x * 2

print(x)               # prints the global x (100)
print(double_it())     # prints 999 * 2 = 1998
print(x)               # global x is still 100


# Explanation (in my own words):
# Python keeps variables inside functions separate from variables outside them.
# The x inside double_it() is a completely different variable from the x in the main script.
# Because of scope rules, changing x inside the function does NOT affect the global x.
# The only way for a function to send data back is through return.
