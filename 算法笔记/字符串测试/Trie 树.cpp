/*
 * File: Trie 树.cpp
 * File Created: Friday, 2025-07-18 11:16:55
 * Author: Grok 3
 */
#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

// Trie 节点
struct TrieNode {
    map<char32_t, TrieNode*> children; // 使用 map 存储子节点，键为 Unicode 字符
    bool is_end;                       // 是否为字符串结尾

    TrieNode() : is_end(false) {}
};

// 将 UTF-8 字符串转换为 Unicode 字符序列
vector<char32_t> utf8_to_unicode(const string& str) {
    vector<char32_t> result;
    size_t i = 0;
    while (i < str.size()) {
        char32_t codepoint = 0;
        // 0x80 = 10000000 检查最高位知否为 0
        if ((str[i] & 0x80) == 0) { // 1 字节 (ASCII)
            codepoint = str[i];
            i += 1;
        } else if ((str[i] & 0xE0) == 0xC0) { // 2 字节
            codepoint = ((str[i] & 0x1F) << 6) | (str[i + 1] & 0x3F);
            i += 2;
        } else if ((str[i] & 0xF0) == 0xE0) { // 3 字节（中文常用）
            codepoint = ((str[i] & 0x0F) << 12) | ((str[i + 1] & 0x3F) << 6) | (str[i + 2] & 0x3F);
            i += 3;
        } else if ((str[i] & 0xF8) == 0xF0) { // 4 字节
            codepoint = ((str[i] & 0x07) << 18) | ((str[i + 1] & 0x3F) << 12) |
                        ((str[i + 2] & 0x3F) << 6) | (str[i + 3] & 0x3F);
            i += 4;
        }
        result.push_back(codepoint);
    }
    return result;
}

// Trie 类
class Trie {
private:
    TrieNode* root;

    // 递归清理内存
    void clear(TrieNode* node) {
        if (!node) return;
        for (auto& child : node->children) {
            clear(child.second);
        }
        delete node;
    }

public:
    Trie() {
        root = new TrieNode();
    }

    // 插入字符串
    void insert(const string& word) {
        TrieNode* node = root;
        vector<char32_t> chars = utf8_to_unicode(word);
        for (char32_t c : chars) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->is_end = true;
    }

    // 查找字符串
    bool search(const string& word) {
        TrieNode* node = root;
        vector<char32_t> chars = utf8_to_unicode(word);
        for (char32_t c : chars) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->is_end;
    }

    // 查找前缀
    bool startsWith(const string& prefix) {
        TrieNode* node = root;
        vector<char32_t> chars = utf8_to_unicode(prefix);
        for (char32_t c : chars) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return true;
    }

    // 析构函数
    ~Trie() {
        clear(root);
    }
};

// 使用示例
int main() {
    Trie trie;
    trie.insert("你好");
    trie.insert("世界");
    cout << trie.search("你好") << endl;    // 输出 1
    cout << trie.search("你") << endl;      // 输出 0
    cout << trie.startsWith("世") << endl;  // 输出 1
    cout << trie.startsWith("你好") << endl; // 输出 1
    return 0;
}