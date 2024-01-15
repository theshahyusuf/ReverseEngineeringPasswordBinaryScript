def reverse_engineer_password(keyword):
    password = ""
    for i in range(len(keyword)):
        # Get the ASCII values of the current and next character (circularly)
        current_char_ascii = ord(keyword[i])
        next_char_ascii = ord(keyword[(i + 1) % len(keyword)])

        # Calculate the original character's ASCII by reversing the operation
        original_char_ascii = abs(current_char_ascii - next_char_ascii) + ord('`')

        # Convert ASCII to character and add it to the password
        password += chr(original_char_ascii)

    return password

# Keywords array from the decompiled C code
keywords = ["hackadayu", "software", "reverse", "engineering", "ghidra"]

# Dictionary to hold the passwords
passwords = {}

# Generate passwords for each keyword
for keyword in keywords:
    passwords[keyword] = reverse_engineer_password(keyword)

# Print the passwords
for key, value in passwords.items():
    print(f"Keyword: {key}, Password: {value}")

