def xor(a, b):
    """Perform XOR between two binary strings."""
    result = ""
    for i in range(1, len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def crc_remainder(data, generator):
    """Compute CRC remainder for given data and generator polynomial."""
    n = len(generator)
    # Append n-1 zeros to data
    padded_data = data + '0' * (n - 1)
    temp = padded_data[:n]

    for i in range(len(data)):
        if temp[0] == '1':
            temp = xor(generator, temp) + padded_data[n + i]
        else:
            temp = xor('0'*n, temp) + padded_data[n + i]
    # Last XOR
    if temp[0] == '1':
        temp = xor(generator, temp)
    else:
        temp = xor('0'*n, temp)

    return temp

def encode(data, generator):
    """Return codeword = data + remainder."""
    rem = crc_remainder(data, generator)
    return data + rem, rem

def decode(codeword, generator):
    """Check if codeword has error (remainder all zeros)."""
    rem = crc_remainder(codeword[:-len(generator)+1], generator)
    return all(bit == '0' for bit in rem)

# ---------------- DEMO ----------------
if __name__ == "__main__":
    # Input data
    data = "11010011101100"
    generator = "1011"

    print("Original Data:       ", data)
    print("Generator Polynomial:", generator)

    # Encoding
    codeword, remainder = encode(data, generator)
    print("\nCRC Remainder:       ", remainder)
    print("Encoded Codeword:    ", codeword)

    # Decoding without error
    print("\n--- Decoding without error ---")
    if decode(codeword, generator):
        print("No error detected.")
    else:
        print("Error detected!")

    # Simulate error
    error_codeword = list(codeword)
    error_codeword[5] = '1' if codeword[5] == '0' else '0'  # flip 6th bit
    error_codeword = ''.join(error_codeword)
    print("\n--- Decoding with error ---")
    print("Received Codeword:   ", error_codeword)
    if decode(error_codeword, generator):
        print("No error detected! (CRC failed)")
    else:
        print("Error detected by CRC!")
