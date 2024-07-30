* 定义常量
    1. `defind N 100005`
    1. `define INF 0x3f3f3f3f(1e19)`
    1. `define ll long long`
* 定义常见的操作
    1. `define For(i,st,en) for(i=st;i<en;i++)`
    1. `define max(a,b) ((a)>(b)?(a):(b))`
    1. `define printD(n) printf("%d",n)`

* 在主函数加上`ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);`这句可以提高cin、cout的速度，不如scanf
* 调试时从文件读取的方法：`freopen(".in","r",stdin);`
### 函数
1. **strlen** 位于string.h头文件，获取字符串长度。
        char s1[6] = {"hello"};
        cout<<strlen(s1);
        输出6。
1. **strcpy** 函数原型：覆盖原字符串
            `char * strcpy(char * dest,const char * src);`
            或 `char * strcpy(char * dest,char * src);`
            把src中的字符串复制到目的字符数组dest中。
            `char a[10],b[]={"copy"};`
            // strpy：把b中的字符串复制到目的字符数组a中
            strcpy(a,b);
            cout<<a;
            输出copy
1. **strncpy**  字符串后没有结束标志，需要自己添加'\0'
            char c[10],d[]={"JIANGJI"};
            strncpy(c,d,5);// 从d开始取n个字符
            c[5] = '\0';
            cout<<"c="<<c<<endl;
1. **strcat** 字符串连接
            char e[20] = "Come on!";
            char s[] = "Baby";
            strcat(e,s);
            cout<<e<<endl;
1. **memcpy** 拷贝
`memcpy(s2,s1,n) //s1中的n个字符拷贝到s2`
1. **reverse** 反转
`reverse(s,s+n) //将s中的前n项反转`
1. **strncat**  
输出Come on!Baby
1. **strmcp** 字符串比较,相同返回0，若不同则比较第一个不同的元素，s1>s2返回1，s1<s2返回-1
`int a = strmcp(s1,s2);`
1. **strncmp** 字符串比较，比较前n个
`int g = strncmp(s2,s3,5);`
            
1. **sizeof** 返回一个对象或类型所占的内存字节数。
1. **stoi** 将字符串转换为整型,位于string头文件
`int a = stoi(str)`
1. **substr**
1. **system("color F0")** 更改输出界面颜色
    * **F**代表背景颜色，**0**代表字体颜色
    * **背景颜色**的可选范围为0~F，**字体颜色**可选范围为0~7，对应关系如下：
        * 0 = 黑色
        * 1 = 蓝色
        * 2 = 绿色
        * 3 = 浅绿色（青色）
        * 4 = 红色
        * 5 = 紫色
        * 6 = 黄色
        * 7 = 白色
        * 8 = 灰色
        * 9 = 蓝灰色
        * A = 海绿色
        * B = 青绿色
        * C = 深红色
        * D = 紫罗兰色
        * E = 淡黄色
        * F = 亮白色
