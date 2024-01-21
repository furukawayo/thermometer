from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

WIDTH = 128
HEIGHT = 64

# I2C設定 (I2C識別ID 0or1, SDA, SCL)
i2c = I2C(0, sda=Pin(16), scl=Pin(17) )

# 使用するSSD1306のアドレス取得表示（通常は0x3C）
addr = i2c.scan()
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)


while True:

    # センサから取得した値(0~65535) を電圧に変換します。
    reading = sensor_temp.read_u16() * conversion_factor
   
    # 温度を計算します。センサは27度を基準にしているため、
    # 温度センサの数値を27度から引いて計算します。
    temperature = 27 - (reading - 0.706)/0.001721

    print(temperature)
    oled.fill( 0 )
    oled.text(str(temperature), 5, 5)
    oled.text("temperature", 5, 15)
    oled.show()
    utime.sleep(1)
#gro 3v3 22 21