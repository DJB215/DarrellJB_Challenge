import re

def validate_credit_card(card_number):
    # Regex pattern to match valid credit card numbers
    pattern = r"^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$"
    
    # Check if the card number matches the pattern
    if re.match(pattern, card_number):
        return "Valid"
    else:
        return "Invalid"

# Read input
n = int(input())
card_numbers = [input().strip() for _ in range(n)]

# Validate each credit card number
results = [validate_credit_card(card) for card in card_numbers]

# Print results
for result in results:
    print(result)
