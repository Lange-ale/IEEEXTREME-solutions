#include <bits/stdc++.h>
using namespace std;

pair<int, int> findLetter(const vector<vector<char>>& grid, char c, char pos) {
    int i, j;
    if (pos == 'S') {
        for (int k = 0; k < grid.size(); k++)
            for (int l = 0; l < grid[k].size(); l++)
                if (grid[k][l] == c) {
                    i = k;
                    j = l;
                    return make_pair(i + 1, j + 1);
                }
    }
    for (int k = grid.size() - 1; k >= 0; k--)
        for (int l = grid[k].size() - 1; l >= 0; l--)
            if (grid[k][l] == c) {
                i = k;
                j = l;
                return make_pair(i + 1, j + 1);
            }
    return make_pair(-1, -1);
}

int main() {
    int p, n, R, C;
    char pos;
    queue<string> phrases, XML;
    vector<string> chiper;
    cin >> p >> n;
    string temp;
    cin >> temp;
    R = stoi(temp.substr(0, temp.find(',')));
    C = stoi(temp.substr(temp.find(',') + 1));
    vector<vector<char>> grid(R, vector<char>(C));
    cin >> pos;
    for (int i = 0; i < p; i++) {
        cin >> temp;
        phrases.push(temp);
    }
    getline(cin, temp);
    for (int i = 0; i < n; i++) {
        getline(cin, temp);
        XML.push(temp);
    }

    int i = 0, j = 0;
    while (!XML.empty() && i < R && j < C) {
        temp = XML.front();
        XML.pop();
        for (int k = 0; k < temp.size(); k++) {
            if (temp[k] == '<')
                while (temp[k] != '>')
                    k++;
            else
                grid[i][j++] = temp[k] != ' ' ? temp[k] : '_';
            if (j == C) {
                j = 0;
                i++;
                if (i == R)
                    break;
            }
        }
    }

    unordered_map<char, pair<int, int>> positions;
    for (char c = 0; c < 127; c++)
        positions[c] = findLetter(grid, c, pos);

    while (!phrases.empty()) {
        temp = phrases.front();
        phrases.pop();
        chiper.emplace_back("");
        for (const char& c : temp) {
            if (positions.find(c) == positions.end())
                positions[c] = findLetter(grid, c, pos);
            if (positions[c].first == -1) {
                chiper.back() = "0 ";
                break;
            }
            chiper.back() += to_string(positions[c].first) + "," + to_string(positions[c].second) + ",";
        }
        chiper.back().pop_back();
    }

    for (const string& s : chiper)
        cout << s << endl;
/*
    // print positions
    for (const auto& p : positions)
        cout << p.first << " " << p.second.first << " " << p.second.second << endl;

    // print grid
    for (const auto& row : grid) {
        for (const auto& c : row)
            cout << c;
        cout << endl;
    }*/

    return 0;
}