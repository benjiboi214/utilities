from sys import argv
from random import choice, randint

def generate_password():
    random_words = ('Adult', 'Mushroom', 'Air', 'Aircraft',
    'Airforce', 'Airport', 'Album', 'Alphabet', 'Apple', 'Arm',
    'Army', 'Baby', 'Backpack', 'Balloon', 'Banana', 'Bank',
    'Barbecue', 'Bathroom', 'Bathtub', 'Bed', 'Bee', 'Chick',
    'Bird', 'Archway', 'Book', 'Boss', 'Bottle', 'Bowl', 'Box',
    'Boy', 'Brain', 'Bridge', 'Butterfly', 'Button', 'Cappuccino',
    'Car', 'Decking', 'Carpet', 'Carrot', 'Cave', 'Chair', 'Chess',
    'Chief', 'Child', 'Chisel', 'Chocolates', 'Hoop', 'Circle',
    'Circus', 'Clock', 'Clown', 'Coffee', 'Comet', 'Compact',
    'Compass', 'Computer', 'Crystal', 'Cup', 'Cycle', 'Data',
    'Desk', 'Diamond', 'Dress', 'Drill', 'Drink', 'Drum', 'Faction',
    'Ears', 'Earth', 'Egg', 'Electricity', 'Elephant', 'Eraser',
    'Cookbook', 'Eyes', 'Family', 'Fan', 'Feather', 'Festival',
    'Film', 'Finger', 'Fire', 'Floodlight', 'Flower', 'Foot', 'Fork',
    'Brew', 'Fruit', 'Drawer', 'Game', 'Garden', 'Gas', 'Gate',
    'Gemstone', 'Girl', 'Gloves', 'Daze', 'Grapes', 'Guitar',
    'Hammer', 'Hat', 'Activity', 'Highway', 'Feast', 'Horse',
    'Hose', 'Ice', 'Icecream', 'Insect', 'Jet', 'Junk',
    'Kitchen', 'Knife', 'Leather', 'Leg', 'Library', 'Liquid',
    'Magnet', 'Man', 'Map', 'Maze', 'Meat', 'Meteor', 'Microscope',
    'Milk', 'Milkshake', 'Mist', 'Money', 'Monster', 'Mosquito', 'Mouth',
    'Nail', 'Navy', 'Necklace', 'Needle', 'Onion', 'Paintbrush', 'Pants',
    'Parachute', 'Passport', 'Pebble', 'Pendulum', 'Pepper', 'Perfume',
    'Pillow', 'Plane', 'Planet', 'Pocket', 'Post', 'Potato', 'Printer',
    'Doorman', 'Pyramid', 'Radar', 'Rainbow', 'Record', 'Restaurant',
    'Rifle', 'Ring', 'Robot', 'Rock', 'Rocket', 'Roof', 'Room', 'Rope',
    'Saddle', 'Salt', 'Sandpaper', 'Sandwich', 'Satellite', 'School',
    'Ship', 'Shoes', 'Shop', 'Shower', 'Signature', 'Skeleton', 'Snake',
    'Snail', 'Software', 'Solid', 'Space', 'Spectrum', 'Sphere', 'Spice',
    'Spiral', 'Spoon', 'Spotlight', 'Square', 'Staircase',
    'Star', 'Stomach', 'Sun', 'Sunglasses', 'Supreme', 'Swimming',
    'Sword', 'Table', 'Tapestry', 'Teeth', 'Telescope', 'Television',
    'Tennis', 'Thermometer', 'Tiger', 'Transform', 'Tongue', 'Torch',
    'Torpedo', 'Train', 'Treadmill', 'Triangle', 'Tunnel', 'Typewriter',
    'Umbrella', 'Vacuum', 'Vampire', 'Videotape', 'Vulture', 'Water',
    'Weapon', 'Web', 'Wheelchair', 'Window', 'Woman', 'Worm', 'Xray')
    
    rn = randint(0,100)
    rs = choice('!@#$%^&*=+')
    rw1, rw2 = choice(random_words), choice(random_words)
    
    while rw2 == rw1:
        rw2 = choice(random_words)
    
    new_pw = '%s%s%s%s' % (rw1,rn,rw2,rs)
    return new_pw

def main():
    script, cycle = argv
    
    try:
        cycle = int(cycle)
    except ValueError:
        exit("Please use int for argv")
    
    for n in range(cycle):
        print generate_password()

if __name__ == '__main__':
    main()
    

