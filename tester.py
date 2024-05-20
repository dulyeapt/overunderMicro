
import requests


while True:
    print("TEST OPTIONS\n"
              " 1: TO VIEW API CALL INSTRUCTIONS\n"
              " 2: TO CALL API FOR OVERUNDER\n"
              " 3: EXIT THE TESTER\n")
    userImput = input("PLEASE ENTER YOUR CHOICE\n")

# 1 Call information from API
    if userImput == "1":
        api_url = "http://127.0.0.1:5010"
        response = requests.get(api_url)
        response.json()
        print(response.json())
        print("\n")

    if userImput == "2":
        compare_url = "http://127.0.0.1:5010/compare/"
        compare_max = int(input("\nPlEASE ENTER YOUR MAX VALUE \n"))
        compare_value = int(input("\nPLEASE ENTER YOUR TEST VALUE\n"))

        comparefull_url = compare_url + str(compare_max) + "/" + str(compare_value)
        response = requests.get(comparefull_url).json()
        print(response)
        results = response['Warning']
        print(results)
 

# 4 Handles users choice to exit the program
    if userImput.upper() == "3":
              exit()

# 5 Handles an entry that was not a valid option by the user              
    if userImput.upper() not in  ["1", "2", "3"]:
        print("\nPlease choose a valid option \n")