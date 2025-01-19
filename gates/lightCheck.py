lights = [False, True, True, False]

while True:
    lightChoice = int(input('Which light would you like to access (1, 2, 3, 4)? '))
  
    if lightChoice in (1, 2, 3, 4):
        lightChange = input('What would you like to do with the light (check or switch)? ')
    
        if lightChange == 'check':
            if lights[lightChoice - 1]:
                print('Light is on')
            else:
                print('Light is off')

        elif lightChange == 'switch':
            if lights[lightChoice - 1]:
                lights[lightChoice - 1] = False
                print('The light is switched off')

            else:
                lights[lightChoice - 1] = True
                print('The light is switched on')
    
    else:
        print('Invalid input')


# Masks
'''
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
'''