# Implementing monitoring in minikube + Grafana Dashboard As a Code

## Monitoring
### Prerequesits
-   Install minikube & kubectl
-   python & pip
-   grafanalib (pip module)

### Deploy Monitoring
-   Use [monitoring-deploy.yml](/monitoring-deploy.yml) to deploy Prometheus, Node Exporter, Kube-State Metrics, Grafana.
    -   Additionally this file contain RBAC inorder to give necessary permissions to kube-state-metrics to scrate data from the node & send it to prometheus.

### Grafana Dashboard As a Code - GDAC
-   Using "grafanalib" we are creating a dashboard in Grafana.
-   For testign I took "busybox" docker image
    - ```kubectl run busybox-crash --image=busybox -- /bin/sh -c "exit 1"```
    - This will creates a container that will always crashes.
-   Use [gflib.py](/gflib.py) to create  a JSON file.
-   Use the following command to push the JSON file to Grafana
    - ```curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <Grafana API Token>" -d @kubernetes_pod_restarts_dashboard_for_api.json <Dashboard Url>/api/dashboards/db```

#### Generate Grafana API Token

-   Grafana UI  > Configuration > API Keys > Generate New Token


![](/dac.png)