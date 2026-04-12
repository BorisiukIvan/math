# This program calculates sequences of random integers in the range [10^38; 10^39] and makes statistics based on sequences' endings.
# All cycles whose members are lower than 21 are considered primitive and consered simultaneosly.
# The program runs only in Python 2.

import random, time
def general(x):
    if (x < 2): return x
    if (x < 3): return 2
    if (x < 5): return 3
    if (x < 7): return 5
    if (x < 11): return 7
    if (x < 13): return 11
    if (x < 17): return 13
    if (x < 19): return 17
    if (x < 23): return 19
    if (x < 29): return 23
    if (x < 31): return 29
    if (x < 37): return 31
    if (x < 41): return 37
    if (x < 43): return 41
    if (x < 47): return 43
    if (x < 53): return 47
    if (x < 59): return 53
    if (x == 59): return 59

def mn2and5(x):
    k = 0
    if x == 10000: k=1
    if x == 12800: k=1
    if x == 16000: k=1
    if x == 20000: k=1
    if x == 25000: k=1
    if x == 25600: k=1
    if x == 32000: k=1
    if x == 40000: k=1
    if x == 50000: k=1
    if x == 51200: k=1
    if x == 64000: k=1
    if x == 80000: k=1
    if x == 100000: k=1
    if x == 125000: k=1
    if x == 128000: k=1
    if x == 160000: k=1
    if x == 200000: k=1
    if x == 250000: k=1
    if x == 256000: k=1
    if x == 320000: k=1
    if x == 400000: k=1
    if x == 500000: k=1
    if x == 512000: k=1
    if x == 625000: k=1
    if x == 640000: k=1
    if x == 800000: k=1
    if x == 1000000: k=1
    if x == 1250000: k=1
    if x == 1600000: k=1
    if x == 2000000: k=1
    if x == 2500000: k=1
    if x == 3125000: k=1
    if x == 3200000: k=1
    if x == 4000000: k=1
    if x == 5000000: k=1
    if x == 6250000: k=1
    if x == 8000000: k=1
    return k

f0 = 0
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
f8 = 0
f9 = 0
f10 = 0
f11 = 0
f12 = 0
f13 = 0
cep = 0
naska = 0
naska2 = 0
naska3 = 0
naska4 = 0
naska5 = 0
t1 = time.time()
maxcep = 0
maxtime = 0
if maxcep == 0: maxcep = 10**100
if maxtime == 0: maxtime = 10**100
while 1:
    cep = cep+1
    if cep > maxcep: break
    a0 = random.randint(10**38, 10**39)
#    print a0,':',
    a = a0
    d = 0
    bs = 0
    t = 0
    while (a > 21):
        s=1
        d=d+1
        g=1
        a2=str(a)
	mod = 0
	for i in range(0, len(a2)):
	    a1 = mod*10 + int(a2[i])
            if (a1 > 1):
		n = general(a1)
                s=s*n
		mod = a1 - n
	    else: mod = a1
	a = s
#	print a,
	if (d > 500): break
	if (a == 65) or (a == 121) or (a == 6699) or (a == 65975) or (a == 213992164519) or (a == 14449856421) or (a == 304698185748945450) or (a == 701664509) or (a == 38637674850439354079908833978512850):  
#		print 'naska',a,'(',cep,')'
		break
#    print a,
    if a > 21:
	if a == 65: f1 = f1+1
	else:
		if (a == 6699): f2 = f2+1
		else:
			if a == 65975: f4 = f4+1 
			else: 
				if a == 121: f3 = f3+1
				else:
					if (a == 213992164519): f5 = f5+1 
					else:
						if (a == 14449856421): f6 = f6+1
						else:
							if (a == 304698185748945450): f7 = f7+1
							else:
								if (a == 2462063578985010): f8 = f8+1
								else:
									if (a == 45037249997922): f9 = f9+1
									else:
										if a == 701664509: f10 = f10+1
										else:
											if a == 423018500869965: f11 = f11+1
											else:
												if a == 38637674850439354079908833978512850: f12 = f12+1
												else:
													f13 = f13+1
													if naska == 0: naska = a
													else:
														if naska2 == 0: naska2 = a
														else:
															if naska3 == 0: naska3 = a
															else:
																if naska4 == 0: naska4 = a
																else:
																	naska5 = a
																	print 'Found 5 cycles. Terminating.'
																	print naska,naska2,naska3,naska4,naska5
																	break
													print 'Found a new cycle!',a,'(',cep,')'
	if (a == 2462063578985010) or (a == 450373249997922) or (a == 701664509) or (a == 423018500869965) or (a == 38637674850439354079908833978512850): print 'Rare cycle!'
    if a <= 62: 
	f0 = f0+1
#	print '<21'
    a0 = a0+1
    if cep%10000==0: 
	t2 = time.time()
	t = t2 - t1
	if mn2and5(cep) == 1:
		test_file = open('ExSeq1_Stat'+str(cep)+'.txt', 'w')
	else: 
		test_file = open('ExSeq1_Stat.txt', 'w')
	print >> test_file, '----------------TOTAL SEQ =',cep,'-----------------------------------'
	print >> test_file, '5 FOUND CYCLES = ',naska,naska2,naska3,naska4,naska5
	print >> test_file, f0/(cep+0.)*100, '% - <21(',f0,')'
	print >> test_file, f1/(cep+0.)*100, '% - 65(',f1,')'
	print >> test_file, f2/(cep+0.)*100, '% - 69745 25935 8050 56203 59675 148925 41990 6699(',f2,')'
	print >> test_file, f3/(cep+0.)*100, '% - 121(',f3,')'
	print >> test_file, f4/(cep+0.)*100, '% - 65975(',f4,')'
	print >> test_file, f5/(cep+0.)*100, '% - 213992164519 37848442996 184743205647 1619079150 52958867143 650419989310 100131326295 910059150(',f5,')'
	print >> test_file, f6/(cep+0.)*100, '% - 14449856421 923568174529 170365396412211 519054916380 11795034225(',f6,')'
	print >> test_file, f7/(cep+0.)*100, '% - 304698185748945450 202368401042200238547 1078847620548237540 6246002820510377925 58982475028933120665 531237564542534850 60452029927414125(',f7,')'
	print >> test_file, f8/(cep+0.)*100, '% - 2462063578985010(',f8,')'
	print >> test_file, f9/(cep+0.)*100, '% - 450373249997922(',f9,')'
	print >> test_file, f10/(cep+0.)*100, '% - 701664509(',f10,')'
	print >> test_file, f11/(cep+0.)*100, '% - 423018500869965(',f11,')'
	print >> test_file, f12/(cep+0.)*100, '% - 38637674850439354079908833978512850 and 4 new(',f12,')'
	print >> test_file, f13/(cep+0.)*100, '% - Other cycles(',f13,').'
	test_file.flush()
	if t > maxtime: break
print 'END!!'