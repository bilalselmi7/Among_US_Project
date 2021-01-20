def Step1():
    #!/usr/bin/env python
    # coding: utf-8
    
    # ## Generate random score / name
    
    # In[1]:
    
    
    import random 
    from IPython.display import clear_output
    
    def random_score():
        score = random.randint(0,12)
        return score
    random_score()
    
    def random_name():
        low = "abcdefghijklmnopqrstuvwxyz"
        up  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
    #     sym = "()[]{}*:/,;_-"
        all = low + up + num #+ sym
        length = 5
        name = "".join(random.sample(all,length))
        return name
    random_name()
    
    
    # ## Class Player
    
    # In[2]:
    
    
    class Player:
        def __init__(self):
            self.name = random_name()
            self.score = random_score()
            
        def __str__(self):
            return "Name : {}, Score : {}".format(self.name, self.score)
        
        def __lt__(self,player):
            return self.score<player.score
    
        def __gt__(self,player):
            return self.score>player.score
        
        def __ge__(self,player):
            return self.score>=player.score
        
        def __le__(self,player):
            return self.score<=player.score
    
    
    # ## Class Node
    
    # In[3]:
    
    
    class Node():
        
        def __init__(self,value, left=None,right=None):
            self.value = value
            self.left = left
            self.right = right
            self.height = 1
            
        def display(self):
            lines, *_ = self._display_aux()
            for line in lines:
                print(line)
    
        def _display_aux(self):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if self.right is None and self.left is None:
                line = '%s' % self.value
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle
    
            # Only left child.
            if self.right is None:
                lines, n, p, x = self.left._display_aux()
                s = '%s' % self.value
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    
            # Only right child.
            if self.left is None:
                lines, n, p, x = self.right._display_aux()
                s = '%s' % self.value
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
                # Two children.
            left, n, p, x = self.left._display_aux()
            right, m, q, y = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
    
            
            
        def __str__(self):
            return str(self.value)
        
        
    class AVL_Tree(object): 
        
    
        def RotationLeft(self, x): 
            y = x.right 
    #         try:
            T2 = y.left 
            y.left = x 
            x.right = T2 
            x.height =  max(self.Height(x.left), self.Height(x.right)) + 1
            y.height =  max(self.Height(y.left), self.Height(y.right)) + 1
            return y 
    #         except:
    #             pass
      
        def RotationRight(self, y): 
      
            x = y.left 
    #         try:
            T3 = x.right 
            x.right = y
            y.left = T3 
            y.height = max(self.Height(y.left), self.Height(y.right)) + 1
            x.height = max(self.Height(x.left), self.Height(x.right)) + 1
            return x 
    #         except:
    #             pass
            
    
      
        def Height(self, root): 
            if root == None:  
                return 0
            return root.height 
      
        def Balance(self,root): 
            if root == None: 
                return 0
            return self.Height(root.left) - self.Height(root.right) 
      
        def insert(self, root, key): 
          
            # 1. Perform normal BST 
            if not root: 
                return Node(key) 
            if key < root.value: 
                root.left = self.insert(root.left, key) 
            else: 
                root.right = self.insert(root.right, key) 
      
            # 2. Update the height of the  
            
            root.height = 1 + max(self.Height(root.left), 
                               self.Height(root.right)) 
      
            # 3. Get the balance factor 
            balance = self.Balance(root) 
      
            # 4. If node is unbalanced then we check where the inbalance is
            # Left Left 
            if (balance > 1) and (key <= root.left.value): 
                return self.RotationRight(root) 
      
            # Right Right 
            if (balance < -1) and (key >= root.right.value): 
                return self.RotationLeft(root) 
      
            # Left Right 
            if (balance > 1) and (key > root.left.value): 
                root.left = self.RotationLeft(root.left) 
                return self.RotationRight(root) 
      
            # Right Left 
            if (balance < -1) and (key < root.right.value): 
                root.right = self.RotationRight(root.right) 
                return self.RotationLeft(root) 
      
            return root 
    
        def delete(self, root, key): 
      
            if root == None: 
                return root 
      
            elif (key < root.value): 
                root.left = self.delete(root.left, key) 
            elif (key > root.value): 
                root.right = self.delete(root.right, key) 
      
            else: 
                if root.left is None: 
                    temp = root.right 
                    root = None
                    return temp 
      
                elif root.right is None: 
                    temp = root.left 
                    root = None
                    return temp 
      
                temp = self.getMinvalueNode(root.right) 
                root.value = temp.value 
                root.right = self.delete(root.right, 
                                          temp.value) 
            if root == None: 
                return root 
      
            root.height = 1 + max(self.Height(root.left),self.Height(root.right)) 
       
            balance = self.Balance(root) 
    
            #  Left Left 
            if (balance> 1) and (self.Balance(root.left) >= 0): 
                return self.RotationRight(root) 
      
            # Right Right 
            if (balance < -1) and (self.Balance(root.right) <= 0): 
                return self.RotationLeft(root) 
      
            # Left Right 
            if (balance > 1) and (self.Balance(root.left) < 0): 
                root.left = self.RotationLeft(root.left) 
                return self.RotationRight(root) 
      
            # Right Left 
            if (balance < -1) and (self.Balance(root.right) > 0): 
                root.right = self.RotationRight(root.right) 
                return self.RotationLeft(root) 
      
            return root 
          
      
        def getMinvalueNode(self, root): 
            if root is None or root.left is None: 
    #             return "Minimum Root Value: {}".format(root)
                return root
      
            return self.getMinvalueNode(root.left) 
        
        
        # def del_last_ten(self,root):
        #     for i in range(10):
        #         root = Tree.delete(root,Tree.getMinvalueNode(root).value)
        #     return root
        
        def preOrder(self,root):
            if root == None:
                return
            print("{0}\n ".format(root.value), end="") 
            self.preOrder(root.left) 
            self.preOrder(root.right) 
    
    
    # In[4]:
    
    
    def inOrder(root, liste=[]):
        if root:
            inOrder(root.left, liste) 
            liste.append(root.value)
            inOrder(root.right, liste)
    
    
    # In[5]:
    
    
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    
    # In[6]:
    
    
    def update(Tree, root):
        l=[]
        inOrder(root,l)
        root=None
        for i in l:
    #         i = round((random_score()+random_score()+random_score())/3) uncomment if working with int only
            i.score = i.score + (random_score()+random_score()+random_score())/3
            root = Tree.insert(root,i)
        return root
    
    
    # In[7]:
    
    
    def update_final(Tree, root):
        l=[]
        inOrder(root,l)
        root=None
        for i in l:
            i.score = 0
            root = Tree.insert(root,i)
        return root
    
    
    # In[8]:
    
    
    def update_final_final(Tree, root):
        l=[]
        inOrder(root,l)
        root=None
        for i in l:
            i.score = (random_score()+random_score()+random_score())/5
            root = Tree.insert(root,i)
        return root
    
    
    # In[9]:
    
    
    def Create_Tree():
        Tree = AVL_Tree()
        root = None
        for i in range(100): 
            root = Tree.insert(root,Player())
        return root
    
    
    # In[10]:
    
    
    def delete_last_ten(Tree,root):  
        for i in range(10):
            root = Tree.delete(root,Tree.getMinvalueNode(root).value)
        return root
    
    
    # In[15]:
    
    
    def Tournament():
        Tree=AVL_Tree()
        root = Create_Tree()
        print("------------------------------")
        Tree.preOrder(root)
        print("------------------------------")
        
        for i in range(9):
            if (count_nodes(root) % 10 == 0):
                root = delete_last_ten(Tree,root)
                root = update(Tree,root)
                Tree.preOrder(root)
                print("\nNumber of players left : \n" + str(count_nodes(root)))
                input("Press Enter to continue")
                clear_output()
        print("\nThere is only 10 players left, let's reset all the scores ! ")
        root = update_final(Tree,root)
        Tree.preOrder(root)
        
        print("\nNow, let's play the 5 final games !!\n")
        root = update_final_final(Tree,root)
        Tree.preOrder(root)
        L=[]
        inOrder(root,L)
        L.sort(reverse=True)
        print("\n----------------------------------------------")
        print("Here is the ranking of the final 10 players ")
        print("----------------------------------------------")
        [print(i) for i in L]
        print("\nAnd the winner is : {} ".format(L[0].name), end="") 
        
    Tournament()

