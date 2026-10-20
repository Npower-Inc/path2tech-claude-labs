"""
Text Adventure Game - Starter Version
Reads room data from rooms.csv and lets the player explore by typing
directions (north, south, east, west) until they reach the treasure room.
"""

import csv

ROOMS_FILE = "rooms.csv"


def load_rooms(filename):
    rooms = {}
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            room_id = row["room_id"]
            rooms[room_id] = {
                "description": row["description"],
                "north": row["north"],
                "south": row["south"],
                "east": row["east"],
                "west": row["west"],
                "is_treasure": row["is_treasure"].strip().lower() == "yes",
            }
    return rooms


def print_room(room):
    print(room["description"])
    exits = []
    for direction in ["north", "south", "east", "west"]:
        if room[direction]:
            exits.append(direction)
    print("Exits: " + ", ".join(exits))
    print()


def play_game(rooms):
    current_room_id = "start"

    print("Welcome to the Adventure Game!")
    print("Type a direction (north, south, east, west) to move, or 'quit' to exit.\n")

    while True:
        current_room = rooms[current_room_id]
        print_room(current_room)

        if current_room["is_treasure"]:
            print("You found the treasure! You win!")
            break

        command = input("> ").strip().lower()

        if command == "quit":
            print("Thanks for playing!")
            break

        if command in ["north", "south", "east", "west"]:
            next_room_id = current_room[command]
            if next_room_id:
                current_room_id = next_room_id
            else:
                print("You can't go that way.\n")
        else:
            print("I don't understand that command.\n")


if __name__ == "__main__":
    rooms = load_rooms(ROOMS_FILE)
    play_game(rooms)
