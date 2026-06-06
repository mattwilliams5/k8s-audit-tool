from audit import (
    get_cluster_names,
    get_large_clusters,
    total_nodes,
    count_services,
    find_unhealthy_services,
    load_clusters,
)

clusters = [
    {
        "name": "prod-east",
        "nodes": 25,
        "services": [
            {"name": "vault", "status": "running"},
            {"name": "consul", "status": "running"},
        ],
    },
    {
        "name": "prod-west",
        "nodes": 18,
        "services": [
            {"name": "vault", "status": "stopped"},
        ],
    },
    {
        "name": "dev",
        "nodes": 3,
        "services": [],
    },
]


def test_get_cluster_names():
    assert get_cluster_names(clusters) == ['prod-east', 'prod-west', 'dev']

def test_get_large_clusters():
    assert get_large_clusters(clusters) == ['prod-east', 'prod-west']

def test_total_nodes():
    assert total_nodes(clusters) == 46

def test_count_services():
    assert count_services(clusters) == 3

def test_find_unhealthy_services():
    assert find_unhealthy_services(clusters) == [('prod-west', 'vault')]

def test_load_clusters():
    clusters = load_clusters("clusters.json")
    assert len(clusters) == 2