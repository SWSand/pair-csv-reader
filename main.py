import csv

def main():
    animal_list = []
    user_choice = ''
    user_choice = input("Enter type of animal you would like to look at: ")

    try:
        with open(f'./data/{user_choice}.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                animal_list.append(row)
    except:
        print(f"Sorry, we don't have any {user_choice}.")

    for animal in animal_list:
        print(f"{animal['name']} is a {animal[' age']} year old {animal[' breed']}.")

if __name__ == "__main__":
    main()