#%%    
def Step2():
    #!/usr/bin/env python
    # coding: utf-8
    
    # In[130]:
    
    
    
    class Graph2(object):
        def __init__(self, dictionary=None):
            if dictionary == None:
                dictionary = {}
            self.dictionary = dictionary
    
        def vertices(self):
            return list(self.dictionary.keys())
    
    
    
    def Potential_Impostors(graph):
        tab =  {
            vertex: {
                other_vertex: (
                    0 if other_vertex == vertex or other_vertex in graph.dictionary[vertex] else 1
                )
                for other_vertex in graph.vertices()
            } for vertex in graph.vertices()
        }
        liste = ["1","4","5"]
        for i in range(len(liste)):
            print("\n\nKnowing that Player {} may be an Impostor, the other one may be among those players : ".format(liste[i]))
            for j in tab[liste[i]]:
                if tab[liste[i]][j] == 1:
                    print("Player", j, "||",end=" ")
    
                    
    
    graph = Graph2({
        "0": ["1", "4", "5"], # Player 0 saw Players 1, 4 and 5
        "1": ["0", "2", "6"], # Player 1 saw Players 0, 2 and 6
        "2": ["1", "3", "7"], # Player 2 saw Players 1, 3 and 7
        "3": ["2", "4", "8"], # Player 3 saw Players 2, 4 and 8
        "4": ["0", "3", "9"], # Player 4 saw Players 0, 3 and 9
        "5": ["0", "7", "8"], # Player 5 saw Players 0, 7 and 8
        "6": ["1", "8", "9"], # Player 6 saw Players 1, 8 and 9
        "7": ["2", "5", "9"], # Player 7 saw Players 2, 5 and 9
        "8": ["3", "5", "6"], # Player 8 saw Players 3, 5 and 6
        "9": ["4", "6", "7"]  # Player 9 saw Players 4, 6 and 7
    })
    
    
    matrix = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]]
    
    print("Here is the matrix of players who saw themselves during the game : \n")
    print(" 0  1  2  3  4  5  6  7  8  9  *")
    compteur = 0
    for l in matrix:
        print(l,compteur)
        compteur += 1
    
    
    Potential_Impostors(graph)
    
