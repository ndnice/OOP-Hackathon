from pet import Pet

# Create a pet object
my_pet = Pet(name="Silky")

# Display the initial status of the pet
print("Initial Status:")
my_pet.get_status()

# Teach the pet some tricks
print("\nTeaching tricks:")
my_pet.train("Roll Over")
my_pet.train("Play Dead")

# Show all learned tricks
print("\nLearned Tricks:")
my_pet.show_tricks()

# Interact with the pet
print("\nInteracting with the pet:")
my_pet.eat()
my_pet.sleep()
my_pet.play()

# Display the updated status of the pet
print("\nUpdated Status:")
my_pet.get_status()