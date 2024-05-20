import requests

# Test code for the API. Also demonstrates the call formate and how to build the url needed for the call.
while True:
    print("TEST OPTIONS\n"
              " 1: TO VIEW API CALL INSTRUCTIONS\n"
              " 2: TO CALL API FOR INT OVERUNDER\n"
              " 3: TO CALL API FOR FLOAT OVERUNDER\n"
              " 4: EXIT TESTER\n")
    userImput = input("PLEASE ENTER YOUR CHOICE\n")

# 1 Call information from API
    if userImput == "1":
        api_url = "http://127.0.0.1:5010"
        response = requests.get(api_url)
        response.json()
        print(response.json())
        print("\n")

    if userImput == "2":
        compare_url = "http://127.0.0.1:5010/compareInt/"
        compare_max = int(input("\nPlEASE ENTER YOUR MAX VALUE \n"))
        compare_value = int(input("\nPLEASE ENTER YOUR TEST VALUE\n"))

        comparefull_url = compare_url + str(compare_max) + "/" + str(compare_value)
        response = requests.get(comparefull_url).json()
        print(response)
        results = response['Warning']
        print(results)
        print("\n")

    if userImput == "3":
        compare_url = "http://127.0.0.1:5010/compareFloat/"
        compare_max = float(input("\nPlEASE ENTER YOUR MAX VALUE \n"))
        compare_value = float(input("\nPLEASE ENTER YOUR TEST VALUE\n"))

        comparefull_url = compare_url + str(compare_max) + "/" + str(compare_value)
        response = requests.get(comparefull_url).json()
        print(response)
        results = response['Warning']
        print(results)

# 4 Handles users choice to exit the program
    if userImput.upper() == "4":
              exit()

# 5 Handles an entry that was not a valid option by the user              
    if userImput.upper() not in  ["1", "2", "3", "4"]:
        print("\nPlease choose a valid option \n")