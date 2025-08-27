class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("Pet_type should be part of PET_TYPES")
        self.name=name
        self.pet_type=pet_type
        if owner is not None:
            self.owner=owner
        Pet.all.append(self)

class Owner:
    def __init__(self,name):
        self.name=name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner==self] 
    
    def add_pet(self,pet_value):
        if not isinstance(pet_value,Pet):
            raise ValueError("pet_value should be a type of Pet")
        Pet.owner=self
    
    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet:pet.name)