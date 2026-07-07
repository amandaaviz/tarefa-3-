#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <limits>

using namespace std;

struct Ponto {
    double x, y;
};

double distancia(const Ponto &a, const Ponto &b) {
    return sqrt((a.x - b.x) * (a.x - b.x) +
                (a.y - b.y) * (a.y - b.y));
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    while (cin >> N) {

        vector<Ponto> p(N);

        for (int i = 0; i < N; i++)
            cin >> p[i].x >> p[i].y;

        vector<double> minDist(N, numeric_limits<double>::max());
        vector<bool> usado(N, false);

        minDist[0] = 0;

        double resposta = 0.0;

        for (int i = 0; i < N; i++) {

            int u = -1;

            for (int j = 0; j < N; j++) {
                if (!usado[j] && (u == -1 || minDist[j] < minDist[u]))
                    u = j;
            }

            usado[u] = true;
            resposta += minDist[u];

            for (int v = 0; v < N; v++) {

                if (!usado[v]) {

                    double d = distancia(p[u], p[v]);

                    if (d < minDist[v])
                        minDist[v] = d;
                }
            }
        }

        cout << fixed << setprecision(2) << resposta << "\n";
    }

    return 0;
}
