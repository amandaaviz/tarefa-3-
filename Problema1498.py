#include <bits/stdc++.h>
using namespace std;

struct Node {
    int depth;
    long long weight;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    while (cin >> N) {
        vector<Node> nodes;

        for (int i = 0; i < N; i++) {
            int L;
            cin >> L;
            nodes.push_back({L, 1});
        }

        while ((int)nodes.size() > 1) {
            int maxDepth = -1;

            for (auto &x : nodes) {
                maxDepth = max(maxDepth, x.depth);
            }

            int p1 = -1, p2 = -1;

            for (int i = 0; i < (int)nodes.size(); i++) {
                if (nodes[i].depth == maxDepth) {
                    if (p1 == -1 || nodes[i].weight < nodes[p1].weight) {
                        p2 = p1;
                        p1 = i;
                    } else if (p2 == -1 || nodes[i].weight < nodes[p2].weight) {
                        p2 = i;
                    }
                }
            }

            if (p1 > p2)
                swap(p1, p2);

            long long w1 = nodes[p1].weight;
            long long w2 = nodes[p2].weight;

            long long limite = max(w1, w2);

            Node novo;
            novo.depth = maxDepth - 1;
            novo.weight = w1 + w2;

            nodes.erase(nodes.begin() + p2);
            nodes.erase(nodes.begin() + p1);

            for (auto &x : nodes) {
                if (x.weight < limite)
                    x.weight = limite;
            }

            nodes.push_back(novo);
        }

        cout << nodes[0].weight << "\n";
    }

    return 0;
}
