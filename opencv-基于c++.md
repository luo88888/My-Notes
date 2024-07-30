### OpenCV部分函数

1. **imread()** 图像读取函数
    * 函数原型`cv::Mat cv::imread(const String & filename,int flags=IMREAD_COLOR)`
    * **filename**：图片地址。
    * **flags**：   读取图片形式的标志，如将彩色图片按照灰度图读取，默认是按彩色图像格式读取。
    * **flags**可选参数：
        * **-1 IMREAD_UNCHANGED**   按照图像原样读取，保留Alpha通道（第4通道）
        * **0 IMREAD_GRAYSCALE**    将图像转换为单通道灰度图象后读取
        * **1 IMREAD_COLOR**        将图像转换成3通道BGR彩色图像
        * **2 IMREAD_ANYDEPTH**     保留原图像的16位、32位深度，不声明该参数则转成8为读取
        * **4 IMREAD_ANYCOLOR**     以任何可能得颜色读取图像
        * **8 IMREAD_LOAD_GDAL**    使用gdal驱动程序加载图像
        * **16 IMREAD_ REDUCED_GRAYSCALE_2**    将图像转换成单通道灰度图像，尺寸缩小1/2。可以更改最后一位数字实现缩小1/4、1/8（最后一位改为4、8）
        * **17 IMREAD_REDUCED_COLOR_2**         将图像转成3通道彩色图像，尺寸缩小1/2。可以更改最后一位数字实现缩小1/4、1/8（最后一位改为4、8）
        * **128 IMREAD_IGNORE_ORIENTATION**     不以EXIF的方向旋转图像
1. **imshow** 图像显示函数
    * 函数原型`void cv::imshow(const String & winname,InputArray mat)`
    * **winname**：要显示图片的窗口的名字，用字符串形式赋值。
    * **mat**：要显示的图像的矩阵（Mat）。
    * **InputArray**：这个是OpenCV定义的一个类型声明引用，用作输入参数的标识，我们在遇到它时可以认为是需要输入一个Mat类型数据。
    * 会缩放图片以适应窗口属性。
    * 若winname窗口不存在，则会以WINDOW_AUTOSIZE标志创建一个。
1. **imwrite** 保存图像
    * 函数原型`bool cv::imwrite(const String& filename,InputArray img,Const std::vector<int>& params = std::vector<int>())`
        * 保存成功返回**true**，否则返回**false**
        * **filename**：保存图像的路径
        * **img**：将要保存的Mat类矩阵变量
        * **params**：保存图片属性设置标志，该参数一般不需填写
1. **namedWindow()** 图像窗口函数
    * 函数原型`void cv::namedWindow(const String & winname,int flags = WINDOW_AUTOSIZE)`
    * **winname**：窗口名称，用作窗口的标识符
    * **flags**：   窗口属性标志
    * ***flags可选参数***
        * **WINDOW_NORMAL**        显示图片后允许用户随意调整窗口大小。
        * **WINDOW_AUTOSIZE**      根据图像大小显示窗口，不允许用户调整大小。
        * **WINDOW_OPENGL**        创建窗口的时候会支持OpenGL
        * **WINDOW_FULLSCREEN**    全屏显示窗口
        * **WINDOW_FREERATIO**     调整图片尺寸以充满窗口
        * **WINDOW_KEEPRATIO**     保持图像的比例
        * **WINDOW_GUI_EXPANDED**  创建的窗口允许添加工具栏和状态栏
        * **WINDOW_GUI_NORMAL**    创建没有状态栏和工具栏的窗口
1. **destroyWindow()** 销毁窗口
    * 接收一个字符串，关闭指定名称的窗口。
1. **destroyAllWindow** 销毁所有窗口
    * 关闭所有窗口。  

### VideoCapture类
1. 构造函数
    * `cv::VideoCapture::VideoCapture();   //默认构造函数`
    * `cv::VideoCapture::VideoCapture(const String& filename,int apiPreference=CAP_ANY)` 
        * **filename** 视频文件或图像序列名称
        * **apiPreference** 读取数据时设置的属性，例如编码格式、是否调用OpenNI等
1. **get()**方法
    * 通过输入指定标志获取视频属性，例如图像的像素尺寸、帧数、帧率等。
    * 常用的标志和含义如下（更多见图1-1）
        * **0 CAP_PROP_POS_MSeC** 视频文件的当前位置（以毫秒为单位）
        * **3 CAP_PROP_FRAMEWIDTH** 视频流中图像的宽度
        * **4 CAP_PROP_FRAME_HEIGHT** 视频流中图像的高度
        * **5 CAP_PROP_FRAME_FPS** 视频流中图像的帧率（每秒帧数）
        * **7 CAP_PROP_FRAME_COUNT** 视频流中图像的帧数
    ![图片显示失败](IMG_20240601_153532.jpg)
1. 构造函数
    * `cv::VideoCapture::VideoCapture(int index,int apiPreference = CAP_ANY)`
        * **index** 需要打开的摄像头的索引
        * 通过摄像头获取视频时，VideoCapture类具有的属性同样可以使用

### VideoWriter类
1. 构造函数
    * `cv::VideoWriter::VideoWriter();`
    * `cv::VideoWriter::VideoWriter(const String& filename,int fourcc,double fps,Size frameSize,bool isColor=true)`
        * **filename** 保存视频的路径，包含视频格式
        * **fourcc** 压缩帧的4字符编码器代码，赋值“-1”会自动搜索合适的编解码器。详细参数见图1-3
        * **fps** 保存视频的帧率
        * **frameSize** 视频帧的尺寸
        * **isColor** 保存视频是否为彩色视频

### FileStorage类
1. 构造函数
    * `cv::FileStorage::FileStorage(const String & filename,int flags,const String & encoding = String())`
        * **filename** 文件路径
        * **flags** 对文件进行的操作类型标志
            1. **0 READ**:读
            1. **1 WRITE**:写，会覆盖原有内容
            1. **2 APPEND**:追加
            1. **4 MEMORY**:将数据写入或读取到内部缓冲区
        * **encoding** 编码格式
        * 写入操作文件可以不存在
        * 默认构造函数没有任何参数，需要通过FileStorage类中的open()函数单独声明，open()函数原型如下：
        `virtual bool cv::FileStorage::open(const String & filename,int flags,const String & encoding=String())`成功打开文件返回true，否则返回false
1. 成员函数
    1. **isOpened** 判断是否成功打开文件
    1. **write()** 
        * 函数原型`void cv::FileStorage::write(const String & name,int val)`
            * **name**:写入文件中变量的名称
            * **val**:变量值,write()函数有多个重载版本，可以将double,String,Mat,vector<String>类型变量写入文件中
* ***FileStorage***类的用法请见**FileStorage示例**
