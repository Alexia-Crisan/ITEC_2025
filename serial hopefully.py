import serial
import matplotlib.pyplot as plt
import numpy as np

SERIAL_PORT = 'COM6'  
BAUD_RATE = 115200

lab = np.zeros((7, 7), dtype=int)  
i, j = 0, 0

try:
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Listening on {SERIAL_PORT} at {BAUD_RATE} baud rate...")

        while True:
            if ser.in_waiting:
                data = ser.read(1)
                char_received = data.decode('utf-8', errors='ignore') 


                print(f"Received character: '{char_received}'")

                if char_received == '\n': 
                    i += 1
                    j = 0
                    if i == 7: 
                        break
                else:
                    lab[i][j] = int(char_received)
                    j += 1 

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
except KeyboardInterrupt:
    print("\nStopped by user.")

print("Received matrix:")
print(lab)

labirint=lab
for i in range(6):
    labirint[i] = lab[i + 1]
labirint[6] = lab[0]

lab=labirint


fig, ax = plt.subplots()
ax.matshow(lab, cmap='gray_r')


for i in range(lab.shape[0]):
    for j in range(lab.shape[1]):
        c = lab[i, j]
        ##ax.text(j, i, str(c), va='center', ha='center')

plt.show()
