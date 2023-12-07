PING = 0
basic.show_icon(IconNames.HAPPY)

def on_forever():
    global PING
    PING = sonar.ping(DigitalPin.P13, DigitalPin.P14, PingUnit.CENTIMETERS)
    serial.write_value("x", PING)
    if PING < 15:
        basic.show_leds("""
            . . # . .
            . # # . .
            # # # # #
            . # # . .
            . . # . .
            """)
        pins.analog_write_pin(AnalogPin.P1, 100)
        pins.analog_write_pin(AnalogPin.P8, 0)
        pins.analog_write_pin(AnalogPin.P12, 0)
        pins.analog_write_pin(AnalogPin.P16, 100)
        basic.pause(10)
    elif 15 < PING and PING < 180:
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
            """)
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P8, 200)
        pins.analog_write_pin(AnalogPin.P12, 0)
        pins.analog_write_pin(AnalogPin.P16, 300)
    else:
        basic.show_icon(IconNames.SAD)
    basic.pause(10)
basic.forever(on_forever)
