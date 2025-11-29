/*
 * Source of the problem: Unknow
 * File: 1.4 线性筛.cpp
 * File Created: Friday, 2025-07-25 14:32:49
 * Author: 犯困的00后最喜欢夏天
 * Result: Pending
 * Time: 0 ms
 */
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n = 100; // 找出小于等于 n 的所有素数
    vector<bool> isPrime(n + 1, true); // true 表示素数，false 表示非素数
    vector<int> primes; // 存储素数
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) { // 如果 i 是素数
            primes.push_back(i);
        }
        for (int j = 0; j < primes.size() && i * primes[j] <= n; j++) {
            isPrime[i * primes[j]] = false; // 标记合数
            if (i % primes[j] == 0) break; // 确保每个合数只被最小素数因子筛掉
        }
    }
    for (int x : primes) cout << x << ' ';
    cout << '\n';

    for (int i = 2; i <= n; i++) if (isPrime[i]) cout << i << ' ';

    return 0;
}