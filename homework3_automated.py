## Automated program to run all 69 sample input files for all 4 algorithms
for p in range(70):
        print("***************************"+str(p)) /// Displays currebt file number
        input_file_name='input'+str(p)+'.txt'
        output_file_name='output\output'+str(p)+'.txt'
        f = open(output_file_name, "w")
        f.write(input_file_name+'\n')
        f.close()
        r = open('output\output_combined.txt','a')
        r.write('\n'+input_file_name+'\n')
        r.close()

        ### Input Code
        ip='input_all\\'+ input_file_name
        input_file = open(ip,'r')
        input = input_file.read()
        input_file.close()
        input = input.split('\n')

        ## Declaring Global Variables
       # global opened
       # global closed
       # opened = []
       # closed = []
        global start_state
        global goal_state
        global live_TrafficLines
        global sunday_TrafficLines
        ## Global Variables Declared

        #Assigining values
        # Algo, Start State, Goal State, No. of live Traffic lines, Live TrafficLines, /
        # no. of Sunday Traffic Lines, Sunday Traffic Lines
        algos=['BFS','DFS','UCS','A*']
        #algo = input[0].upper()
        start_state = input[1]
        goal_state = input[2]

        # Assigining live Traffic Lines
        # liveTrafficLines (From,To,Cost,RouteNo.)
        no_of_Live_TrafficLines = int(input[3])
        live_TrafficLines_temp =[]
        liveTraffic_line_no = no_of_Live_TrafficLines+4
        for i in range(4, liveTraffic_line_no):
            live_TrafficLines_temp.append(input[i]+" "+ str(i-4))

        live_TrafficLines = []
        for i in range(len(live_TrafficLines_temp)):
            live_TrafficLines.append(live_TrafficLines_temp[i].split(' '))

        for i in range(len(live_TrafficLines)):
            live_TrafficLines[i][2] = int(live_TrafficLines[i][2])
            live_TrafficLines[i][3] = int(live_TrafficLines[i][3])
        print(live_TrafficLines)
        # Finished assigning live traffic lines with an extra last column which gives /
        # the order in which input arrived

        # Assigining sunday Traffic Lines
        # sundayTrafficLines (From,Cost)
        no_of_Sunday_TrafficLines = int(input[liveTraffic_line_no])
        sunday_TrafficLines_temp =[]
        for i in range(liveTraffic_line_no+1, liveTraffic_line_no+no_of_Sunday_TrafficLines+1):
            sunday_TrafficLines_temp.append(input[i])

        sunday_TrafficLines = []
        for i in range(len(sunday_TrafficLines_temp)):
            sunday_TrafficLines.append(sunday_TrafficLines_temp[i].split(' '))

        for i in range(len(sunday_TrafficLines)):
            sunday_TrafficLines[i][1] = int(sunday_TrafficLines[i][1])
        print (sunday_TrafficLines)
        # Finished assigning sunday traffic lines
        # All values assigned from input file
        ### Input Code Completed

        ### Create a Node_Table Class
        class Node_State(object):
            """A class that makes a queue type table of nodes"""
            def __init__(self, node, state, g, depth, parent):
                self.node = node
                self.state = state
                self.g = g
                self.depth = depth
                self.parent = parent

            def description(self):
                return "I'm node %d. My State is %s, cost is %d, depth is %d. My parent is node %d" % (self.node, self.state, self.g, self.depth, self.parent)
        ### Node_Table Class Created

        class Node_State_Heuristic(object):
            """A class that makes a queue type table of nodes"""
            def __init__(self, node, state, g, depth, parent, h, f):
                self.node = node
                self.state = state
                self.g = g
                self.depth = depth
                self.parent = parent
                self.h = h
                self.f =f

            def description(self):
                return "I'm node %d. My State is %s, cost is %d, depth is %d,heuristic cost is %d and f_n is %d. My parent is node %d" % (self.node, self.state, self.g, self.depth, self.h, self.f, self.parent)
        ### Node_Table Class Created

        ###Define printtofile
        def findparent(parent_node):
            for i in range(len(closed)):
                if closed[i].node == parent_node:
                    print ('FINDPARENT:'+str(i))
                    return i
            else:
                print ('Parent Not Found')

        def printtofile(sol):
            print("Printing To File")
            solution=[]
            solution.append([sol.state, sol.g])
            parent_node=sol.parent
            for i in range (len(closed)):
                print(closed[i].description())
            while(parent_node!=0):
                j=findparent(parent_node)
                parent_found=closed[j]
                solution.append([parent_found.state,parent_found.g])
                parent_node = parent_found.parent
            print (solution)

            f = open(output_file_name, "a")
            r = open('output\output_combined.txt', "a")
            f.write(algo+"\n")
            r.write(algo+"\n")
            for i in solution[::-1]:
                print (i)
                f.write(i[0]+" "+str(i[1])+"\n")
                r.write(i[0]+" "+str(i[1])+"\n")
            f.close()
            r.close()
        ### Printtofile defined

        ### BFS
        def BFS():

            node_state_no = 1
            root_node = Node_State(node_state_no,start_state,0,0,0)
            opened.append(root_node)

            while (opened != []):
                currnode = opened.pop(0)
                print("Current Node: "+ currnode.state)
                if(currnode.state == goal_state):
                    print('Success')
                    return currnode
                else:
                    closed.append(currnode)
                    children=[]
                    for i in range(len(live_TrafficLines)):
                        if(currnode.state == live_TrafficLines[i][0]):
                            children.append(live_TrafficLines[i])

                    for i in range(len(children)):
                        opens = 0
                        closes = 0
                        currchild=children[i][1]
                        for j in range(len(opened)):
                            if(currchild == opened[j].state):
                                print("Open:"+currchild)
                                opens = 1
                                break
                        for j in range(len(closed)):
                            if(currchild == closed[j].state):
                                print("Closed")
                                closes = 1
                                break
                        if (opens!=1 and closes!=1):
                            node_state_no += 1
                            g=currnode.g + children[i][2]
                            depth=currnode.depth + 1
                            parent=currnode.node
                            opened.append(Node_State(node_state_no,currchild,g,depth,parent))
                            if(currchild == goal_state):
                                print ('Success')
                                z = opened.pop(-1)
                                return z
                    print("Final")
                    for i in range(len(opened)):
                        print(opened[i].description())
            else:
                return 'Failure'
        ### BFS defined

        def DFS():
            node_state_no = 1
            root_node = Node_State(node_state_no,start_state,0,0,0)
            opened.append(root_node)
            print(opened[0].description())

            while (opened != []):
                currnode = opened.pop(-1)
                print("Current Node: "+ currnode.state)
                if(currnode.state == goal_state):
                    print('Success')
                    return currnode
                else:
                    closed.append(currnode)
                    children=[]
                    for i in range(len(live_TrafficLines)):
                        if(currnode.state == live_TrafficLines[i][0]):
                            children.insert(0,live_TrafficLines[i])
                    print (children)
                    for i in range(len(children)):
                        opens = 0
                        closes = 0
                        k = 0
                        currchild=children[i][1]
                        print(currchild)
                        for j in range(len(opened)):
                            if(currchild == opened[j].state):
                                print("Open:"+currchild)
                                opens = 1
                                k = j
                                break
                        for j in range(len(closed)):
                            if(currchild == closed[j].state):
                                print("Closed")
                                closes = 1
                                break
                        if (closes!=1):
                            node_state_no += 1
                            g=currnode.g + children[i][2]
                            depth=currnode.depth + 1
                            parent=currnode.node
                            if(opens == 1 and depth > opened[k].depth):
                                print("Skip Node...Loop Detection")
                            else:
                                opened.append(Node_State(node_state_no,currchild,g,depth,parent))
                    for i in range(len(opened)):
                        print(opened[i].description())
            else:
                return 'Failure'
        ### DFS defined

        ### UCS
        def UCS():

            node_state_no = 1
            root_node = Node_State(node_state_no,start_state,0,0,0)
            opened.append(root_node)

            while (opened != []):
                currnode = opened.pop(0)
                print("Current Node: "+ currnode.state)
                if(currnode.state == goal_state):
                    print('Success')
                    return currnode
                else:
                    closed.append(currnode)
                    children=[]
                    for i in range(len(live_TrafficLines)):
                        if(currnode.state == live_TrafficLines[i][0]):
                            children.append(live_TrafficLines[i])

                    #print (children)
                    for i in range(len(children)):
                        currchild=children[i][1]
                        k = -1
                        opens = 0
                        closes = 0
                        for j in range(len(opened)):
                            if(currchild == opened[j].state):
                                print("Open")
                                opens=1
                                k = j
                                break
                        for j in range(len(closed)):
                            if(currchild == closed[j].state):
                                print("Closed")
                                k = j
                                closes=1
                                break
                        if (i<len(children)):
                            node_state_no += 1
                            g=currnode.g + children[i][2]
                            depth=currnode.depth + 1
                            parent=currnode.node
                            if(opens == 1 ):
                                if(g < opened[k].g):
                                  removednode = opened.pop(k)
                                  print("Node removed from open:" + removednode.description())
                                  opened.append(Node_State(node_state_no,currchild,g,depth,parent))

                            elif(closes == 1):
                                if(g < closed[k].g):
                                  removednode = closed.pop(k)
                                  print("Node removed from close:" + removednode.description())
                                  opened.append(Node_State(node_state_no,currchild,g,depth,parent))

                            else:
                                opened.append(Node_State(node_state_no,currchild,g,depth,parent))
                            print("Before sorting")
                            for i in range(len(opened)):
                                print(opened[i].description())
                            opened.sort(key=lambda x: x.g)
                            print("After sorting")
                            for i in range(len(opened)):
                                print(opened[i].description())

                    for i in range(len(opened)):
                        print(opened[i].description())
            else:
                return 'Failure'
        ### UCS Defined

        ### Astar
        def AStar():

            node_state_no = 1
            root_node = Node_State_Heuristic(node_state_no,start_state,0,0,0,sunday_TrafficLines[0][1],sunday_TrafficLines[0][1])
            opened.append(root_node)

            while (opened != []):
                currnode = opened.pop(0)
                print("Current Node: "+ currnode.state)
                if(currnode.state == goal_state):
                    print('Success')
                    return currnode
                else:
                    closed.append(currnode)
                    children=[]
                    for i in range(len(live_TrafficLines)):
                        if(currnode.state == live_TrafficLines[i][0]):
                            children.append(live_TrafficLines[i])

                    for i in range(len(children)):
                        currchild=children[i][1]
                        k = -1
                        opens = 0
                        closes = 0
                        child_index = -1
                        for j in range(len(sunday_TrafficLines)):
                            if(currchild == sunday_TrafficLines[j][0]):
                                print(sunday_TrafficLines[j])
                                child_index = j
                                break
                            else:
                                print("child not in sunday traffic lines so assume the cost as that of last traffic line which will be 0 if it is admissible")
                        for j in range(len(opened)):
                            if(currchild == opened[j].state):
                                print("Open")
                                opens=1
                                k = j
                                break
                        for j in range(len(closed)):
                            if(currchild == closed[j].state):
                                print("Closed")
                                k = j
                                closes=1
                                break
                        if (i<len(children)):
                            node_state_no += 1
                            g=currnode.g + children[i][2]
                            depth=currnode.depth + 1
                            parent=currnode.node
                            h=sunday_TrafficLines[child_index][1]
                            f=g+h
                            if(opens == 1 ):
                                if(g < opened[k].g):
                                  removednode = opened.pop(k)
                                  print("Node removed from open:" + removednode.description())
                                  opened.append(Node_State_Heuristic(node_state_no,currchild,g,depth,parent,h,f))

                            elif(closes == 1):
                                if(g < closed[k].g):
                                  removednode = closed.pop(k)
                                  print("Node removed from close:" + removednode.description())
                                  opened.append(Node_State_Heuristic(node_state_no,currchild,g,depth,parent,h,f))

                            else:
                                opened.append(Node_State_Heuristic(node_state_no,currchild,g,depth,parent,h,f))
                            opened.sort(key=lambda x: x.f)
                            print("After sorting")
                            for i in range(len(opened)):
                                print(opened[i].description())

            else:
                return 'Failure'
        ### Astar defined

        for all_algos in range(len(algos)):

                opened = []
                closed = []
                algo = algos[all_algos]
                ### BFS
                if (algo == 'BFS'):
                    sol= BFS()
                    if (sol == 'Failure'):
                        print('Failure')
                    else:
                        closed.append(sol)
                        print ("Solution:"+sol.description())
                        for i in range(len(closed)):
                            closed[i].g=closed[i].depth
                        printtofile(sol)
                    print ('BFS')
                ### BFS Completed

                ### DFS
                elif (algo == 'DFS'):
                    sol= DFS()
                    if (sol == 'Failure'):
                        print('Failure')
                    else:
                        closed.append(sol)
                        print ("Solution:"+sol.description())
                        for i in range(len(closed)):
                            closed[i].g=closed[i].depth
                        printtofile(sol)
                    print ('DFS')
                ### DFS Completed

                ### UCS
                elif (algo == 'UCS'):
                    sol= UCS()
                    if (sol == 'Failure'):
                        print('Failure')
                    else:
                        closed.append(sol)
                        print ("Solution:"+sol.description())
                        printtofile(sol)
                    print ('UCS')
                ### UCS Completed

                ### A*
                elif (algo == 'A*'):
                    sol= AStar()
                    if (sol == 'Failure'):
                        print('Failure')
                    else:
                        closed.append(sol)
                        print ("Solution:"+sol.description())
                        printtofile(sol)
                    print ('A*')
                ### A* Completed
                else:
                    print('Invalid Algo')
