import pyttsx3 as ff

engine = ff.init()
engine.setProperty('volume', 4.0)
engine.setProperty('rate', 115)


def welcome_message():
    ff.speak('Hallo, willkommen im Sky Hotel')
    ff.speak("Geben Sie bitte Ihren Namen ein:")
    print("Bitte geben Sie Ihren Namen ein:")
    name = input()
    print("Ich freue mich, dass Sie da sind, Herr " + name)
    ff.speak("Ich freue mich, dass Sie da sind, Herr " + name)


def get_floor_number():
    while True:
        ff.speak('Wie lautet bitte Ihre Raumnummer?')
        room_number = input('Wie lautet Ihre Raumnummer? ')

        if not room_number.isdigit():
            ff.speak('Bitte geben Sie eine gültige Zahl ein.')
            print("Bitte geben Sie eine gültige Zahl ein.")
            continue

        room_number = int(room_number)

        if room_number > 350 or room_number < 1:
            ff.speak('Bitte geben Sie eine gültige Zahl ein.')
            continue
        else:
            return room_number


def get_floor_from_room_number(room_number):
    floor_mappings = {
        range(333, 351): '20. Stockwerk',
        range(314, 333): '19. Stockwerk',
        range(296, 314): '18. Stockwerk',
        range(278, 296): '17. Stockwerk',
        range(259, 278): '16. Stockwerk',
        range(240, 259): '15. Stockwerk',
        range(221, 240): '14. Stockwerk',
        range(203, 221): '13. Stockwerk',
        range(185, 203): '12. Stockwerk',
        range(172, 185): '11. Stockwerk',
        range(154, 172): '10. Stockwerk',
        range(136, 154): '9. Stockwerk',
        range(118, 136): '8. Stockwerk',
        range(100, 118): '7. Stockwerk',
        range(82, 100): '6. Stockwerk',
        range(64, 82): '5. Stockwerk',
        range(46, 64): '4. Stockwerk',
        range(28, 46): '3. Stockwerk',
        range(10, 28): '2. Stockwerk',
        range(1, 10): '1. Stockwerk'
    }

    for floor_range, floor_name in floor_mappings.items():
        if room_number in floor_range:
            return floor_name


def main():
    welcome_message()
    room_number = get_floor_number()
    floor = get_floor_from_room_number(room_number)
    ff.speak('Ihr Raum ist im ' + floor + '.')
    print('Ihr Raum ist im ' + floor + '.')
    ff.speak('Weitere Informationen finden Sie im Abschnitt Dienstleistungen.')
    print("Weitere Informationen finden Sie im Abschnitt Dienstleistungen.")
    ff.speak('Ich wünsche Ihnen eine schöne Zeit bei uns.')
    print("Ich wünsche Ihnen eine schöne Zeit bei uns.")


if __name__ == '__main__':
    main()