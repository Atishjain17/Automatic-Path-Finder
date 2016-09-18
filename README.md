# Automatic-Path-Finder
A project which uses various traversal algorithms like BFS, DFS, UCS and A* along with loop detection to find a path between two locations on a map ( given in the form of input of road intersections ).

Project Description:
The Los Angeles Lakers are playing against their rivals the Boston Celtics tonight. Lakers star Jordan Clarkson wants to arrive earlier today to prepare himself for the game, and he is leaving from his mansion at Newport Coast to Staples Center. As everyone knows, Los Angeles is notorious for its traffic. Driving his 2016 Lamborghini Aventador, Jordan definitely does not want to be stuck in traffic. Please help Jordan find a route to get him to Staples Center as fast as possible.
To accomplish this, you will be given a list of freeway or road intersections (i.e., locations) and the time it would take to travel from there to other freeway or road intersections. You will be required to create a program that finds the fastest route Jordan must travel to get to Staples Center.
Your program will be given live traffic information in the input.txt file, which is an arbitrarily large list of current traveling times between intersections/locations.

Full specification for input.txt:
<ALGO>
<START STATE>
<GOAL STATE>
<NUMBER OF LIVE TRAFFIC LINES>
<… LIVE TRAFFIC LINES …>
<NUMBER OF SUNDAY TRAFFIC LINES>
<… SUNDAY TRAFFIC LINES …>
where:
  <ALGO> is the algorithm to use and will be one of: “BFS”, “DFS”, “UCS”, “A*”.
  <START STATE> is a string with the name of the start location (e.g., JordanHome).
  <GOAL STATE> is a string with the name of the goal location (e.g., StaplesCenter).
  <NUMBER OF LIVE TRAFFIC LINES> is the number of lines of live traffic information that follow.
  <… LIVE TRAFFIC LINES …> are lines of live traffic information in the format described below:
        <STATE1> <STATE2> <TRAVEL TIME FROM STATE1 TO STATE2>
  <NUMBER OF SUNDAY TRAFFIC LINES> is the number of lines of Sunday traffic estimates that follow.
  <… SUNDAY TRAFFIC LINES …> are lines of sunday traffic information in the following format:
        <STATE> <ESTIMATED TIME FROM STATE TO GOAL>

Full specification for output.txt:
Any number of lines with the following format for each:
  <STATE> <ACCUMULATED TRAVEL TIME FROM START TO HERE>

Additional notes:
- Times are positive or zero integers (32-bit ok, larger ok too).
- Capitalization of state names will be maintained.
- State names will not have any white spaces in them and will consist of ASCII letters,
numbers and/or other non-special ASCII characters.
- There will not be any duplicate entries in the live traffic data.
- There will be exactly one entry in the Sunday traffic data for each state mentioned in the
live traffic data.
- Intersections of 2 freeways are always given in the same order. For example, when
referring to I110/I405, it is always I110/I405, rather than sometimes I405/I110 and
sometimes I110/I405.
- In output.txt, the first line should always be “<START STATE> 0” and the last line’s state
should always be <GOAL STATE> (and the total accumulated travel time should follow).
- Hence, if the start state is the same as the goal state, you should output a single line
“<START STATE> 0”.
- The goal state will always be reachable from the start state.
- If all else is equal while searching routes (ties), you should explore (enqueue) multiple
paths from the same intersection in the order in which they are listed in the live traffic
inputs.
- The Sunday traffic information may or may not be admissible. We understand that when
it is not admissible your solution may not be optimal.
