#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;

vector<vector<int>> dista;
vector<vector<int>> meio;
vector<string> cidade;

vector<int> construirCaminho(int i, int j) {
    if (meio[i][j] == -1) {
        return {i, j};
    }

    int k = meio[i][j];

    vector<int> esq = construirCaminho(i, k);
    vector<int> dir = construirCaminho(k, j);

    esq.pop_back();

    for (int x : dir)
        esq.push_back(x);

    return esq;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int P;
        cin >> P;

        cidade.assign(P, "");
        unordered_map<string, int> id;

        for (int i = 0; i < P; i++) {
            cin >> cidade[i];
            id[cidade[i]] = i;
        }

        dista.assign(P, vector<int>(P, INF));
        meio.assign(P, vector<int>(P, -1));

        for (int i = 0; i < P; i++) {
            for (int j = 0; j < P; j++) {
                int w;
                cin >> w;

                if (w != -1) {
                    dista[i][j] = w;
                }
            }
        }

        for (int k = 0; k < P; k++) {
            for (int i = 0; i < P; i++) {
                for (int j = 0; j < P; j++) {
                    if (dista[i][k] == INF || dista[k][j] == INF)
                        continue;

                    int novo = dista[i][k] + dista[k][j];

                    if (novo < dista[i][j]) {
                        dista[i][j] = novo;
                        meio[i][j] = k;
                    }
                }
            }
        }

        int R;
        cin >> R;

        while (R--) {
            string funcionario, origem, destino;
            cin >> funcionario >> origem >> destino;

            int s = id[origem];
            int d = id[destino];

            if (dista[s][d] == INF) {
                cout << "Sorry Mr " << funcionario
                     << " you can not go from "
                     << origem << " to "
                     << destino << "\n";
            } else {
                cout << "Mr " << funcionario
                     << " to go from "
                     << origem
                     << " to "
                     << destino
                     << ", you will receive "
                     << dista[s][d]
                     << " euros\n";

                vector<int> caminho;

                if (s == d) {
                    caminho.push_back(s);
                    caminho.push_back(d);
                } else {
                    caminho = construirCaminho(s, d);
                }

                cout << "Path:";

                for (int i = 0; i < (int)caminho.size(); i++) {
                    if (i > 0)
                        cout << " ";

                    cout << cidade[caminho[i]];
                }

                cout << "\n";
            }
        }
    }

    return 0;
}
