## Graph Parser for LTL formulation
LTL Graph parser takes a **.dot** file as an input, parse it and creates a Graph with node-edge information.

### API Reference
class **LTLGraphCreation** contain following APIs.
  - **parsing_buffer()**
    - This method takes the **.dot** file as string and creates the graph object. Internally a callback method is invoked to store the node and edge information in a dictionary object. 
    
  - **graph_print()**
    - Print the full graph information with edges and nodes.
    
  - **get_action(src, dst)**
    - Returns a list of actions taken from a source vertex to the destination vertex in the LTL formaulation.
    
  - **check_dead_nodes()**
    - Print all the dead nodes (if present any) in the formulated graph. 
  
  - **is_dead()**
    - Check whether a vertex/node is in a dead state, i.e., no other vertex/state can be reachable from this vertex/node.
 
  - **recurse_traversal()**
    - It prints the path of length p_len (default: 20) and the corresponding actions taken along the edges from a starting vertex. While traversing the graph, it avoids the dead vertex and randomly choose the next valid vertex with an action.  

  - **self.graph**
    - This class variable holds all the node and edge information of the ltl graph.
