name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s", %name)
print("He's %d cm tall." % round(height / 0.39370))
print("He's %d kg heavy.") % round(weight / 2.2046)
print("Actually that's not too heavy.")
print("He's got % eyes and % hair.") % (eyes, hair)
print("Hi's teeth are usually % depending on the coffee.") % teeth

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d") % (age, height, weight, age + height + weight)
