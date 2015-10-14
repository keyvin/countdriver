#!/usr/bin/python3

import datetime
import random
import time
import RPi.GPIO as gpio
import sys
import os


#todo - consider replacing the datetime objects in the code with timedeltas. Seems like it would make more sense.

#function for switching direction for useless things hackathon clock... 
def getDirection(direction=-1):
        #  switch directions (positive if initial)
    if direction == -1:
        direction = 1
    else:
        direction = -1
    return direction


class countdowntimer():
    def __init__(self, count_to, direction=-1, stop_at_target=True)
        self.direction = direction
        self.time_set = direction
        self.disp_pin = [3, 5, 7, 11, 13, 15, 19, 21] 
        self.bcd_pins = [29,31,33,35]
        self.plus_minus_pin = 37
        self.over_under_pin = 23
        self.timer_value = datetime.datetime()
        self.direction = datetime.timedelta(seconds = count_direction)
        self.strobe_delay = .000001
        self.stop_at_target = stop_at_target
        self.initpins()



    #We are counting down. Initialize timer to the time the count starts on.
        if direction == -1:    
            self.timer_value = count_to

    #counting up. Initialize timer to zero. Great candidate for time..
       if count_direction == 1:
           our_time == datetime.datetime(time_set.day, 1, 1,1,0,0,0)


    def initpins(self):
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)

        outpins = self.disp_pin+self.bcd_pins+self.plus_minus_pin+self.over_under_pin
        for i in outpins:
            gpio.setup(i, gpio.OUT)
    
        for i in disp_pins:
            gpio.setup(i, gpio.OUT, initial=gpio.LOW)


   #  convert timestring to bcd array.
   #  input - "01-14-2001 HH:MM:DD:SS:MS
   #  output - ["0101", "1001"....]

    def makebcd(self):
   #  set pin numbers
        #  split time into numbers
        to_bcd = self.timer_value
        just_nums = ''.join(to_bcd.split()[1].split(':'))
        nums = list("00"+just_nums)
        bcd = []
        for i in nums:
            tmp = format(int(i),"#010b")
            bcd.append(tmp[6:])
        return bcd


#This is the function that interacts with the hardware. Output pins are defined here
#Write bcd values to bcd bus, then enable segment. Repeat for each segment
#This needs an addition for the +/- value
    def strobe(self, bcd):
        for segment in range(len(self.disp_pin)):
            for bcds in range(4):
                gpio.output(self.bcd_pins[bcds], (int(bcd[segment][bcds]) ^ 1))
            #print ("segment %d, value %s, pin %d, value %c",
            #       %(segment, bcd[segment],bcd_pins[bcds], bcd[segment][bcds])) 
                time.sleep(self.strobe_delay)
                gpio.output(self.disp_pin[segment], gpio.HIGH)
                time.sleep(self.strobe_delay)
                gpio.output(self.disp_pin[segment], gpio.LOW)
                time.sleep(self.strobe_delay)


#divedisplay - outputs to clock via strobe for one full second before returning. 


#note - accuracy depends on returning to this function within the same second it left. 
#       Otherwise, we skip a second. 

    def drivedisplay(self):               
        then = datetime.datetime.now()
    #Convert our time object to an array of bcd values
        bcd = makebcd(str(self.timer_value))
        while True:
        #strobe 7 segments or write time or w/e
            self.strobe(bcd)
            now = datetime.datetime.now()
        #check if 1 second has elapsed, return if so
            delta = (now - then)
            if delta.seconds == 1:
                break


#A real countdown/Count Up function. General flow - 


    #1. Enter main loop
    #2.    call drivedisplay with our timer value
    #3.    Check if we have reached our current time, set direction to 0 so counting stops
    def countmain(self):


    #infinite loop driving the clock
        while True:
        #debug print.
            print (self.timer_value)
            self.drivedisplay()
            self.timer_value = self.timer_value + self.direction

            if self.direction == -1:
            #drive the display for a single second, then count up
            #we have reached our target. stop counting and keep driving the clock.
                if self.timer_value.hour == 0 and self.timer_value.minute == 0 and self.timer_value.second == 0:
                    #Need to flip +/- if false and start infinite count up
                    if self.stop_at_target == True:
                        self.direction = datetime.timedelta()
                    else:
                        #flip count and +/- sign
                        pass
        #We are counting up
            if self.direction == 1:
            #stop counting. We have reached our time. 
                if self.timer_value == time_set:
                    if self.stop_at_target == True:
                        self.direction = datetime.timedelta()
                    else:
                        #flip count and +/- sign, 
                        pass
                    





if __name__ == '__main__':
    print (sys.argv[0])
    if len(sys.argv) == 1:
        print ("Usage: time.py random - random countdown\n time.py direction DD:HH:MM:SS\n direction is 1 for count up, -1 for countdown")
        sys.exit(0)
    
#    if sys.argv[1] == 'random':
#        ranmain()
    
    if sys.argv[1] == 'count':
        direction = int(sys.argv[2])
        time = sys.argv[3] 
        #time format 
        #DD:HH:MM:SS
        #split time to prep for date time obj
        i_time = time.split(':')
        for i in range(len(i_time)):
            i_time[i] = int(i_time[i])

        time_obj = datetime.datetime(2000, 10, i_time[0], i_time[1], i_time[2], i_time[3])


    timer_obj = countdowntimer(time_obj, direction)
    timer_obj.maincount()

# This function is leftover from the useless things hackathon 
#ef ranmain():
        #  determine time values
#   random.seed(time.time())
#   our_time = datetime.datetime(2000,1,1,int(random.random()*24), int(random.random()*60), int(random.random()*60))
        #  determine time arrow
#   time_dir = getDirection(-1)
        #  determine length of timer
#   ticks = int(random.random()*15)+15
#   count = 0
        #  loop forever
#   while True:
        #  wait one second
        
        #  count second
#       our_time = our_time + datetime.timedelta(0,time_dir)
        #print (str(our_time) + " " + str(count) + " " + str(ticks))
#       os.system('clear')
 #      print ("\n\n\n\t", '{:02d}'.format(our_time.hour), ':', '{:02d}'.format(our_time.minute), ':', '{:02d}'.format(our_time.second), '\n')
        
#       bcd = makebcd(str(our_time))
#@      flag = True  
#       delta = datetime.timedelta()
#       while flag:
#           then = datetime.datetime.now()
#           strobe(bcd)
#           now = datetime.datetime.now()
#           delta = delta + (now - then)
#            print(delta)
#           if delta.seconds == 1:
#               flag = False

        #  iterate counter
#       count = count + 1
        #  direction switch conditional
#       if count == ticks:
        #   switch time arrow
#            time_dir = getDirection(time_dir)
        #   reinitialize length of timer
#            ticks = int(random.random()*45)+15
        #   reinitialize counter
#            count = 0                   
         #  initialize display and output pins

