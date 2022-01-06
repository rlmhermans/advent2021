with open('input') as f:
    input = f.readline()

def process(packet):
    version = int(packet[:3], 2)
    typeid = int(packet[3:6], 2)

    if typeid == 4:
        literal = packet[6:]
        number = ''
        last = False
        while not last:
            last = literal[0] == '0'
            number += literal[1:5]
            literal = literal[5:]

        return (int(number, 2), literal)

    else:
        results = []
        if packet[6] == '0':
            length = int(packet[7:22], 2)
            packin = packet[22:]

            while length > 0:
                result, packout = process(packin)
                results.append(result)
                length -= len(packin)-len(packout)
                packin = packout

        else:
            amount = int(packet[7:18], 2)
            packin = packet[18:]

            while amount > 0:
                result, packin = process(packin)
                results.append(result)
                amount -= 1

        if typeid == 0:
            opresult = sum(results)
        if typeid == 1:
            opresult = 1
            for x in results:
                opresult *= x
        if typeid == 2:
            opresult = min(results)
        if typeid == 3:
            opresult = max(results)
        if typeid == 5:
            opresult = 1 if results[0] > results[1] else 0
        if typeid == 6:
            opresult = 1 if results[0] < results[1] else 0
        if typeid == 7:
            opresult = 1 if results[0] == results[1] else 0
            
        return (opresult, packin)

packet = str(bin(int(input, 16)))[2:]

while len(packet) < len(input) * 4:
    packet = '0' + packet

print(process(packet)[0])