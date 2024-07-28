

def wrap_to_360(value):
    """ Converts legative values to positive values in the range [0, 360) 
    
    Args:
        value (float): The value to be wrapped

    Returns:
        float: The wrapped value

    Ex: 
        -10 -> 350
    """
    return (value + 360) % 360