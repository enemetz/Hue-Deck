function lightOneSwitch() {
    eel.lightSwitchOnePressed()(function() {console.log("Light 1 switched")})
    isOn(1, "lightOne");
}

function lightTwoSwitch() {
    eel.lightSwitchTwoPressed()(function() {console.log("Light 2 switched")})
    isOn(2, "lightTwo")
}

function lightThreeSwitch() {
    eel.lightSwitchThreePressed()(function () {console.log("Light 3 switched")})
    isOn(3, "lightThree");
}

function lightFourSwitch() {
    eel.lightSwitchFourPressed()(function () {console.log("Light 4 switched")})
    isOn(4, "lightFour");
}

function isOn(light, elementID) {
    eel.isLightOn(light)(function (ret) {
        console.log(ret);
        if (ret == true) {
            document.getElementById(elementID).innerHTML = "On"
        } else {
            document.getElementById(elementID).innerHTML = "Off"
        }

    })
}