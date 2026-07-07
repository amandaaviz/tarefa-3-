#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Ponto {
    double x, y;
};

struct Aresta {
    int u, v;
    double peso;

    bool operator<(const Aresta &other) const {
        return peso < other.peso;
    }
};

vector<int> pai;
vector<int> tamanho;

int find(int x) {
    if (pai[x] == x)
        return x;
    return pai[x] = find(pai[x]);
}

bool unite(int a, int b) {

    a = find(a);
    b = find(b);

    if (a == b)
        return false;

    if (tamanho[a] < tamanho[b])
        swap(a, b);

    pai[b] = a;
    tamanho[a] += tamanho[b];

    return true;
}

double distancia(Ponto a, Ponto b) {

    return sqrt(
        (a.x - b.x) * (a.x - b.x) +
        (a.y - b.y) * (a.y - b.y)
    );
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    while (cin >> N) {

        vector<Ponto> pontos(N);

        for (int i = 0; i < N; i++)
            cin >> pontos[i].x >> pontos[i].y;

        vector<Aresta> arestas;

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {

                arestas.push_back({
                    i,
                    j,
                    distancia(pontos[i], pontos[j])
                });

            }
        }

        sort(arestas.begin(), arestas.end());

        pai.resize(N);
        tamanho.assign(N,1);

        for (int i = 0; i < N; i++)
            pai[i] = i;

        double resposta = 0;
        int usadas = 0;

        for (auto &e : arestas) {

            if (unite(e.u, e.v)) {

                resposta += e.peso;
                usadas++;

                if (usadas == N - 1)
                    break;
            }

        }

        cout << fixed << setprecision(2)
             << resposta << "\n";
    }

    return 0;
}
