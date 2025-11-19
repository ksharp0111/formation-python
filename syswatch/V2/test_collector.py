import collector
import json

data = collector.collector_cpu()
print("CPU data: ", data)

tout = collector.collecter_tout()

print(json.dumps(tout, indent=2, default=str))