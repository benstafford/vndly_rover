from PyInquirer import prompt
from rover import Rover

questions = [   
    {
        'type': 'input',
        'name': 'map_size',
        'message': 'Map size \'X Y\'',
    },
    {
        'type': 'input',
        'name': 'rover_placement',
        'message': 'Rover placement',
    },
    {
        'type': 'input',
        'name': 'rover_instructions',
        'message': 'Rover instructions',
    },
]

answers = prompt(questions)

# adding second param puts bounds on movement
# rover = Rover(answers['rover_placement'], answers['map_size'])
rover = Rover(answers['rover_placement'])
rover.send_instructions(answers['rover_instructions'])

print(rover.get_readable_location())