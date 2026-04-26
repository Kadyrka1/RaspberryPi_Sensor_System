import sys
import select
from time import sleep
import machine

ADC2 = machine.ADC(28)

# Wait for commands...
while True:
    
    # Check if data is available an serial interface
    if select.select([sys.stdin], [], [], 0)[0]:
        
        # Read command
        command = sys.stdin.readline().strip()

        # Analyze and interpret command...
        if command == "*IDN?":
            print("I'm Pico")
            
        elif command=="MEAS:RAW?":
            meas_count = ADC2.read_u16()*3.3
            print(meas_count)
            
        elif command=="MEAS:VOLT?":
            meas_voltage = ADC2.read_u16()/65535*3.3
            print(meas_voltage)
        
    sleep(0.1)

