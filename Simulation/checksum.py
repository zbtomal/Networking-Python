def ones_complement_sum(data_words):
    """Perform 1's complement addition on a list of binary strings."""
    word_len = len(data_words[0])
    total = 0
    for word in data_words:
        total += int(word, 2)
        # Wrap around carry bits
        while total >> word_len:
            total = (total & ((1 << word_len) - 1)) + (total >> word_len)
    # 1's complement
    checksum = (~total) & ((1 << word_len) - 1)
    return format(checksum, f'0{word_len}b')

def encode(data_words):
    """Return data + checksum."""
    checksum = ones_complement_sum(data_words)
    return data_words + [checksum], checksum

def decode(received_words):
    """Return True if no error, False if error detected."""
    return ones_complement_sum(received_words) == '0' * len(received_words[0])

# ---------------- DEMO ----------------
data = ["10101001", "11001100", "11110000"]  # Example 8-bit words
print("Data words: ", data)

# Encoding
codeword, checksum = encode(data)
print("Checksum:   ", checksum)
print("Codeword:   ", codeword)

# Decoding without error
print("\nNo error test:")
print("Valid?" , decode(codeword))

# Simulate error (flip a bit in first word)
error_codeword = codeword.copy()
error_word = list(error_codeword[0])
error_word[3] = '1' if error_word[3] == '0' else '0'  # flip one bit
error_codeword[0] = ''.join(error_word)
print("\nWith error:")
print("Received:   ", error_codeword)
print("Valid?" , decode(error_codeword))
