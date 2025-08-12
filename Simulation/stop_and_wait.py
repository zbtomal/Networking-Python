import random
import time

def stop_and_wait(frames):
    sender_seq = 0  # Sequence number at sender
    receiver_seq = 0  # Expected sequence number at receiver
    
    i = 0  # Frame index
    while i < len(frames):
        frame = frames[i]
        
        print(f"\n[Sender] Sending Frame {sender_seq}: {frame}")
        
        # Simulate sending time
        time.sleep(0.5)
        
        # Simulate ACK loss or delay (20% chance)
        ack_lost = random.random() < 0.2
        
        if not ack_lost:
            # Receiver gets frame
            if sender_seq == receiver_seq:
                print(f"[Receiver] Frame {receiver_seq} received: {frame}")
                receiver_seq = 1 - receiver_seq  # Toggle expected seq
                ack = sender_seq  # ACK with same seq
                print(f"[Receiver] Sending ACK {ack}")
            else:
                print(f"[Receiver] Duplicate Frame {frame} ignored. Resending ACK {1 - receiver_seq}")
                ack = 1 - receiver_seq
            
            # Sender gets ACK
            print(f"[Sender] ACK {ack} received.")
            sender_seq = 1 - sender_seq
            i += 1  # Move to next frame
        
        else:
            # Simulate ACK loss
            print(f"[Receiver] Frame received but ACK lost!")
            print(f"[Sender] Timeout! Resending Frame {sender_seq}")
            # Sender does not increment i, so frame is resent

# ---------------- DEMO ----------------
if __name__ == "__main__":
    data_frames = ["Hello", "World", "This", "Is", "Stop-and-Wait"]
    print("=== Stop-and-Wait ARQ Simulation ===")
    stop_and_wait(data_frames)
    print("\nAll frames transmitted successfully!")
