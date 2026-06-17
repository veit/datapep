# dataprep-Paket

Das Paket wurde erstellt mit
```console
uv init --package dataprep
```

Falls `uv` bei Ihnen noch nicht installiert ist, können sie es unter Windows installieren mit

```console
> powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installation

```console
> cd dataprep
> uv sync
```

## Nutzung

### auf der Konsole:

```console
> uv run dataprep
Hello from dataprep!
```

### in Python
```console
> uv run python
```
```python
import dataprep
dataprep.main()
```
