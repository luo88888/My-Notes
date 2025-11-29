/*
 * Source of the problem: Unknow
 * File: manacher.cpp
 * File Created: Sunday, 2025-07-13 19:53:12
 * Author: 犯困的00后最喜欢夏天
 * Result: Peding
 */
#include <iostream>
#include <vector>

using namespace std;

int manacher(const string &s) {
    vector<char> t;
    // s = s + '#'+ c 较慢
    for (char c : s) {
        t.push_back('#');
        t.push_back(c);
    }
    t.push_back('#');
    int n = t.size();
    vector<int> p(n, 0);
    int mx = 0, id = 0;
    for (int i = 0; i < n; i++) {
        if (i < mx) p[i] = min(p[2 * id - i], mx - i);
        while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 && t[i + p[i] + 1] == t[i - p[i] - 1]) p[i]++;
        if (i + p[i] > mx) {
            mx = i + p[i];
            id = i;
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, p[i]);
    }
    return ans;
}

int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        string s;
        cin >> s;
        cout << manacher(s) << '\n';
    }

    return 0;
}