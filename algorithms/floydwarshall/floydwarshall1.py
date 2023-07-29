def floydwarshall(map_):
    # 경로 웨이트를 Boolean으로 설정하여 순위를 결정하는 문제의 해결법
    for search in map_:
        for target in map_:
            if search == target: 
                continue
            for dest in map_[search]:
                if search == dest or target == dest: # 도착지점과 시작지점이 같은경우 제외: 테이블이 자기 자신으로 향하는 루트가 존재할경우 불필요 
                    continue
                if map_[target][dest] == None:
                    if map_[target][search] == map_[search][dest] != None:
                        if map_[target][search] == map_[search][dest]: 
                            map_[target][dest] = map_[search][dest] 
    return map_