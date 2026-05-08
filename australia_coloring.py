def is_safe(node, color, assignment, graph):
    """Check if the color assignment is safe for the current node."""
    for neighbor in graph.get(node, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(nodes, colors, assignment, graph):
    """Recursive backtracking algorithm to find a valid coloring."""
    if len(assignment) == len(nodes):
        return assignment

    # Select the next unassigned node
    unassigned_nodes = [n for n in nodes if n not in assignment]
    node = unassigned_nodes[0]

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(nodes, colors, assignment, graph)
            if result is not None:
                return result
            # Backtrack
            del assignment[node]
    
    return None

def main():
    print("--- Task Two (a): Australia Map Coloring ---")
    
    # 1. Define the regions (nodes)
    # WA: Western Australia, NT: Northern Territory, SA: South Australia
    # QLD: Queensland, NSW: New South Wales, VIC: Victoria, TAS: Tasmania
    regions = ["WA", "NT", "SA", "QLD", "NSW", "VIC", "TAS"]
    
    # 2. Define the colors
    colors = ["Red", "Green", "Blue"]
    
    # 3. Define the adjacency graph
    graph = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "QLD"],
        "SA": ["WA", "NT", "QLD", "NSW", "VIC"],
        "QLD": ["NT", "SA", "NSW"],
        "NSW": ["QLD", "SA", "VIC"],
        "VIC": ["SA", "NSW"],
        "TAS": [] # Island
    }
    
    # 4. Solve
    solution = backtrack(regions, colors, {}, graph)
    
    if solution:
        print("Successfully colored the map!")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found with 3 colors.")

if __name__ == "__main__":
    main()