#%%
def Step3():
    import math

    nV = 14
    
    INF = math.inf
    
    # Algorithm implementation
    def floyd_warshall(G):
        distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    
        # Adding vertices individually
        for k in range(nV):
            for i in range(nV):
                for j in range(nV):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        print_solution(distance)
    
    
    # Printing the solution
    def print_solution(distance):
        a = ""
        b = ""
        for i in range(nV):
            for j in range(nV):
                if(distance[i][j] == INF):
                    print("INF", end=" ")
                else:
                    a = str(i)
                    b = str(j)
                    if a == "0":
                        a = "Reactor"
                    if b == "0":
                        b = "Reactor"
                        
                    if a == "1":
                        a = "Upper Engine"
                    if b == "1":
                        b = "Upper Engine"
                        
                    if a == "2":
                        a = "Security"
                    if b == "2":
                        b = "Security"
                        
                    if a == "3":
                        a = "Lower Engine"
                    if b == "3":
                        b = "Lower Engine"
                        
                    if a == "4":
                        a = "Medbay"
                    if b == "4":
                        b = "Medbay"
                        
                    if a == "5":
                        a = "Cafeteria"
                    if b == "5":
                        b = "Cafeteria"
                        
                    if a == "6":
                        a = "Storage"
                    if b == "6":
                        b = "Storage"
                        
                    if a == "7":
                        a = "Electrical"
                    if b == "7":
                        b = "Electrical"
                        
                    if a == "8":
                        a = "Admin"
                    if b == "8":
                        b = "Admin"
                        
                    if a == "9":
                        a = "Weapons"
                    if b == "9":
                        b = "Weapons"
                        
                    if a == "10":
                        a = "O²"
                    if b == "10":
                        b = "O²"
    
                    if a == "11":
                        a = "Navigation"
                    if b == "11":
                        b = "Navigation"
                        
                    if a == "12":
                        a = "Shields"
                    if b == "12":
                        b = "Shields"
                        
                    if a == "13":
                        a = "Communication"
                    if b == "13":
                        b = "Communication"
    
    
                    # print(distance[i][j], end="  ")
                    print("Start = {} | Stop = {} | Time = {}".format(a,b,distance[i][j]),end="\n")
                    
            
            
            print(" ")
    
    
    
    Crewmate_Graph = [[0, 6, 5, 6, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],   # Reactor 1        
    [6, 0, 6, INF, 7, 9, INF, INF, INF, INF, INF, INF, INF, INF],                       # Upper Engine 2                               
    [5, 6, 0, 6, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],                     # Security 3                                 
    [6, INF, 6, 0, INF, INF, 10, 8, INF, INF, INF, INF, INF, INF],                      # Lower Engine 4                                
    [INF, 7, INF, INF, 0, 6, INF, INF, INF, INF, INF, INF, INF, INF],                   # Medbay 5               
    [INF, 9, INF, INF, 6, 0, 8, INF, 6, 5, INF, INF, INF, INF],                         # Cafeteria 6                             
    [INF, INF, INF, 10, INF, 8, 0, 7, 6, INF, INF, INF, 5, 4],                          # Storage 7       
    [INF, INF, INF, 8, INF, INF, 7, 0, INF, INF, INF, INF, INF, INF],                   # Electrical 8              
    [INF, INF, INF, INF, INF, 6, 6, INF, 0, INF, INF, INF, INF, INF],                   # Admin 9              
    [INF, INF, INF, INF, INF, 5, INF, INF, INF, 0, 4, 7, 7, INF],                       # Weapons 10         
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, 0, 7, 9, INF],                     # O² 11           
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 7, 7, 0, 8, INF],                     # Navigation 12           
    [INF, INF, INF, INF, INF, INF, 5, INF, INF, 7, 9, 8, 0, 3],                         # Shields 13        
    [INF, INF, INF, INF, INF, INF, 4, INF, INF, INF, INF, INF, 3, 0]]                   # Communication 14             
    
    Impostor_Graph = [[0, 0, 5, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],   # Reactor 1
    [0, 0, 6, INF, 7, 9, INF, INF, INF, INF, INF, INF, INF, INF],                       # Upper Engine 2
    [5, 6, 0, 6, 0, INF, INF, 0, INF, INF, INF, INF, INF, INF],                         # Security 3
    [0, INF, 6, 0, INF, INF, 10, 8, INF, INF, INF, INF, INF, INF],                      # Lower Engine 4
    [INF, 7, 0, INF, 0, 6, INF, 0, INF, INF, INF, INF, INF, INF],                       # Medbay 5 
    [INF, 9, INF, INF, 6, 0, 8, INF, 0, 5, 4, 4, INF, INF],                             # Cafeteria 6
    [INF, INF, INF, 10, INF, 8, 0, 7, 6, INF, INF, INF, 5, 4],                          # Storage 7
    [INF, INF, 0, 8, 0, INF, 7, 0, INF, INF, INF, INF, INF, INF],                       # Electrical 8
    [INF, INF, INF, INF, INF, 0, 6, INF, 0, INF, INF, INF, INF, INF],                   # Admin 9
    [INF, INF, INF, INF, INF, 5, INF, INF, INF, 0, 4, 0, 7, INF],                       # Weapons 10
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, 0, 7, 9, INF],                     # O² 11
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 7, 0, 0, INF],                     # Navigation 12
    [INF, INF, INF, INF, INF, INF, 5, INF, INF, 7, 9, 0, 0, 3],                         # Shields 13 
    [INF, INF, INF, INF, INF, INF, 4, INF, INF, INF, INF, INF, 3, 0]]                   # Communication 14
    
    
        
    while True:
        try:
            number = int(input("Do you want to check time as a Crewmate (1) ? Or an Impostor (2) ? : "))
            if 1 <= number <= 2:
                if number == 1:
                    print("Here are the different times it takes to travel between rooms as a Crewmate :\n")
                    floyd_warshall(Crewmate_Graph)
                if number == 2:
                    print("Here are the different times it takes to travel between rooms as an Impostor :\n")
                    floyd_warshall(Impostor_Graph)
                break
            raise ValueError()
        except ValueError:
            print("Please select a valid Step (number between 1 and 4)\n")

