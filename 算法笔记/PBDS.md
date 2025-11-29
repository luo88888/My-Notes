### PBDS（Policy-Based Data Structure）
#### 1. 简介
PBDS 是 GNU C++ 提供的扩展库（ext/pb_ds），基于红黑树实现，支持高效的动态有序数据结构。相比标准库的 std::set 和 std::map，PBDS 提供额外功能，如秩查询（order_of_key）和按秩查找（find_by_order），适用于算法竞赛和复杂数据处理。

- 头文件：
```cpp
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
```

- 核心数据结构：红黑树（rb_tree_tag，快）或 Splay 树（splay_tree_tag，中）、ov_tree_tag（有序向量树，慢），红黑树更常用。
- 复杂度：
    插入、删除、查询：$(O(\log n))$
    秩查询和按秩查找：$(O(\log n))$



#### 2. PBDS 类型定义
PBDS 通过模板定义数据结构，常用类型为有序集合（set）或多重集合（multiset）。以下是定义方式：
##### 2.1 有序集合（无重复元素）
```cpp
typedef tree<
    int,                        // 键类型
    null_type,                  // 值类型（null_type 表示集合而非映射）
    less<int>,                  // 比较函数（升序，无重复）
    rb_tree_tag,                // 红黑树
    tree_order_statistics_node_update // 支持秩查询
> pbds_set;
```

- 功能：
    类似 std::set，但支持额外操作。
    less<int> 确保键严格升序，自动去重。



##### 2.2 多重集合（允许重复元素）
```cpp
typedef tree<
    int,                        // 键类型
    null_type,                  // 值类型
    less_equal<int>,            // 比较函数（允许重复）
    rb_tree_tag,                // 红黑树
    tree_order_statistics_node_update
> pbds_multiset;
```

- 注意：
    使用 less_equal<int> 允许重复键（multiset 行为）。
    插入重复元素会被记录多次，`order_of_key(k)` 返回严格小于 (k) 的元素数。



##### 2.3 映射（键值对）
```cpp
typedef tree<
    int,                        // 键类型
    int,                        // 值类型（非 null_type）
    less<int>,                  // 比较函数
    rb_tree_tag,
    tree_order_statistics_node_update
> pbds_map;
```
- 类似 std::map，但支持秩操作。

#### 3. 核心操作
PBDS 支持以下关键操作（以 pbds_multiset 为例）：
##### 3.1 插入
```cpp
pbds_multiset s;
s.insert(5); // 插入元素 5，O(log n)
s.insert(5); // 可再次插入 5（多重集合）
```

##### 3.2 删除

- 删除特定值的一个实例（多重集合中需注意）：
```cpp
s.erase(s.find(5)); // 删除一个 5，O(log n)
```

- 删除所有某值：
```cpp
s.erase(5); // 删除所有 5，O(log n + k)，k 为重复次数
```

**注意**：直接 erase(5) 删除所有值为 5 的节点，而 erase(s.find(5)) 只删除一个实例。


##### 3.3 秩查询
```cpp
order_of_key(k); // 返回集合中严格小于 (k) 的元素个数。
s.insert(1); s.insert(3); s.insert(3); s.insert(5);
cout << s.order_of_key(3) << endl; // 输出 1（只有 1 小于 3）
cout << s.order_of_key(4) << endl; // 输出 3（1, 3, 3 小于 4）
```
复杂度：$(O(\log n))$

##### 3.4 按秩查找
```cpp
find_by_order(k); // 返回第 (k) 小元素的迭代器（从 0 开始计数）。
auto it = s.find_by_order(2); // 返回第 2 小元素（0-based）
if (it != s.end()) cout << *it << endl; // 输出 3（集合为 {1, 3, 3, 5}）
```


复杂度：$(O(\log n))$

##### 3.5 其他操作

- 标准集合操作：size(), empty(), clear(), find(k) 等。
- 迭代器遍历：支持 begin(), end()，可按序遍历所有元素。

#### 4. 典型应用
PBDS 常用于需要动态维护有序数据和秩查询的场景，例如：

##### 4.1 动态第 (k) 小

- 问题：查询动态集合中第 (k) 小元素。
- 方法：用 find_by_order(k) 获取第 (k) 小元素。
- 例：实时查询中位数或特定排名的元素。

##### 4.2 区间计数

- 问题：查询区间 $[l, r)$ 中的元素数。
- 方法：计算 order_of_key(r) - order_of_key(l)。
- 例：int count = s.order_of_key(r) - s.order_of_key(l);



#### 5. 优势与局限
##### 5.1 优势

- 功能强大：支持 std::set 所有功能外加秩查询和按秩查找。
- 高效：红黑树保证 $(O(\log n))$ 操作，适合动态维护。
- 简洁：某些情况下可以替代线段树、树状数组等复杂数据结构，代码更简洁。
- 支持重复：less_equal<int> 实现多重集合，灵活处理重复元素。

#### 5.2 局限

- **非标准库**：需确保编译器支持 GNU PBDS。
- 常数较大：红黑树常数可能略高于树状数组，需权衡。
- 内存开销：相比简单数组实现的线段树，PBDS 内存占用稍高。
- **注意事项**：
less_equal<int> 的多重集合中，order_of_key(k) 返回严格小于 (k) 的个数，需注意边界。
删除操作需谨慎区分删除单个实例还是所有实例。



#### 6. 示例代码
以下是一个简单示例，展示 PBDS 的基本用法：
```cpp
#include <iostream>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> pbds_multiset;

int main() {
    pbds_multiset s;
    s.insert(1); s.insert(3); s.insert(3); s.insert(5);
    
    cout << s.order_of_key(3) << endl; // 输出 1（小于 3 的有 1 个）
    cout << s.order_of_key(4) << endl; // 输出 3（小于 4 的有 1, 3, 3）
    cout << *s.find_by_order(2) << endl; // 输出 3（第 2 小元素，0-based）
    
    s.erase(s.find(3)); // 删除一个 3
    cout << s.order_of_key(4) << endl; // 输出 2（剩余 1, 3, 5）
    
    return 0;
}
```

#### 7. 注意事项

- 编译环境：确保使用支持 PBDS 的编译器（如 g++，Codeforces 默认支持）。
- 边界处理：order_of_key(k) 返回**严格**小于 (k) 的个数，注意查询边界（如 (k-1)）。
- 重复元素：多重集合需用 less_equal<int>，但删除时需用迭代器操作单个实例。