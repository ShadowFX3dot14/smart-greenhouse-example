def on_button_pressed_a():
    basic.show_string(kitronik_smart_greenhouse.read_time())
    basic.pause(500)
    basic.show_string("T:")
    basic.show_number(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C))
    basic.show_string("C")
    basic.pause(500)
    basic.show_string("H:")
    basic.show_number(kitronik_smart_greenhouse.humidity())
    basic.show_string("%")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global lampOn
    if not (lampOn):
        lampOn = True
        zipStick.show_color(kitronik_smart_greenhouse.colors(ZipLedColors.YELLOW))
    else:
        lampOn = False
        zipStick.clear()
        zipStick.show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
        kitronik_smart_greenhouse.on_off(True))
    basic.pause(200)
    kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
        kitronik_smart_greenhouse.on_off(False))
input.on_button_pressed(Button.B, on_button_pressed_b)

soilHue = 0
humidHue = 0
tempHue = 0
lampOn = False
zipStick: kitronik_smart_greenhouse.greenhouseZIPLEDs = None
kitronik_smart_greenhouse.set_date(20, 1, 20)
kitronik_smart_greenhouse.set_time(15, 0, 0)
zipLEDs = kitronik_smart_greenhouse.create_greenhouse_zip_display(8)
statusLEDs = zipLEDs.status_leds_range()
zipStick = zipLEDs.zip_stick_range()
zipLEDs.set_brightness(255)
lampOn = False

def on_forever():
    global tempHue, humidHue, soilHue
    tempHue = Math.map(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C),
        0,
        40,
        210,
        0)
    humidHue = Math.map(kitronik_smart_greenhouse.humidity(), 0, 100, 35, 150)
    soilHue = Math.map(kitronik_smart_greenhouse.read_io_pin(kitronik_smart_greenhouse.PinType.ANALOG,
            kitronik_smart_greenhouse.IOPins.P1),
        0,
        1023,
        35,
        150)
    statusLEDs.set_zip_led_color(0, kitronik_smart_greenhouse.hue_to_rgb(tempHue))
    statusLEDs.set_zip_led_color(1, kitronik_smart_greenhouse.hue_to_rgb(humidHue))
    statusLEDs.set_zip_led_color(2, kitronik_smart_greenhouse.hue_to_rgb(soilHue))
    statusLEDs.show()
basic.forever(on_forever)
