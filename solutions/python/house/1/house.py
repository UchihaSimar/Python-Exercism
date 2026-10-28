# house.py

# List of components starting from the foundation up to the last addition.
# Each item contains the subject/description and the action connecting it to the next.
COMPONENTS = [
    ("the house", "that Jack built."),
    ("the malt", "that lay in "),
    ("the rat", "that ate "),
    ("the cat", "that killed "),
    ("the dog", "that worried "),
    ("the cow with the crumpled horn", "that tossed "),
    ("the maiden all forlorn", "that milked "),
    ("the man all tattered and torn", "that kissed "),
    ("the priest all shaven and shorn", "that married "),
    ("the rooster that crowed in the morn", "that woke "),
    ("the farmer sowing his corn", "that kept "),
    ("the horse and the hound and the horn", "that belonged to ")
]

def get_verse(verse_num):
    """Generates a single verse based on its index (1-based)."""
    # Adjust for 0-based indexing
    idx = verse_num - 1
    
    # Start the verse with the target subject
    parts = [f"This is {COMPONENTS[idx][0]} "]
    
    # Work backwards to embed all previous historical clauses
    for i in range(idx, -1, -1):
        if i == 0:
            parts.append(COMPONENTS[i][1])
        else:
            parts.append(COMPONENTS[i][1])
            parts.append(f"{COMPONENTS[i-1][0]} ")
            
    return "".join(parts)

def recite(start_verse, end_verse):
    """Returns a list of verses from start_verse to end_verse inclusive."""
    return [get_verse(v) for v in range(start_verse, end_verse + 1)]
