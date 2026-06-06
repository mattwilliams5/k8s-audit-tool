import json

'''
  Audit.py calls the following functions
  get_cluster_names()
  get_large_clusters()
  total_nodes()
  count_services()
  find_unhealthy_services()
'''
clusters = [
    {
        "name": "prod-east",
        "nodes": 25,
        "services": [
            {"name": "vault", "status": "running"},
            {"name": "consul", "status": "running"}
        ]
    },
    {
        "name": "prod-west",
        "nodes": 18,
        "services": [
            {"name": "vault", "status": "stopped"}
        ]
    }
]

def get_cluster_names(clusters):
    result = []

    for cluster in clusters:
        result.append(cluster['name'])
    return result


def get_large_clusters(clusters):
    result = []

    for cluster in clusters:
        if cluster['nodes'] > 10:
            result.append(cluster['name'])
    return result

def total_nodes(clusters):
    total = 0

    for cluster in clusters:
        total += cluster["nodes"]
    return total

def count_services(clusters):
    count = 0

    for cluster in clusters:
        for service in cluster['services']:
            count += 1

    return count

def find_unhealthy_services(clusters):
    result = []
    
    for cluster in clusters:
        for service in cluster['services']:
            if service['status'] == 'stopped':
                result.append((cluster["name"],
                service["name"]
                ))
    return result

def generate_report(clusters):
    cluster_count = len(clusters)
    node_count = total_nodes(clusters)
    service_count = count_services(clusters)
    large_clusters = get_large_clusters(clusters)
    unhealthy_services = find_unhealthy_services(clusters)

    return f"""Cluster Audit Report
    ====================

    Clusters: {cluster_count}
    Total Nodes: {node_count}
    Total Services: {service_count}
    """

def load_clusters(filename):
    with open(filename) as file:
        clusters = json.load(file)
        return clusters