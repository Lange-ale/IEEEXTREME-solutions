//this approach takes 44.44/100 points

#include <bits/stdc++.h>
using namespace std;

long long dfs(const unordered_map<int, unordered_set<int>>& edges, const unordered_map<int, int>& weights, int part, int dest, int prec) {
    if (part == dest)
        return weights.at(part);

    long long weight_path = 1;
    if (edges.at(part).find(dest) != edges.at(part).end())
        return dfs(edges, weights, dest, dest, part) * weights.at(part) % 1000000007;
    for (auto& edge : edges.at(part))
        if (edge != prec) {
            weight_path *= dfs(edges, weights, edge, dest, part) % 1000000007;
            if (weight_path != 1)
                return weight_path * weights.at(part) % 1000000007;
        }

    return weight_path;
}

int main() {
    int T, N, Q, u, v, op, temp;
    cin >> T;
    while (T--) {
        cin >> N;
        unordered_map<int, unordered_set<int>> edges;
        unordered_map<int, int> weights;
        for (int i = 1; i <= N; i++)
            cin >> weights[i];
        for (int i = 1; i < N; ++i) {
            cin >> u >> v;
            edges[u].insert(v);
            edges[v].insert(u);
        }
        cin >> Q;
        while (Q--) {
            cin >> op >> u >> v;
            if (op == 1) {
                weights[u] = v;
            } else {
                cout << dfs(edges, weights, u, v, u) << endl;
            }
        }
    }
}