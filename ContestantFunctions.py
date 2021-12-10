import tkinter
import random

class Contestant:
    
    def __init__(self):
        self.name = None 
        self.key_attributes = []

    def set_name(self):
        name_bank = ['Emily', 'Sophie', 'Owen', 'Shawn', 'Brandon', 'Lia', 'Kayden', 'Tom', 'Eliana', 'Carrie', 'John', 'Maggie', 'Camila', 'Skye', 'Lindsey', 'Peyton', 'Amanda', 'Justin', 'Sandra', 'Parker', 'Cameron', 'Lexi', 'Rylee', 'Dalton', 'Blaine', 'Coby', 'Jameson', 'Veronica', 'Dylan', 'Caleb', 'Jane', 'Alison', 'Natalie', 'Jackson', 'Sabrina', 'Jessie', 'Joe', 'Abbey', 'Alan', 'Emma', 'Taylor', 'Meredith', 'Olivia', 'Ben', 'Calvin', 'Connor', 'Jake', 'Harry', 'Rory', 'Noah', 'Mason', 'Selena', 'Brianna', 'Ava', 'Isabella', 'Mia', 'Gianna', 'Asher', 'James', 'Logan', 'Grayson', 'Holden', 'Henry', 'Avery', 'Scarlett', 'Madison', 'Carter', 'Chloe', 'Alex', 'Eric', 'Matt', 'Melanie', 'Jessica', 'Sam', 'William', 'Luke', 'Abigail', 'Hazel', 'Elizabeth', 'Zoe', 'Willow', 'Michael', 'Jayden', 'David', 'Nathan', 'Addison', 'Anthony', 'Grace', 'Eli', 'Hannah', 'Kinsley', 'Skylar', 'Victoria', 'Aubrey', 'Theo', 'Ryan', 'Adrian', 'Thomas', 'Autumn', 'Leah', 'Miles', 'Andrew', 'Josh', 'Brooklen', 'Bailey', 'Ryder', 'Austin', 'Gabriella', 'Carson', 'Anna', 'Jade']
        self.name = random.choice(name_bank)

    def get_name(self):
        return self.name

    def set_key_attributes(self):
        key_attributes_bank = ['blonde hair', 'brown hair', 'short hair', 'long hair', 'blue eyes', 'brown eyes', 'green eyes', 'tall', 'short', 'muscular', 'adventurous', 'athletic', 'compassionate', 'confident', 'courageous', 'creative', 'friendly', 'hardworking', 'honest', 'humorous', 'imaginative', 'independent', 'intelligent', 'loyal','passionate', 'reliable', 'respectful', 'selfless', 'strong', 'sympathetic']
        check = []
        while len(self.key_attributes) < 3:
            key_attribute_item = random.choice(key_attributes_bank)
            if key_attribute_item not in check:
                self.key_attributes.append(key_attribute_item)
                check.append(key_attribute_item)
            else:
                key_attribute_item = random.choice(key_attributes_bank)
                
    def get_key_attributes(self):
        return self.key_attributes
        
def create_number_list():
    number_list_a = random.sample(range(1, 9), 8)
    number_list_b = random.sample(range(1, 9), 8)
    match_numbers = number_list_a + number_list_b
    return match_numbers

def create_contestants():
    contestants = []
    names = []
    match_numbers = create_number_list()
    for i in range(16):
        contestant = Contestant()
        contestant.set_name()
        if contestant.get_name() not in names:
            names.append(contestant.get_name())
        else:
            while contestant.get_name() in names:
                contestant.set_name()
        contestant.set_key_attributes()
        c = [contestant.get_name(), contestant.get_key_attributes()]
        c.append(match_numbers[i])
        contestants.append(c)
    return contestants

