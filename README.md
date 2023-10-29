# shortest_path

_There is a [TODO](TODO.md) to this project_

How to find a shortest path in graph?

This is a part of the group project implemented within 24 hours on Python for Beginners Intensive Course. That specific part took me around 4 hours. The program ended up working pretty slow, some fixing is planned.

## Project description

Graph is parsed from JSON file with a specific format. File location is specified in `GRAPH_FILE` variable.

Script options:

+ `-h, --help` Show help message, list of options and exit
+ `-f FROM, --from FROM` Starting node
+ `--to TO`               End point to search
+ `-v`                    Print the full path
+ `--non-directed`        Ignore the direction of paths

By default, script prints the length of the shortes path from node "Programming language" to node "PAQ", concidering the directions of graph paths.

File that stores graph must have format as shown:
```
{
    "vertices" : [
        "List",
        "of",
        "all",
        "vertices",
        "in graph"
    ],
    "edges": [
        [
            "List",
            "of"
        ],
        [
            "of",
            "all"
        ]
        ...  # and so on
    ]
}
```

The example of such [file is present in repository](graph.json).

**The vertice not included in vertices list but present in edge connection will not be used in search.**