def get_input(text):
    while True:
        try:
            tmp = int(input(text))
            break
        except ValueError:
            print("It must be digit.")
    return tmp
