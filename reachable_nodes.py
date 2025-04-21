def reachable_nodes_func(adj_list, start_node, reachable_nodes):
    if start_node not in reachable_nodes:
        reachable_nodes.append(start_node)
        for i in adj_list[start_node]:
            reachable_nodes_func(adj_list, i, reachable_nodes)
    else:
        return

def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    reachable_nodes = []
    if (len(adj_list[start_node]) == 0):
        return ()

    for i in adj_list[start_node]:
        reachable_nodes_func(adj_list, i, reachable_nodes)
    return set(reachable_nodes)

def main():
    adj_list = [[1, 3], [2], [0], [4], [3], []]

    print(reachable(adj_list, 0))

if __name__ == "__main__":
    main()