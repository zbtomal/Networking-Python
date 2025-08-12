def crc_remainder(data, generator):
    # Append zeros (degree = len(generator) - 1)
    data = data + '0' * (len(generator) - 1)
    data = list(data)
    gen = list(generator)

    for i in range(len(data) - len(gen) + 1):
        if data[i] == '1':  # Divide only if leading bit is 1
            for j in range(len(gen)):
                data[i + j] = '0' if data[i + j] == gen[j] else '1'
    # Remainder is last len(generator)-1 bits
    return ''.join(data[-(len(generator)-1):])

def encode(data, generator):
    remainder = crc_remainder(data, generator)
    return data + remainder, remainder

def decode(codeword, generator):
    return crc_remainder(codeword[:-len(generator)+1], generator) == '0' * (len(generator)-1)

# ---------------- DEMO ----------------
data = "11010011101100"
generator = "1011"

print("Data:       ", data)
print("Generator:  ", generator)

# Encoding
codeword, rem = encode(data, generator)
print("Remainder:  ", rem)
print("Codeword:   ", codeword)

# Decoding without error
print("\nNo error test:")
print("Valid?" , decode(codeword, generator))

# Simulate error
error_codeword = list(codeword)
error_codeword[5] = '1' if codeword[5] == '0' else '0'
error_codeword = ''.join(error_codeword)
print("\nWith error:")
print("Received:  ", error_codeword)
print("Valid?" , decode(error_codeword, generator))
