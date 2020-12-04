from kubernetes import client, config
import sys

namespace = 'default'
if len(sys.argv) > 1:
    namespace = sys.argv[1]

config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs in %s namespace" % (namespace))
pods = v1.list_namespaced_pod(namespace=namespace)
for i in pods.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

print("\nListing servicesin %s namespace" % (namespace))
services = v1.list_namespaced_service(namespace=namespace)
for i in services.items:
    print("%s\t%s" % (i.metadata.namespace, i.metadata.name))