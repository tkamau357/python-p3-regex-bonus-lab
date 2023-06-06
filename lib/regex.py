import re

my_pattern = r""
my_regex = re.compile(my_pattern)

text = "It's such a lovely day today."
pattern = r"It's such a lovely day today"
match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("No match found.")


text2 = "Some weather we're having today, huh?"
pattern2 = r"Some weather we're having today, huh\?"
match = re.search(pattern2, text2)

if match:
    print("Match found!")
else:
    print("No match found.")


text3 = "Maybe today's just not my day."
pattern3 = r"Maybe today's just not my day\."
match = re.search(pattern3, text3)

if match:
    print("Match found!")
else:
    print("No match found.")


text4 = "It's such a lovely day today. Some weather we're having today, huh? Maybe today's just not my day. Another random sentence."

# The list of target strings
target_strings = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day."
]

# Construct the regex pattern to match the target strings exactly
pattern4 = "|".join(re.escape(string) for string in target_strings)

# Matching the pattern in the text
matches = re.findall(pattern4, text4)

if matches:
    print("Matches found:")
    for match in matches:
        print(match)
else:
    print("No matches found.")