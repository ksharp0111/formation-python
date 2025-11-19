import collector
import json

data = collector.collect_cpu()
print("CPU data: ", data)

tout = collector.collect_all()

print(json.dumps(tout, indent=2, default=str))