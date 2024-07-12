mask1 = 0b1000
mask2 = 0b0100
mask3 = 0b0010
mask4 = 0b0001

# Lights
lights = 0b0011

def light1_on(lights):
    lights = lights ^ mask1
    return lights

def light2_on(lights):
    lights = lights ^ mask2
    return lights

def light3_on(lights):
    lights = lights ^ mask3
    return lights

def light4_on(lights):
    lights = lights ^ mask4
    return lights

def light_on(lights, light):
    if light == 1:
        lights = lights ^ mask1
    elif light == 2:
        lights = lights ^ mask2
    elif light == 3:
        lights = lights ^ mask3
    elif light == 4:
        lights = lights ^ mask4
    return lights

def show_lights(lights):
    light1 = lights & mask1
    light2 = lights & mask2
    light3 = lights & mask3
    light4 = lights & mask4

    return light1, light2, light3, light4

while True:
    print('1. Light 1')
    print('2. Light 2')
    print('3. Light 3')
    print('4. Light 4')
    print('5. Show lights')
    print('6. Exit')
    lightChoice = int(input('Enter light choice: '))
    if lightChoice == 6:
        break
    elif lightChoice == 5:
        print(show_lights(lights))
    else:
        lightChange = input('Switch on or off: ')
        if lightChange == 'on':
            lights = light_on(lights, lightChoice)
            print('The light is switched on')
        elif lightChange == 'off':
            lights = light_on(lights, lightChoice)
            print('The light is switched off')
        else:
            print('Invalid input')