def weight_on_planets():
    """Takes a user input of their weight,
    then prints out their respective weight on Mars and Jupiter

    Args:
         None

    Returns:
         None
    """
    weight_on_earth = float(input("What do you weigh on earth? "))
    weight_on_mars = weight_on_earth * .38
    weight_on_jupiter = weight_on_earth * 2.34
    print("\nOn Mars you would weigh %s pounds."
          "\nOn Jupiter you would weigh %s pounds."
          % (weight_on_mars, weight_on_jupiter))


if __name__ == '__main__':
    weight_on_planets()
