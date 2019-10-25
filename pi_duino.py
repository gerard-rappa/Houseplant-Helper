import serial

port = "/dev/ttyACM0"
rate = 9600

s1 = serial.Serial(port,rate)
s1.flushInput()

while True:
    if s1.inWaiting()>0:
        #Soil Moisture Sensor
        inputValue=s1.readline().decode("utf-8")
        inputValue = int(inputValue)
        if inputValue>550:
            print("Very dry", inputValue)
        if inputValue<350:
            print("Very wet", inputValue)
        #Temperature    
        inputValue=s1.readline().decode("utf-8")
        inputValue = float(inputValue)     
        print("Temperature: ",inputValue," F")
        
        #Humidity
        inputValue=s1.readline().decode("utf-8")
        inputValue = float(inputValue)
        print("Humidity: ",inputValue,"%")
        
        
