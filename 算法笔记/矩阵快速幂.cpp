/*
 * Source of the problem: Unknow
 * File: 矩阵快速幂.cpp
 * File Created: Friday, 2025-08-15 07:57:34
 * Author: 犯困的00后最喜欢夏天
 * Result: Pending
 * Time: 0 ms
 */
#include <iostream>
#include <vector>

using namespace std;

struct Matrix {
    vector<vector<int64_t> > mat;
    int n, m;

    Matrix(int n_, int m_) : n(n_), m(m_) {
        mat.resize(n, vector<int64_t>(m, 0));
    }

    // 矩阵乘法
    Matrix operator*(const Matrix &B) const {
        Matrix result(n, B.m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < B.m; ++j) {
                for (int k = 0; k < m; ++k) {
                    result.mat[i][j] += mat[i][k] * B.mat[k][j];    // % mod
                }
            }
        }
        return result;
    }

    // 只对方阵有效
    Matrix operator^(int64_t power) const {
        Matrix result(n, m);
        for (int i = 0; i < n; ++i) {
            result.mat[i][i] = 1;
        }
        Matrix base = *this;

        while (power) {
            if (power & 1) {
                result = result * base;
            }
            base = base * base;
            power >>= 1;
        }
        return result;
    }
};

int64_t fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    Matrix fib(2, 2);
    fib.mat[0][0] = 1; fib.mat[0][1] = 1;
    fib.mat[1][0] = 1; fib.mat[1][1] = 0;

    Matrix result = fib ^ (n - 1);
    return result.mat[0][0];
}

int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n;
        cin >> n;
        cout << fibonacci(n) << '\n';
    }
    return 0;
}