def dijkstra(map_, start):
    # 2차원 Dictionary 로 구성된 map_ 탐색
    # e.g.) map_[start][dest] = dist
    definedNodes = {start:0}
    cands = {start:0}
    loc = start
    while True:
        del cands[loc]
        for d in map_[loc]:
            if d not in definedNodes:
                if d in cands:
                    cands[d] = min(cands[d], map_[loc][d]+definedNodes[loc])
                else:
                    cands[d] = map_[loc][d]+definedNodes[loc]
        if not cands:
            break
        minkey = min(cands, key=cands.get)
        definedNodes[minkey] = cands[minkey]
        loc = minkey
            
    return definedNodes