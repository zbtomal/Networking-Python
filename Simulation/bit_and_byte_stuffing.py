def bit_stuffing(data):
    """Performs bit stuffing: insert a '0' after five consecutive '1's."""
    stuffed = ""
    count = 0
    for bit in data:
        stuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                stuffed += '0'
                count = 0
        else:
            count = 0
    return stuffed

def bit_unstuffing(data):
    """Removes stuffed bits."""
    unstuffed = ""
    count = 0
    i = 0
    while i < len(data):
        bit = data[i]
        unstuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                i += 1  # skip the stuffed '0'
                count = 0
        else:
            count = 0
        i += 1
    return unstuffed

def byte_stuffing(data, flag="F", esc="E"):
    """Performs byte stuffing using flag and escape characters."""
    stuffed = flag  # Start with flag
    for byte in data:
        if byte in (flag, esc):
            stuffed += esc
        stuffed += byte
    stuffed += flag  # End with flag
    return stuffed

def byte_unstuffing(data, flag="F", esc="E"):
    """Removes stuffed escape characters."""
    # Remove start and end flags
    data = data[1:-1]
    unstuffed = ""
    skip = False
    for i, byte in enumerate(data):
        if skip:
            skip = False
            continue
        if byte == esc:
            skip = False
            continue
        unstuffed += byte
    return unstuffed


# --------------------- DEMO ---------------------
if __name__ == "__main__":
    # Example binary data
    binary_data = "01111110111110111110"
    print("Original Binary Data: ", binary_data)

    # --- Bit Stuffing ---
    stuffed_bits = bit_stuffing(binary_data)
    print("Bit Stuffed Data:     ", stuffed_bits)
    unstuffed_bits = bit_unstuffing(stuffed_bits)
    print("Bit Unstuffed Data:   ", unstuffed_bits)

    print("\n--- BYTE STUFFING ---")
    # Example byte stream (characters)
    byte_stream = "ABFECDEFG"
    print("Original Byte Data:   ", byte_stream)

    stuffed_bytes = byte_stuffing(byte_stream, flag="F", esc="E")
    print("Byte Stuffed Data:    ", stuffed_bytes)

    unstuffed_bytes = byte_unstuffing(stuffed_bytes, flag="F", esc="E")
    print("Byte Unstuffed Data:  ", unstuffed_bytes)
