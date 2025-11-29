/*
 * Source of the problem: Unknow
 * File: 1.3 埃氏筛.cpp
 * File Created: Friday, 2025-07-25 14:10:11
 * Author: 犯困的00后最喜欢夏天
 * Result: Pending
 * Time: 0 ms
 */
#include <iostream>
#include <vector>

using namespace std;

int n = 100; // 找出小于等于 n 的所有素数
int isPrime[101] = {0};   // 1 表示素数，0 表示非素数

int main() {
    int n = 100; // 找出小于等于 n 的所有素数
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) { // 如果 i 是素数
            for (int j = i * i; j <= n; j += i) {   // j = i * 2 效率略低，注意不要溢出
                isPrime[j] = false;
            }
        }
    }
    for (int i = 2; i <= n; i++) if (isPrime[i]) cout << i << ' ';

    return 0;
}