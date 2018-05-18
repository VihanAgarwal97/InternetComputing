#Import the requests package that allows us to access the Metro Transit API
import requests

#Method to get the directions of the selected route
def getDirections():
    #Global variable to hold the users route
    global myRoute
    myRoute = input("Which route do you want to take:")

    link = 'http://svc.metrotransit.org/NexTrip/Directions/' + myRoute + '?format=json'
    d = requests.get(link)
    #Global variable to hold the directions list returned from the API
    global directions
    directions = d.json()
    try:
        #Global variable to hold the two directions of the bus
        global dir1,dir2
        dir1= directions[0].get('Text')
        dir2= directions[1].get('Text')
    except IndexError:
        print("Wrong route entered!")
    else:
        getStops()

#Method to get the stops of a particular route and direction
def getStops():
    #Global variable to hold the users selected directions
    global myDir
    myDir = int(input('Enter 1 for ' + dir1 + ' and 2 for ' + dir2 + ':'))
    if myDir == 1:
        routeCode = directions[0].get('Value')
    elif myDir == 2:
        routeCode = directions[1].get('Value')
    else:
        print("Wrong choice entered!")
        return

    link = 'http://svc.metrotransit.org/NexTrip/Stops/' + myRoute + '/' + routeCode + '?format=json'
    s = requests.get(link)
    #Global variable to hold the list of all stops of a particular route
    global stops
    stops = s.json()
    getTimes()

#Method to get the times of the buses at a particular stop
def getTimes():
    #Prints all the stops to the user
    for stop in stops:
        print(stop.get('Text') + ":" + stop.get('Value'))
    myStop = input("Enter a stop code from the list above:")
    link = "http://svc.metrotransit.org/NexTrip/"+ myRoute +'/'+ str(myDir) + "/" + myStop +"?format=json"
    st = requests.get(link)
    myTimes = st.json()
    
    #Prints the times to the users
    try:
       print("The next bus is in/at " + myTimes[0].get('DepartureText'))
    except IndexError:
       print("Error! Please check the stop code entered. If you entered the correct code, there is no bus available at this stop")


getDirections()