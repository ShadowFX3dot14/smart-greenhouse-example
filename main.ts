input.onButtonPressed(Button.A, function () {
    basic.showString(kitronik_smart_greenhouse.readTime())
    basic.pause(500)
    basic.showString("T:")
    basic.showNumber(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C))
    basic.showString("C")
    basic.pause(500)
    basic.showString("H:")
    basic.showNumber(kitronik_smart_greenhouse.humidity())
    basic.showString("%")
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    if (!(lampOn)) {
        lampOn = true
        zipStick.showColor(kitronik_smart_greenhouse.colors(ZipLedColors.Yellow))
    } else {
        lampOn = false
        zipStick.clear()
        zipStick.show()
    }
})
input.onButtonPressed(Button.B, function () {
    kitronik_smart_greenhouse.controlHighPowerPin(kitronik_smart_greenhouse.HighPowerPins.pin13, kitronik_smart_greenhouse.onOff(true))
    basic.pause(200)
    kitronik_smart_greenhouse.controlHighPowerPin(kitronik_smart_greenhouse.HighPowerPins.pin13, kitronik_smart_greenhouse.onOff(false))
})
let soilHue = 0
let humidHue = 0
let tempHue = 0
let lampOn = false
let zipStick: kitronik_smart_greenhouse.greenhouseZIPLEDs = null
kitronik_smart_greenhouse.setDate(20, 1, 20)
kitronik_smart_greenhouse.setTime(15, 0, 0)
let zipLEDs = kitronik_smart_greenhouse.createGreenhouseZIPDisplay(8)
let statusLEDs = zipLEDs.statusLedsRange()
zipStick = zipLEDs.zipStickRange()
zipLEDs.setBrightness(255)
lampOn = false
basic.forever(function () {
    tempHue = Math.map(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C), 0, 40, 210, 0)
    humidHue = Math.map(kitronik_smart_greenhouse.humidity(), 0, 100, 35, 150)
    soilHue = Math.map(kitronik_smart_greenhouse.readIOPin(kitronik_smart_greenhouse.PinType.analog, kitronik_smart_greenhouse.IOPins.p1), 0, 1023, 35, 150)
    statusLEDs.setZipLedColor(0, kitronik_smart_greenhouse.hueToRGB(tempHue))
    statusLEDs.setZipLedColor(1, kitronik_smart_greenhouse.hueToRGB(humidHue))
    statusLEDs.setZipLedColor(2, kitronik_smart_greenhouse.hueToRGB(soilHue))
    statusLEDs.show()
})
