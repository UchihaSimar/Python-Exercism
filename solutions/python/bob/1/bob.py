def response(hey_bob):
    final_hey_bob = hey_bob.strip()
    if final_hey_bob.endswith("?") and final_hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif final_hey_bob.endswith("?"):
        return "Sure."
    elif final_hey_bob.isupper():
        return "Whoa, chill out!"
    elif len(final_hey_bob) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."
    
    
    
