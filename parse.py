import re
import sys
pattern = re.compile("")

count = 0
instr_num = 0
instr_name = ""
start_cycle = 0
end_cycle = 0
total_cycle = 0


with open("test.txt") as fp,open("parse.txt","w") as of: 
    while True: 
        count += 1
        line = fp.readline() 

        if not line: 
            break
        if re.search("^\+",line):
            m = re.search("^\+(\d*) ",line)
            # reset
            instr_num = 0
            instr_name = ""
            start_cycle = sys.maxint
            end_cycle = 0
            total_cycle = 0

            instr_num = int(m.group(1))

            print '%s instruction start' %(instr_num)
        if re.search("^\d* .* \d",line):
            # group(1):num group(2):name group(3):time
            m = re.search("(^\d*) (.*) (\d*)",line)
            if int(m.group(3)) < start_cycle:
                start_cycle = int(m.group(3))
            elif int(m.group(3)) > end_cycle:
                end_cycle = int(m.group(3))
            print'num: %s, name: %s, time: %s' % (m.group(1),m.group(2),m.group(3))
        
        if re.search("^\-",line):
            total_cycle = end_cycle - start_cycle
            print '%s instruction end' %(instr_num)
            print 'start cycle:%d end cycle:%d total cycle:%d' %(start_cycle,end_cycle,total_cycle)
            of.write('start cycle:%d end cycle:%d total cycle:%d\n' %(start_cycle,end_cycle,total_cycle))
            print'--------------------------'

