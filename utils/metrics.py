import networkit as nk
import networkx as nx

def list_to_dict_user(list_measure, idmap):
  dict_measure = {}
  for u in idmap.keys():
    dict_measure[u] = list_measure[idmap[u]]
  return dict_measure

def compute_reputation(full_graph):
  full_in_degree = full_graph.in_degree
  full_out_degree = full_graph.out_degree
  reputation = {}
  for node in full_graph.nodes().keys():
    reputation[node]=full_in_degree[node]/(full_in_degree[node]+full_out_degree[node])
  return reputation


def degree_centrality(graph, graph_nk, idmap):
    return list_to_dict_user(nk.centrality.DegreeCentrality(graph_nk, normalized=True).run().scores(), idmap)

def eigenvector_centrality(graph, graph_nk, idmap):
    return list_to_dict_user(nk.centrality.EigenvectorCentrality(graph_nk).run().scores(), idmap)

def katz_centrality(graph, graph_nk, idmap):
    return list_to_dict_user(nk.centrality.KatzCentrality(graph_nk, 0.001, 1e-4).run().scores(), idmap)

def closeness_centrality(graph, graph_nk, idmap):
    return list_to_dict_user(nk.centrality.Closeness(graph_nk, False, nk.centrality.ClosenessVariant.GENERALIZED).run().scores(), idmap)

def betweenness_centrality(graph, graph_nk, idmap):
    return list_to_dict_user(nk.centrality.Betweenness(graph_nk).run().scores(), idmap)

def clustering_coefficients(graph, graph_nk, idmap):
    return nx.clustering(graph)

def hits_scores(graph, graph_nk, idmap):
    return nx.hits(graph)

def reputation_score(graph, graph_nk, idmap):
    return compute_reputation(graph)