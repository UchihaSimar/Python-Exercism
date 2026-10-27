def response(hey_bob):
    final_hey_bob = hey_bob.strip()
    if final_hey_bob.endswith("?") and final_hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if final_hey_bob.endswith("?"):
        return "Sure."
    if final_hey_bob.isupper():
        return "Whoa, chill out!"
    if len(final_hey_bob) == 0:
        return "Fine. Be that way!"
    return "Whatever."
    
    
    
