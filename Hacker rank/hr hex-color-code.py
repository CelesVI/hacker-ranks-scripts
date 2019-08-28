import re

result = list(re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})', input()))

print(result)
