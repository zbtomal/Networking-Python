import random
import time

# Probability of packet loss (0 to 1)
PACKET_LOSS_PROB = 0.2

# Simulate sending a packet
def send_packet(packet):
    print(f"Sender: Sending packet {packet}")
    # Simulate transmission delay
    time.sleep(0.5)
    # Randomly decide if packet is lost
    if random.random() < PACKET_LOSS_PROB:
        print(f"!!! Packet {packet} lost during transmission !!!")
        return False
    else:
        print(f"Receiver: Packet {packet} received")
        return True

# Simulate sending an ACK
def send_ack(packet):
    print(f"Receiver: Sending ACK for packet {packet}")
    time.sleep(0.3)
    if random.random() < PACKET_LOSS_PROB:
        print(f"!!! ACK for packet {packet} lost !!!")
        return False
    else:
        print(f"Sender: ACK for packet {packet} received")
        return True

# Stop-and-Wait Protocol
def stop_and_wait(data_packets):
    packet_number = 0
    while packet_number < len(data_packets):
        success = send_packet(data_packets[packet_number])
        
        if success:
            ack_received = send_ack(data_packets[packet_number])
            if ack_received:
                packet_number += 1
            else:
                print("Sender: Timeout, retransmitting packet...")
        else:
            print("Sender: Timeout, retransmitting packet...")

# Example usage
if __name__ == "__main__":
    packets = ["Hello", "This", "is", "Stop-and-Wait", "Protocol"]
    stop_and_wait(packets)
