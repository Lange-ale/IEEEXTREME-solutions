#include <bits/stdc++.h>
using namespace std;

int main() {
    int budget, n;
    cin >> budget;
    vector<vector<string>> players(5);
    vector<vector<int>> prices(5);
    for (int i = 0; i < 5; i++) {
        cin >> n;
        prices[i].resize(n);
        players[i].resize(n);
        for (int j = 0; j < n; j++)
            cin >> players[i][j] >> prices[i][j];
    }
    int positions[] = {0, 0, 0, 0, 0};

    int max_price = 0;
    for (int i = 0; i < prices[0].size(); ++i) {
        for (int j = 0; j < prices[1].size(); ++j) {
            for (int k = 0; k < prices[2].size(); ++k) {
                for (int l = 0; l < prices[3].size(); ++l) {
                    for (int m = 0; m < prices[4].size(); ++m) {
                        int price = prices[0][i] + prices[1][j] + prices[2][k] + prices[3][l] + prices[4][m];
                        if (price > max_price && price <= budget) {
                            max_price = price;
                            positions[0] = i;
                            positions[1] = j;
                            positions[2] = k;
                            positions[3] = l;
                            positions[4] = m;
                        }
                    }
                }
            }
        }
    }
    cout << players[0][positions[0]] << endl << players[1][positions[1]] << endl << players[2][positions[2]] << endl << players[3][positions[3]] << endl << players[4][positions[4]] << endl;

    return 0;
}