#%%
def Step4():
    class Graph:
    
        # Constructor
        def __init__(self, edges, N):
            # Adjacency List in a list of list (matrix)
            self.adjList = [[] for _ in range(N)]
    
            # We add the edges in the graph
            for (src, dest) in edges:
                self.adjList[src].append(dest)
                self.adjList[dest].append(src)
    
    
    def printAllHamiltonianPaths(g, v, visited, path, N):
        # If len(path) == number of vertices, then all the vertices have been visited, then Hamiltonian Path exists
        if len(path) == N:
    #         print("Hamiltonian path exists")
            return
        # We check if every edge starting from a certain v vertex give us a solution or not
        for w in g.adjList[v]:
            # process only unvisited vertices as hamiltonian
            # path visits each vertex exactly once
            if not visited[w]:
                visited[w] = True
                path.append(w)
    
                # check if adding vertex w to the path leads to solution or not
                printAllHamiltonianPaths(g, w, visited, path, N)
    
                # Backtrack
                visited[w] = False
                if len(path)==14:
                    for index, item in enumerate(path):
                        if item == 0:
                            path[index] = "Reactor"
                        if item == 1:
                            path[index] = "Upper Engine"
                        if item == 2:
                            path[index] = "Security"
                        if item == 3:
                            path[index] = "Lower Engine"
                        if item == 4:
                            path[index] = "Medbay"
                        if item == 5:
                            path[index] = "Cafeteria"
                        if item == 6:
                            path[index] = "Storage"
                        if item == 7:
                            path[index] = "Electrical"
                        if item == 8:
                            path[index] = "Admin"
                        if item == 9:
                            path[index] = "Weapons"
                        if item == 10:
                            path[index] = "O²"
                        if item == 11:
                            path[index] = "Navigation"
                        if item == 12:
                            path[index] = "Shields"
                        if item == 13:
                            path[index] = "Communication"
                    print(path)
                    print("\n")
                path.pop()
    
    
    
    # List of graph edges as per above diagram
    edges = [(0,1),(0,2),(0,3),
             (1,2),(1,4),(1,5),
             (3,2),
             (4,5),
             (5,6),(5,8),(5,9),
             (6,8),(6,7),(6,3),
             (7,3), 
             (9,10),(9,12),(9,11),
             (10,12),(10,11),
             (11,12),
             (12,13),(12,6),
             (13,6)]
    
    # Reactor 0       
    # Upper Engine 1   
    # Security 2       
    # Lower Engine 3   
    # Medbay 4         
    # Cafeteria 5      
    # Storage 6       
    # Electrical 7     
    # Admin 8          
    # Weapons 9       
    # O² 10           
    # Navigation 11    
    # Shields 12       
    # Communication 13 
    
    # Number of Vertices
    N = 14
    
    # Creation of the Graph
    g = Graph(edges, N)
    
    
    
    def Starting_Room_Choice(): 
        while True:
            try:
                print("Here are the different rooms, choose one to start with :\n")
                print("\nThe room that can start a Hamiltonian Path are 4,7,8,9,10,11,13. Otherwise it won't be possible to start a Hamiltonian Path.")
                print("|Reactor : 0|")
                print("|Upper Engine : 1|")
                print("|Security : 2|")
                print("|Lower Engine : 3|")
                print("|Medbay : 4|")
                print("|Cafeteria : 5|")
                print("|Storage : 6|")
                print("|Electrical : 7|")
                print("|Admin : 8|")
                print("|Weapons : 9|")
                print("|O² : 10|")
                print("|Navigation : 11|")
                print("|Shields : 12|")
                print("|Communication : 13|")
                number = int(input("Enter a valid room (number between 1 and 14): "))
                if 0 <= number <= 13:
                    if number == 0:
                        room = "Reactor"
                    if number == 1:
                        room = "Upper Engine"
                    if number == 2:
                        room = "Security"
                    if number == 3:
                        room = "Lower Engine"
                    if number == 4:
                        room = "Medbay"
                    if number == 5:
                        room = "Cafeteria"
                    if number == 6:
                        room = "Storage"
                    if number == 7:
                        room = "Electrical"
                    if number == 8:
                        room = "Admin"
                    if number == 9:
                        room = "Weapons"
                    if number == 10:
                        room = "O²"
                    if number == 11:
                        room = "Navigation"
                    if number == 12:
                        room = "Shields"
                    if number == 13:
                        room = "Communication"
                    break
                raise ValueError()
            except ValueError:
                print("Enter a valid room (number between 1 and 14): ")
        return number,room
    
    number , room = Starting_Room_Choice()
    start = number        
            
    # add starting node to the path
    path = [start]
    
    # mark start node as visited
    visited = [False] * N
    visited[start] = True
    
    
    def Display_Paths():
        if start in [0,1,2,3,5,6,12]:
            print("It is not possible to visit every room without passing two times in the same room by starting in this room. You should select another one.")
        else:
            print("\nHere are the different Hamiltonian Paths possible, starting from {} : \n".format(room))
            printAllHamiltonianPaths(g, start, visited, path, N)
    Display_Paths()
    
#%% 
if __name__ == "__main__":
    while True:
        try:
            number = int(input("Select the step you want to run : "))
            if 1 <= number <= 4:
                if number == 1:
                    Step1()
                if number == 2:
                    Step2()
                if number == 3:
                    Step3()
                if number == 4:
                    Step4()
                break
            raise ValueError()
        except ValueError:
            print("Please select a valid Step (number between 1 and 4)\n")