#include <bits/stdc++.h>
using namespace std;

const long long INF = (1LL << 60);

int R, C, N;
int CSIZE;

vector<vector<int>> V, AR, AC;
vector<pair<int,int>> pontos;

vector<int> rL, rR, rLeft, rRight, rowLeaf;
vector<int> cL, cR, cLeft, cRight, colLeaf;

int idNode(int rNode, int cNode) {
    return rNode * CSIZE + cNode;
}

void buildRows(int node, int l, int r) {
    rL[node] = l;
    rR[node] = r;

    if (l == r) {
        rowLeaf[l] = node;
        return;
    }

    int m = (l + r) / 2;
    rLeft[node] = node * 2;
    rRight[node] = node * 2 + 1;

    buildRows(node * 2, l, m);
    buildRows(node * 2 + 1, m + 1, r);
}

void buildCols(int node, int l, int r) {
    cL[node] = l;
    cR[node] = r;

    if (l == r) {
        colLeaf[l] = node;
        return;
    }

    int m = (l + r) / 2;
    cLeft[node] = node * 2;
    cRight[node] = node * 2 + 1;

    buildCols(node * 2, l, m);
    buildCols(node * 2 + 1, m + 1, r);
}

void getRows(int node, int ql, int qr, vector<int>& resp) {
    if (qr < rL[node] || rR[node] < ql) return;

    if (ql <= rL[node] && rR[node] <= qr) {
        resp.push_back(node);
        return;
    }

    getRows(rLeft[node], ql, qr, resp);
    getRows(rRight[node], ql, qr, resp);
}

void getCols(int node, int ql, int qr, vector<int>& resp) {
    if (qr < cL[node] || cR[node] < ql) return;

    if (ql <= cL[node] && cR[node] <= qr) {
        resp.push_back(node);
        return;
    }

    getCols(cLeft[node], ql, qr, resp);
    getCols(cRight[node], ql, qr, resp);
}

long long dijkstra(pair<int,int> origem, pair<int,int> destino) {
    int totalNodes = (4 * R + 5) * (4 * C + 5);

    vector<long long> dist(totalNodes, INF);
    vector<char> visited(totalNodes, 0);

    priority_queue<
        pair<long long,int>,
        vector<pair<long long,int>>,
        greater<pair<long long,int>>
    > pq;

    int s = idNode(rowLeaf[origem.first], colLeaf[origem.second]);
    int t = idNode(rowLeaf[destino.first], colLeaf[destino.second]);

    dist[s] = 0;
    pq.push({0, s});

    while (!pq.empty()) {
        auto [d, nodeId] = pq.top();
        pq.pop();

        if (visited[nodeId]) continue;
        visited[nodeId] = 1;

        if (nodeId == t) return d;

        int rNode = nodeId / CSIZE;
        int cNode = nodeId % CSIZE;

        bool rLeaf = (rL[rNode] == rR[rNode]);
        bool cLeaf = (cL[cNode] == cR[cNode]);

        auto relax = [&](int nr, int nc, long long nd) {
            int nid = idNode(nr, nc);

            if (!visited[nid] && nd < dist[nid]) {
                dist[nid] = nd;
                pq.push({nd, nid});
            }
        };

        if (!rLeaf && !cLeaf) {
            relax(rLeft[rNode], cLeft[cNode], d);
            relax(rLeft[rNode], cRight[cNode], d);
            relax(rRight[rNode], cLeft[cNode], d);
            relax(rRight[rNode], cRight[cNode], d);
        }
        else if (!rLeaf) {
            relax(rLeft[rNode], cNode, d);
            relax(rRight[rNode], cNode, d);
        }
        else if (!cLeaf) {
            relax(rNode, cLeft[cNode], d);
            relax(rNode, cRight[cNode], d);
        }
        else {
            int i = rL[rNode];
            int j = cL[cNode];

            long long nd = d + V[i][j];

            int r1 = max(0, i - AR[i][j]);
            int r2 = min(R - 1, i + AR[i][j]);
            int c1 = max(0, j - AC[i][j]);
            int c2 = min(C - 1, j + AC[i][j]);

            vector<int> rows, cols;
            getRows(1, r1, r2, rows);
            getCols(1, c1, c2, cols);

            for (int rn : rows) {
                for (int cn : cols) {
                    relax(rn, cn, nd);
                }
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C >> N;

    V.assign(R, vector<int>(C));
    AR.assign(R, vector<int>(C));
    AC.assign(R, vector<int>(C));

    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            cin >> V[i][j];

    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            cin >> AR[i][j];

    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            cin >> AC[i][j];

    pontos.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> pontos[i].first >> pontos[i].second;
        pontos[i].first--;
        pontos[i].second--;
    }

    CSIZE = 4 * C + 5;

    rL.assign(4 * R + 5, 0);
    rR.assign(4 * R + 5, 0);
    rLeft.assign(4 * R + 5, 0);
    rRight.assign(4 * R + 5, 0);
    rowLeaf.assign(R, 0);

    cL.assign(4 * C + 5, 0);
    cR.assign(4 * C + 5, 0);
    cLeft.assign(4 * C + 5, 0);
    cRight.assign(4 * C + 5, 0);
    colLeaf.assign(C, 0);

    buildRows(1, 0, R - 1);
    buildCols(1, 0, C - 1);

    for (int i = 0; i < N - 1; i++) {
        if (i) cout << " ";
        cout << dijkstra(pontos[i], pontos[i + 1]);
    }

    cout << "\n";

    return 0;
}
