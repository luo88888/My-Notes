my_dictionary = {'location':[20,30], 'color':'green'}
print(my_dictionary)

nums = [1, 2, 3, 4, 5]
for num in nums[:3]:
    num += 1
print(nums)

# 创建一个用于存储外星人的空列表。
aliens = [] 
# 创建 30 个绿色的外星人。
for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
    aliens.append(new_alien) 
for alien in aliens[:3]: 
    if alien['color'] == 'green': 
        alien['color'] = 'yellow' 
        alien['speed'] = 'medium' 
        alien['points'] = 10 
# 显示前 5 个外星人。
for alien in aliens[:5]: 
    print(alien) 
print("...")


# 不可变类型示例

s = "hello"
print(id(s))
s += " world"
print(s)  # 输出: hello world
print(id(s))  # 输出: 一个新的内存地址，因为 s 已经指向了一个新的字符串

# 可变类型示例
lst = [1, 2, 3]
print(id(lst))
lst[0] = 10
print(lst)  # 输出: [10, 2, 3]
print(id(lst))  # 输出: 同一个内存地址，因为 lst 指向的还是同一个列表对象