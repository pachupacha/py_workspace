import time

def lab_mixer():
    print("\n🧪 Welcome to the Laboratory Mixer 🧪")
    substances = [
        "Sulfuric Acid (H₂SO₄)", "Water (H₂O)", "Sodium (Na)", "Alcohol (C₂H₅OH)", "Mercury (Hg)", "Ammonia (NH₃)"
    ]
    
    reactions = {
        ("Sulfuric Acid (H₂SO₄)", "Water (H₂O)"): ("Exothermic Reaction", "Releases extreme heat, potential splashes! ☠️", "H₂SO₄ + H₂O"),
        ("Sulfuric Acid (H₂SO₄)", "Sodium (Na)"): ("Hydrogen Gas Explosion", "Violent explosion with hydrogen gas release! 💥", "H₂SO₄ + Na"),
        ("Sulfuric Acid (H₂SO₄)", "Alcohol (C₂H₅OH)"): ("Ether Formation", "Forms ether, highly flammable! 🔥", "H₂SO₄ + C₂H₅OH"),
        ("Sulfuric Acid (H₂SO₄)", "Mercury (Hg)"): ("Mercury Sulfate Formation", "Forms toxic mercury sulfate and releases SO₂ gas ☠️", "H₂SO₄ + Hg"),
        ("Sulfuric Acid (H₂SO₄)", "Ammonia (NH₃)"): ("Ammonium Sulfate Formation", "Forms ammonium sulfate, safe but exothermic", "H₂SO₄ + NH₃"),
        ("Water (H₂O)", "Sodium (Na)"): ("Sodium Hydroxide Formation", "Explosive reaction, releases hydrogen gas! 💥", "H₂O + Na"),
        ("Water (H₂O)", "Alcohol (C₂H₅OH)"): ("Simple Mixture", "Mixes completely, no reaction", "H₂O + C₂H₅OH"),
        ("Water (H₂O)", "Mercury (Hg)"): ("No Reaction", "No reaction, mercury is insoluble", "H₂O + Hg"),
        ("Water (H₂O)", "Ammonia (NH₃)"): ("Ammonium Hydroxide Formation", "Dissolves to form ammonium hydroxide, mildly toxic", "H₂O + NH₃"),
        ("Sodium (Na)", "Alcohol (C₂H₅OH)"): ("Sodium Ethoxide Formation", "Reacts to form sodium ethoxide and releases hydrogen gas! 🔥", "Na + C₂H₅OH"),
        ("Sodium (Na)", "Mercury (Hg)"): ("Sodium Amalgam", "Forms a dangerous sodium amalgam! ⚠️", "Na + Hg"),
        ("Sodium (Na)", "Ammonia (NH₃)"): ("Sodium-Ammonia Solution", "Dissolves forming a deep blue sodium-ammonia solution", "Na + NH₃"),
        ("Alcohol (C₂H₅OH)", "Mercury (Hg)"): ("No Reaction", "No reaction under normal conditions", "C₂H₅OH + Hg"),
        ("Alcohol (C₂H₅OH)", "Ammonia (NH₃)"): ("No Significant Reaction", "No significant reaction", "C₂H₅OH + NH₃"),
        ("Mercury (Hg)", "Ammonia (NH₃)"): ("Mercury-Ammonium Compounds", "Forms explosive mercury-ammonium compounds! ☠️", "Hg + NH₃")
    }
    
    print("\nAvailable substances:")
    for i, substance in enumerate(substances, 1):
        print(f"{i}. {substance}")
    
    try:
        choice1 = int(input("Choose the first substance (number): ")) - 1
        choice2 = int(input("Choose the second substance (number): ")) - 1
        
        if choice1 < 0 or choice2 < 0 or choice1 >= len(substances) or choice2 >= len(substances):
            print("Invalid selection. Try again.")
            return
        
        substance1 = substances[choice1]
        substance2 = substances[choice2]
        
        if substance1 == substance2:
            print("You cannot mix a substance with itself!")
            return
        
        print(f"\n🔬 Mixing {substance1} and {substance2}... 🔬")
        time.sleep(2)
        
        reaction = reactions.get((substance1, substance2)) or reactions.get((substance2, substance1), ("No Reaction", "No reaction occurs.", "N/A"))
        print(f"\n💡 Reaction Name: {reaction[0]}\n🧪 Effect: {reaction[1]}\n🔢 Chemical Formula: {reaction[2]}")
        
    except ValueError:
        print("Invalid input. Use numbers only.")

if __name__ == "__main__":
    lab_mixer()