import heapq

def minimum_transportation_price(suppliers, consumers, costs):
    n = len(suppliers)
    m = len(consumers)
    N = n + m + 2
    S = n + m      
    T = n + m + 1  

    graph = [[] for _ in range(N)]
    inf = float('inf')

    class Edge:
        def __init__(self, to, rev, cap, cost):
            self.to = to       
            self.rev = rev     
            self.cap = cap     
            self.cost = cost    

    def add_edge(frm, to, cap, cost):
        graph[frm].append(Edge(to, len(graph[to]), cap, cost))
        graph[to].append(Edge(frm, len(graph[frm])-1, 0, -cost))

    for i in range(n):
        add_edge(S, i, suppliers[i], 0)

    for j in range(m):
        add_edge(n + j, T, consumers[j], 0)

    for i in range(n):
        for j in range(m):
            add_edge(i, n + j, float('inf'), costs[i][j])

    total_cost = 0
    h = [0] * N  
    prevv = [0] * N
    preve = [0] * N

    flow = sum(suppliers)

    while flow > 0:
        dist = [inf] * N
        dist[S] = 0
        queue = [(0, S)]

        while queue:
            d, v = heapq.heappop(queue)
            if dist[v] < d:
                continue
            for i, e in enumerate(graph[v]):
                if e.cap > 0 and dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]:
                    dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                    prevv[e.to] = v
                    preve[e.to] = i
                    heapq.heappush(queue, (dist[e.to], e.to))

        if dist[T] == inf:
            break

        for v in range(N):
            if dist[v] < inf:
                h[v] += dist[v]

        d = flow
        v = T
        while v != S:
            d = min(d, graph[prevv[v]][preve[v]].cap)
            v = prevv[v]
        flow -= d
        total_cost += d * h[T]
        v = T
        while v != S:
            e = graph[prevv[v]][preve[v]]
            e.cap -= d
            graph[v][e.rev].cap += d
            v = prevv[v]

    return total_cost
