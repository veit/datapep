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
> uv sync --frozen
```

## Aktualisierung der Abhängigkeiten

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
>>> from dataprep import importer
>>> importer.customers
                    name  ...       user_name
0      Patricia Schaefer  ...       ndavidson
1          Olivie Dubois  ...     manonallain
2       Mary Davies-Kirk  ...  colemanmichael
3     Miroslawa Eckbauer  ...     romanjunitz
4          Richard Bauer  ...          adam78
...                  ...  ...             ...
2075        Maurice Stey  ...        dkreusel
2076     Linda Alexander  ...     kennethrchn
2077        Diane Bailly  ...      dorothee41
2078   Jorge Riba Cerdán  ...       eugenia17
2079       Ryan Thompson  ...         cnewton

[2080 rows x 8 columns]
```
