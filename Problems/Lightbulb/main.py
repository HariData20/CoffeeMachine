class Lightbulb:
    def __init__(self):
        self.state = "off"

    # create method change_state here
    def change_state(self):
        state = self.state
        if state == 'on':
            self.state = 'off'
            print('Turning the light off')
            
        else:
            self.state = 'on'
            print('Turning the light on')