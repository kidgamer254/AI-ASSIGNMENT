def is_safe(node, color, assignment, graph):
    for neighbor in graph.get(node, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(nodes, colors, assignment, graph):
    if len(assignment) == len(nodes):
        return assignment

    unassigned_nodes = [n for n in nodes if n not in assignment]
    node = unassigned_nodes[0]

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(nodes, colors, assignment, graph)
            if result is not None:
                return result
            del assignment[node]
    return None

def find_chromatic_number(nodes, graph):
    """Find the least possible number of colors required."""
    max_colors = len(nodes)
    for num_colors in range(1, max_colors + 1):
        colors = [f"Color_{i+1}" for i in range(num_colors)]
        solution = backtrack(nodes, colors, {}, graph)
        if solution:
            return num_colors, solution
    return None, None

def main():
    print("--- Task Two (b): Nairobi Sub-counties Coloring ---")
    
    # 1. Define the 17 sub-counties
    sub_counties = [
        "Westlands", "Dagoretti North", "Dagoretti South", "Lang'ata", "Kibra",
        "Roysambu", "Kasarani", "Ruaraka", "Embakasi South", "Embakasi North",
        "Embakasi Central", "Embakasi East", "Embakasi West", "Makadara",
        "Kamukunji", "Starehe", "Mathare"
    ]
    
    # 2. Define the adjacency graph (Simulative based on Nairobi Geography)
    graph = {
        "Westlands": ["Dagoretti North", "Kibra", "Lang'ata", "Starehe", "Roysambu"],
        "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra"],
        "Dagoretti South": ["Dagoretti North", "Lang'ata"],
        "Kibra": ["Westlands", "Dagoretti North", "Lang'ata", "Starehe"],
        "Lang'ata": ["Westlands", "Dagoretti South", "Kibra", "Starehe", "Embakasi South"],
        "Starehe": ["Westlands", "Kibra", "Lang'ata", "Kamukunji", "Mathare", "Makadara"],
        "Mathare": ["Starehe", "Kamukunji", "Ruaraka"],
        "Kamukunji": ["Starehe", "Mathare", "Makadara", "Embakasi West"],
        "Makadara": ["Starehe", "Kamukunji", "Embakasi West", "Embakasi South"],
        "Ruaraka": ["Mathare", "Roysambu", "Kasarani", "Embakasi North"],
        "Roysambu": ["Westlands", "Ruaraka", "Kasarani"],
        "Kasarani": ["Roysambu", "Ruaraka", "Embakasi North", "Embakasi East"],
        "Embakasi North": ["Ruaraka", "Kasarani", "Embakasi Central", "Embakasi West"],
        "Embakasi Central": ["Embakasi North", "Embakasi West", "Embakasi East"],
        "Embakasi West": ["Kamukunji", "Makadara", "Embakasi North", "Embakasi Central", "Embakasi South"],
        "Embakasi South": ["Lang'ata", "Makadara", "Embakasi West", "Embakasi East"],
        "Embakasi East": ["Kasarani", "Embakasi Central", "Embakasi South"]
    }
    
    # 3. Find minimum colors
    chromatic_num, solution = find_chromatic_number(sub_counties, graph)
    
    if solution:
        print(f"Minimum colors required: {chromatic_num}")
        print("\nSolution:")
        # Group by color for better readability
        color_groups = {}
        for region, color in solution.items():
            if color not in color_groups:
                color_groups[color] = []
            color_groups[color].append(region)
            
        for color, regions in color_groups.items():
            print(f"{color}: {', '.join(regions)}")
    else:
        print("Could not find a coloring solution.")

if __name__ == "__main__":
    main()
