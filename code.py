import time
import board
import busio
import adafruit_bme280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:
    
    #Plot weather values on Mu Plotter
    print((bme280.temperature,bme280.humidity,bme280.pressure))
    
    #Print on Serial console
    print("\nTemperature(C): "+str(bme280.temperature))
    print("Humidity(%): "+str(bme280.humidity))
    print("Pressure(hPa): "+str(bme280.pressure))
    time.sleep(1)
