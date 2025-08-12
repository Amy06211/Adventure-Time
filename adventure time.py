import random

data = {
  "names": [
    "Finnick", "Glim", "Zora", "Quibble", "Luma", "Marn", "Drix",
    "Fizz", "Tilly", "Jax", "Pogo", "Zephyr", "Nix", "Ember", "Sprocket", "Bramble"
  ],
  "genders": [
    "Male", "Female"
  ],
  "haircuts": [
    "Short and spiky", "Long and flowing", "Curly and wild", "Bald", "Mohawk",
    "Braided", "Messy and unkempt", "Ponytail", "Side-swept bangs", "Pixie cut"
  ],
  "hair_colors": [
    "Blonde", "Brown", "Black", "Red", "Blue", "Green", "Pink", "Purple", "White", "Multicolored"
  ],
  "skin_colors": [
    "Light peach", "Pale blue", "Grass green", "Lavender purple", "Warm brown",
    "Bubblegum pink", "Slate gray", "Sunset orange", "Pastel yellow", "Transparent"
  ],
  "eye_colors": [
    "Deep blue", "Emerald green", "Hazel brown", "Jet black", "Golden yellow",
    "Crimson red", "Violet purple", "Milky white", "Glowing cyan", "Shimmering silver"
  ],
  "clothes": {
    "pants": [
      "Denim shorts", "Loose linen pants", "Striped trousers", "Leather armor pants",
      "Simple skirt", "Baggy cargo pants", "Flowing robe bottom", "None"
    ],
    "shirts": [
      "Graphic tee", "Sleeveless tunic", "Hooded sweatshirt", "Shiny chestplate",
      "Flowing wizard robe", "Crop top", "Wool sweater", "Patchwork vest"
    ],
    "accessories": [
      "Pointy wizard hat", "Round glasses", "Beaded necklace", "Wide leather belt",
      "Adventure backpack", "Fingerless gloves", "Colorful scarf", "Spiked wristbands", "Hoop earrings"
    ],
    "shoes": [
      "Sturdy boots", "Lightweight sneakers", "Leather sandals", "Barefoot", "Armored greaves"
    ]
  },
  "powers": [
    "Fire breathing", "Ice shard creation", "Shape-shifting into animals",
    "Teleporting short distances", "Growing and controlling plants", "Super strength and durability",
    "Turning invisible", "Casting elemental magic", "Talking to animals",
    "Manipulating time for a few seconds", "Healing wounds", "Creating protective bubbles",
    "Expert sword fighting skills"
  ],
  "relationships_with_finn_and_jake": [
    "Finn’s adventurous new ally", "Jake’s mischievous partner", "Finn’s rival in bravery",
    "Jake’s loyal protector", "Long-lost sibling of Finn", "Mysterious enemy from the Ice Kingdom",
    "Friendly neighbor in the Candy Kingdom", "Magical mentor guiding Finn",
    "Mischievous troublemaker who annoys Jake", "Creature who idolizes both Finn and Jake"
  ]
}

p = input("What can I do for you? ")
if "character" in p.lower().split():
    print("Sure, let's do it!")
    print("Ask about its look, clothes and his life or type 'exit' to quit:")
    while True:
        answer = input().lower()
        if answer == "exit":
            break
        
        if "name" in answer:
            print(random.choice(data["names"]))
        if "gender" in answer:
            print(random.choice(data["genders"]))
        if "haircut" in answer:
            print(random.choice(data["haircuts"]))
        if "hair color" in answer:
            print(random.choice(data["hair_colors"]))
        if "skin color" in answer:
            print(random.choice(data["skin_colors"]))
        if "eye color" in answer:
            print(random.choice(data["eye_colors"]))
        if "pants" in answer:
            print(random.choice(data["clothes"]["pants"]))
        if "shirt" in answer:
            print(random.choice(data["clothes"]["shirts"]))
        if "accessories" in answer:
            print(random.choice(data["clothes"]["accessories"]))
        if "shoes" in answer:
            print(random.choice(data["clothes"]["shoes"]))
        if "power" in answer:
            print(random.choice(data["powers"]))
        if "relationship" in answer:
            print(random.choice(data["relationships_with_finn_and_jake"]))
else:
    print("I can't do that")