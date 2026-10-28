def commands(binary_str):
    correct_action_order = binary_str[::-1]
    result = []
    if correct_action_order[0] == "1":
        result.append("wink")

    if correct_action_order[1] == "1":
        result.append("double blink")

    if correct_action_order[2] == "1":
        result.append("close your eyes")

    if correct_action_order[3] == "1":
        result.append("jump")

    if correct_action_order[4] == "1":
        result.reverse()

    return result
    
    
