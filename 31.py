counter = 0

for p1 in range(201):
    for p2 in range(int((200.0-1*p1)/2+2)):
        for p5 in range(int((200.0-1*p1-2*p2)/5+2)):
            for p10 in range(int((200.0-1*p1-2*p2-5*p5)/10+2)):
                for p20 in range(int((200.0-1*p1-2*p2-5*p5-10*p10)/20+2)):
                    for p50 in range(5):
                        for p100 in range(3):
                            for p200 in range(2):
                                if 1*p1+2*p2+5*p5+10*p10+20*p20+50*p50+100*p100+200*p200 == 200:
                                    counter += 1
                                    #print counter

print counter
