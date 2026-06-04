'''
  Audit.py calls the following functions
  get_cluster_names()
  get_large_clusters()
  total_nodes()
  count_services()
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
