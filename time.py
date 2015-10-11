import datetime
import random
import time
import RPi.GPIO as gpio

def getDirection(direction=-1):
        #  switch directions (positive if initial)
    if direction == -1:
        direction = 1
    else:
        direction = -1
    return direction

        #  convert timestring to bcd, output to timer
def makebcd(to_bcd):
        #  set pin numbers
         #  split time into numbers
    just_nums = ''.join(to_bcd.split()[1].split(':'))
    nums = list("00"+just_nums)
    bcd = []
    for i in nums:
        tmp = format(int(i),"#010b")
        bcd.append(tmp[6:])
    strobe(bcd)

        #  output time to display            
        #  initialize time, loop execution

def strobe(bcd):
    disp_pin_maps = [3, 5, 7, 11, 13, 15, 19, 21]
    bcd_pins = [29,31,33,35]
    plus_minus = 37
    over_under = 23

    for segment in range(len(disp_pin_maps)):
        for bcds in range(4):
            gpio.output(bcd_pins[bcds], (int(bcd[segment][bcds]) ^ 1))
            #print ("segment %d, value %s, pin %d, value %c" %(segment, bcd[segment],bcd_pins[bcds], bcd[segment][bcds])) 
        time.sleep(.000001)
        gpio.output(disp_pin_maps[segment], gpio.HIGH)
        time.sleep(.000001)
        gpio.output(disp_pin_maps[segment], gpio.LOW)
        time.sleep(.000001)


def main():
        #  determine time values
    random.seed(time.time())
    our_time = datetime.datetime(2000,1,1,int(random.random()*24), int(random.random()*60), int(random.random()*60))
        #  determine time arrow
    time_dir = getDirection(-1)
        #  determine length of timer
    ticks = int(random.random()*15)+15
    count = 0
        #  loop forever
    while True:
        #  wait one second
        
        #  count second
        our_time = our_time + datetime.timedelta(0,time_dir)
        print (str(our_time) + " " + str(count) + " " + str(ticks))
        #  convert string to bcd
        flag = True  
        while flag:
            then = datetime.datetime.now()
            makebcd(str(our_time))
            now = datetime.datetime.now()
            delta = now - then
            if delta.seconds == 1:
                flag = False

        #  iterate counter
        count = count + 1
        #  direction switch conditional
        if count == ticks:
        #   switch time arrow
            time_dir = getDirection(time_dir)
        #   reinitialize length of timer
            ticks = int(random.random()*45)+15
        #   reinitialize counter
            count = 0
            
        
    
        #  initialize display and output pins
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
outpins = [3, 5, 7, 11, 13, 15, 19, 21, 29,31,33,35, 37, 23]
plus_minus = 37
over_under = 23
disp_pins = [3, 5, 7, 11, 13, 15, 19, 21]
for i in outpins:
    gpio.setup(i, gpio.OUT)
    
for i in disp_pins:
    gpio.setup(i, gpio.OUT, initial=gpio.LOW)
    

main()