import re
import io

_authors_ = "Md Rezaur Rahman"
_copyright_ = "Copyright 2020, The Human Motion Synthesis Project"
_version_ = "0.1"
_maintainer_ = "Reza, Matthias"
_status_ = "Dev"

class LTLGraphCreation():
    def __init__(self, file_data):
        buf = io.StringIO(file_data)
        self.graph = {} # Stores all node-edge information from the ltl graph
        self.graph_center = None
        self.parsing_buffer(buf)
        self.trv_ftime = None
        self.dead_nodes = []
          
    def parsing_buffer(self, buf):
        self.lines = buf.readlines()
        for line in lines:
            if (("->" in line) and ("[label=<" in line)): # Contain edge info between nodes
                pattern = "<(.*?)>"
                edges = re.search(pattern, line).group(1)
                edges = edges.replace("&amp;", "&")
                nodes = list(map(int, re.findall(r'\d+', line)))
                print("Nodes: ", nodes)
                print("Edge: ", edges)
                self.store_graph_info(nodes, edges)

            elif ("peripheries" in line):
                self.graph_center = int(re.search(r'\d+', line).group()) # Only take the first node info
    
    def store_graph_info(self, nodes, edges):
        # Source node is empty
        if self.graph.get(nodes[0]) == None:
            temp = {}
            temp["incoming"] = []
            temp["outgoing"] = []
            self.graph[nodes[0]] = temp
        
        # Destination node is empty but source node already exists 
        if self.graph.get(nodes[1]) == None:
            temp = {}
            temp["incoming"] = []
            temp["outgoing"] = []
            self.graph[nodes[1]] = temp
        
        self.graph.get(nodes[0])["outgoing"].append(nodes[1])
        self.graph.get(nodes[1])["incoming"].append(nodes[0])
    
    def graph_print(self):
        print(self.graph)
        print("No. of Vertices : ", len(self.graph.keys()))
        print("The Graph center: ", self.graph_center)
    
    def check_dead_nodes(self):
        for k in self.graph.keys():
            sz = len(self.graph[k]["outgoing"])
            if ((sz == 1) and (self.graph[k]["outgoing"][0] == k)):
                self.dead_nodes.append(k)
        
        if (len(self.dead_nodes) > 0):
            print("Dead nodes exist in the Graph.\nDead nodes are: ")
            for i in self.dead_nodes:
                print(i)
    
    def is_dead(self, u):
        for i in self.dead_nodes:
            if u == i:
                return True
        return False
        
    def print_all_paths(self, src):
        sz = len(self.graph.keys())
        visited = [False for _ in range(sz)]
        path = [] # List to store paths
        # self.trv_ftime = True
        self.recurse_pathfinder(src, visited, path)
    
    def recurse_pathfinder(self, u, visited, path):
        # Mark the current node
        visited[u] = True
        path.append(u)
        
        # if u == d and self.trv_ftime == False:
        #    print("Path: ", path)
            
        # Check in terms of dead nodes, If found then return back to start node.
        if self.is_dead(u):
            print("Enter into dead Node ", u)
            path.append(0)
            print("The updated path is : ", path)
        
        else:
            # self.trv_ftime = False
            edges = self.graph[u]["outgoing"]
            # print("edges --> ", edges)
            for e in edges:
                if visited[e] == False:
                    self.recurse_pathfinder(e, visited, path)
        
        # Remove current node from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
        
