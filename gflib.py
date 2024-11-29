import json  # Import JSON module for conversion
from grafanalib.core import (
    Dashboard, Graph, Row, Target, Time, YAxes, YAxis, GridPos
)

# Define the dashboard
dashboard = Dashboard(
    title="Kubernetes Busybox Pod Restarts Dashboard",
    rows=[
        Row(
            panels=[
                Graph(
                    title="Pod Container Restarts",
                    dataSource="Prometheus",  # Adjust to match your Grafana data source name
                    targets=[
                        Target(
                            expr='kube_pod_container_status_restarts_total{namespace="default"}',
                            legendFormat="{{pod}} - {{container}}",  # Customize labels to show pod and container names
                            refId="A",
                        ),
                    ],
                    gridPos=GridPos(h=8, w=24, x=0, y=0),  # Panel position and size
                    yAxes=YAxes(
                        left=YAxis(format="short", label="Restarts"),  # Display restart counts on the left Y-axis
                        right=YAxis(format="short"),
                    ),
                ),
            ]
        )
    ],
    time=Time("now-1h", "now"),  # Default time range
)

# Custom JSON serializer for non-serializable objects
def custom_serializer(obj):
    if hasattr(obj, "to_json_data"):
        return obj.to_json_data()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

# Prepare the correct JSON structure for Grafana API
dashboard_json = {
    "dashboard": dashboard.to_json_data(),
    "folderId": 0,
    "overwrite": True
}

# Save the properly formatted JSON to a file
with open("kubernetes_pod_restarts_dashboard_for_api.json", "w") as f:
    json.dump(dashboard_json, f, indent=2, default=custom_serializer)
