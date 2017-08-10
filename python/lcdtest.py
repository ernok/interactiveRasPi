import sys
sys.path.append('/home/pi/lcd')
import lcd
lcd.lcd_init()
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string(" Richard's Pi", 1)
lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
lcd.lcd_string("ENTER TEXT HERE!", 1)
lcd.GPIO.cleanup()