def similarities(contestants):
    for x in range(16):
        qualities_1 = []
        qualities_2 = []
        for y in range(len(contestants) - 1):
            c1 = contestants[x]
            c2 = contestants[y + 1]
            if c1[2] == c2[2] and c1 != c2:
                similarities_1 = random.randint(1, 3)
                for i in range(similarities_1):
                    keys_1 = c1[1]
                    quality = random.choice(keys_1)
                    if quality not in qualities_2:
                        qualities_2.append(quality)
                    else:
                        while quality in qualities_2:
                            quality = random.choice(keys_1)
                similarities_2 = random.randint(1, 3)
                for z in range(similarities_2):
                    keys_2 = c2[1]
                    quality = random.choice(keys_2)
                    if quality not in qualities_1:
                        qualities_1.append(quality)
                    else:
                        while quality in qualities_1:
                            quality = random.choice(keys_2)
        c1.append(qualities_1)
    return contestants

def create_traits(contestants):
    eye_bank = ['blue eyes', 'brown eyes', 'green eyes']
    hair_bank = ['blonde hair', 'brown hair', 'short hair', 'long hair']
    physical_bank = ['tall', 'short', 'muscular']
    trait_bank = ['adventurous', 'athletic', 'compassionate', 'confident', 'courageous',
        'creative', 'friendly', 'hardworking', 'honest', 'humorous', 'imaginative', 'independent', 'intelligent', 'loyal', 'passionate', 'reliable', 'respectful', 'selfless', 'strong', 'sympathetic']
    for i in range(len(contestants)):
        c = contestants[i]
        traits = c[3]
        if 'blue eyes' not in traits and 'brown eyes' not in traits and 'green eyes' not in traits:
            eye_trait = random.choice(eye_bank)
            traits.append(eye_trait)
        if 'blonde hair' not in traits and 'brown hair' not in traits and 'short hair' not in traits and 'long hair' not in traits:
            hair_trait = random.choice(hair_bank)
            traits.append(hair_trait)
        if 'tall' not in traits and 'short' not in traits and 'muscular' not in traits:
            physical_trait = random.choice(physical_bank)
            traits.append(physical_trait)
        while len(traits) < 6:
            trait = random.choice(trait_bank)
            if trait not in traits:
                traits.append(trait)
            else:
                trait = random.choice(trait_bank)
    return contestants

def create_matches(contestants):
    matches = []
    check = []
    for x in range(8):
        for i in range(len(contestants) - 1):
            c1 = contestants[x]
            c2 = contestants[i + 1]
            if c1[2] == c2[2] and c1 != c2:
                if c1 not in check and c2 not in check:
                    match = [c1, c2]
                    matches.append(match)
                    check.append(c1)
                    check.append(c2)
    return matches

def alternate_match_list(matches):
    alternate_matches = []
    for i in range(len(matches)):
        match = matches[i]
        c1 = match[0]
        c2 = match[1]
        new_match = [c2, c1]
        alternate_matches.append(new_match)
    return alternate_matches

def user_guess(contestants):
    user_matches = []
    for i in range(8):
        user_match = []
        match_1 = input("Enter Name of Contestant: ")
        match_2 = input("Enter Name of Other Contestant: ")
        for x in range(len(contestants)):
            c = contestants[x]
            if c[0] == match_1:
                user_match.append(c)
            if c[0] == match_2:
                user_match.append(c)
        user_matches.append(user_match)
    return user_matches

def user_guesses(contestants, user_matches):
    user_matches2 = []
    for i in range(8):
        user_match = []
        umatch = user_matches[i]
        match_1 = umatch[0]
        match_2 = umatch[1]
        for x in range(len(contestants)):
            c = contestants[x]
            if c[0] == match_1:
                user_match.append(c)
            if c[0] == match_2:
                user_match.append(c)
        user_matches2.append(user_match)
    return user_matches2

def num_correct(user_matches, matches, alternate_matches):
    num_correct = 0
    for i in range(len(user_matches)):
        match = user_matches[i]
        if match in matches or match in alternate_matches:
            num_correct += 1
    return num_correct

def truth_booth_couple(user_matches):
    booth_couple = random.randint(0, 7)
    truth_booth_match = user_matches[booth_couple]
    return truth_booth_match

def truth_booth(truth_booth_match, matches, alternate_matches):
    if truth_booth_match in matches or truth_booth_match in alternate_matches:
        return True
    else:
        return False


