# Py-TzKT

Wrapper [TzKT API](https://api.tzkt.io/) on Python 3

## Installation

```bash
pip install pytzkt
```

## Examples
```python
from pytzkt import TzKT

tzkt = TzKT()

head = tzkt.get_head()
account = tzkt.get_account('<address>')
```