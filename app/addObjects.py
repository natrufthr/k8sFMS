from kubernetes import client, config, utils

config_file_location = '/app/data/config.yaml'

config.load_kube_config(config_file=config_file_location)

cOa = client.CustomObjectsApi()

v1 = client.CoreV1Api()

k8s_client = client.ApiClient()

def createSpoke(hubName, airLineName, airportName):
    crd_spec = {
        'apiVersion': 'example.air.com/v1',
        'kind': 'Spoke',
        'metadata': {
            'name': airportName,
            'namespace': 'default'
        },
        'spec': {
            'hubName': hubName,
            'airLineName': airLineName
        }
    }
    cOa.create_namespaced_custom_object(body=crd_spec, namespace='default', group="example.air.com", version="v1", plural="spokes")

def createAirLine(airLineName):
    crd_spec = {
        'apiVersion': 'example.air.com/v1',
        'kind': 'Airline',
        'metadata': {
            'name': airLineName,
            'namespace': 'default'
        },
        'spec': {
            'foo': 'bar',
            'baz': 'qux'
        }
    }
    cOa.create_namespaced_custom_object(body=crd_spec, namespace='default', group="example.air.com", version="v1", plural="airlines")

def createHub(hubName,airLineName):
    crd_spec = {
        'apiVersion': 'example.air.com/v1',
        'kind': 'Hub',
        'metadata': {
            'name': hubName,
        },
        'spec': {
            'airLineName': airLineName
        }
    }
    cOa.create_namespaced_custom_object(body=crd_spec, namespace='default', group="example.air.com", version="v1", plural="hubs")

def createFlight(flightName, going, leaving, airLineName):
    crd_spec = {
        'apiVersion': 'example.air.com/v1',
        'kind': 'Flight',
        'metadata': {
            'name': flightName,
        },
        'spec': {
            'going': going,
            'leaving': leaving,
            'airLineName': airLineName
        }
    }
    cOa.create_namespaced_custom_object(body=crd_spec, namespace='default', group="example.air.com", version="v1", plural="flights")
# yaml_file = '<location to your multi-resource file>'
# utils.create_from_yaml(k8s_client, yaml_file)

# createAirLine("airlinetwo")

# createSpoke("hubtwo", "airline-name", "spokethree")