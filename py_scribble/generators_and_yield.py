# sample generators and yeild

def csv_generator_function():
    for row in open('samples/historicalExchangeRates.csv'):
        yield row

        
generator = csv_generator_function()

for value in generator:
    print (value)
    

# sample : generators remembering state

def rem_state():
    num = 0
    while num < 10:
        yield num
        num += 1

rem_state = rem_state()

for v in rem_state:
    print (v)
    
#sample : send method in generators 

def using_send_method():
    i = 0
    num = 0
    while num < 10:
        i = (yield num)
        print (f'loop..{i}')
        if i is not None:
            num = i
        num = num+1
        
send_test = using_send_method()

for v in send_test:
    print(f'main ...{v}')
    if v == 9:
         send_test.send(14)
        