/*
 * Source of the problem: Unknow
 * File: manacher_suffix.cpp
 * File Created: Sunday, 2025-07-13 19:49:35
 * Author: 犯困的00后最喜欢夏天
 * Result: 小数据通过
 */
#include <iostream>
#include <vector>

using namespace std;

int manacher_suffix(const string &s) {
    vector<char> t;
    for (char c : s) {
        t.push_back('#');
        t.push_back(c);
    }
    t.push_back('#');
    int n = t.size(), ans = 0;
    vector<int> p(n, 0);
    int mx = 0, id = 0;
    for (int i = 0; i < n; i++) {
        if (i < mx) p[i] = min(p[2 * id - i], mx - i);
        while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 && t[i + p[i] + 1] == t[i - p[i] - 1]) p[i]++;
        if (i + p[i] > mx) {
            mx = i + p[i];
            id = i;
        }
        if (i + p[i] == n - 1) {
            ans = max(ans, p[i]);
        }
    }
    return ans;
}

int main() {
    string s;
    cin >> s;
    cout << manacher_suffix(s) << '\n';

    return 0;
}