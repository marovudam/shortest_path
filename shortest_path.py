import argparse
import os
import json

def parse_arguments() -> dict :
    parser = argparse.ArgumentParser(
        description="Find shortest way from article_1" + \
            " to article_2 if they are present in JSON"
    )
    parser.add_argument('-f', '--from', default="Harry Potter", \
        help='Starting Wikipedia page')
    parser.add_argument('--to', default="Harry Potter", \
        help='End point to search')
    parser.add_argument('-v', help='Print the full path', action='store_true')
    parser.add_argument('--non-directed', \
        help='Ignore the direction of paths', action='store_true')
    return dict(parser.parse_args()._get_kwargs())

def recurs(path, database, is_directed, p_to, lst_paths):
    filtered_connections = list(
        filter(
                lambda x: ((x[0] == path[-1] and x[1] not in path) if (is_directed is None or is_directed == False) else ((x[0] == path[-1] and x[1] not in path) or (x[1] == path[-1] and x[0] not in path))), database['edges']
        )
    )
    if len(path) < 1000:
        for connection in filtered_connections:
            copy_lst = path.copy()
            if connection[0] == copy_lst[-1]:
                copy_lst.append(connection[1])
            elif connection[1] == copy_lst[-1]:
                copy_lst.append(connection[0])
            else:
                return
            if copy_lst[-1] == p_to:
                lst_paths.append(copy_lst)
                return
            else:
                recurs(copy_lst, database, is_directed, p_to, lst_paths)

def find_way(database: dict, p_from: str, p_to: str, is_directed=False, lst_paths = []):
    path = [p_from]
    recurs(path, database, is_directed, p_to, lst_paths)
    

def print_shortest(lst_paths):
    shortest_path = list(
        filter(
            lambda x: len(x) == min(map(lambda x: len(x), lst_paths)),
            lst_paths
        )
    )
    if len(shortest_path) > 0:
        shortest_path = shortest_path[0]
        print(*shortest_path, sep=' -> ')

def find_shortest_way(arguments: dict) -> None:
    # os.environ['GRAPH_FILE'] = "full filepath"
    os.environ['GRAPH_FILE'] = "wiki.json"
    try:
        with open(os.environ['GRAPH_FILE'], "r") as f:
            database = json.load(f)
            lst_paths = []
            if args['from'] in database['vertices'] and args['to'] in database['vertices']:
                if args['from'] == args['to']:
                    lst_paths += [[args['to']]]
                elif args['non_directed'] is None:
                    find_way(database, args['from'], args['to'], lst_paths=lst_paths)
                else:
                    find_way(database, args['from'], args['to'], True, lst_paths)
                if arguments['v'] is not None:
                    print_shortest(lst_paths)
                if len(lst_paths) > 0:
                    print(min(map(lambda x: len(x), lst_paths)))
                else:
                    print(0)
            else:
                print("There is no start or end point (according to database data)")
    except:
        print("Database not found")

if __name__ == "__main__":
    args = parse_arguments()
    find_shortest_way(args)