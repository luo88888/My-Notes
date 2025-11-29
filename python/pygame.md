#### 字体
1. **使用字体文件**
    `font = pygame.font.Font(path, size)`
1. **使用系统字体**
    `font = pygame.font.SysFont(name, size, bold=False, italic=False)`
    这个函数用于从系统字体中创建一个 Font 对象。这个函数通常用于当你想要使用操作系统提供的字体时，
    - name：这是字体的名称，例如 "arial"、"verdana" 或者 None（表示默认的系统字体）。
    - size：这是字体的大小（以像素为单位）。
    - bold：如果设置为 True，则字体将以粗体显示，默认是 False。
    - italic：如果设置为 True，则字体将以斜体显示，默认是 False。
1. **将文本转化为Surface对象**
    Font 对象的 render 方法用于将文本字符串渲染成一个图像（Surface 对象），以便可以在屏幕上显示。render 方法的基本语法如下：
    `font.render(text, antialias, color, background=None)`
    - text：要渲染的文本字符串。
    - antialias：一个布尔值，如果为 True，则启用抗锯齿效果，使文本边缘更加平滑；如果为 False，则禁用抗锯齿效果。
    - color：文本的颜色，通常是一个 RGB 元组（例如 (255, 0, 0) 表示红色）或颜色名称（如 "red"）。
    - background（可选）：文本背景的颜色，也是一个 RGB 元组或颜色名称。如果不提供此参数，则文本没有背景色。

#### pygame.font
* **函数**
    `pygame.font.init()` —— 初始化字体模块
    `pygame.font.quit()` —— 还原字体模块
    `pygame.font.get_init()` —— 检查字体模块是否被初始化
    `pygame.font.get_default_font()` —— 获得默认字体的文件名
    `pygame.font.get_fonts()` —— 获取所有可使用的字体
    `pygame.font.match_font()` —— 在系统中搜索一种特殊的字体
    `pygame.font.SysFont()` —— 从系统字体库创建一个 Font 对象


* **函数详解**
    - `pygame.font.init()` 初始化字体模块
        - init() -> None
        - 在调用 pygame.init() 时，该函数会被自动调用。
        - 该函数用于初始化字体模块。在使用其他任何函数前，该模块必须被初始化。
        - 多次调用该函数是安全的。

    - `pygame.font.get_init()` 检查字体模块是否被初始化
        - get_init() -> bool
        - 如果该字体模块已经初始化，返回 True，否则返回 False。

    - `pygame.font.get_fonts()` 获取所有可使用的字体
        - get_fonts() -> list of strings
        - 返回系统可使用的字体列表。
        - 字体名将会被设置成小写、所有的空格和标点符号也会将被删除。
        - 该函数在大多数系统内是有效的，但是一些系统如果没有找到字体库会返回一个空的列表。

    - `pygame.font.match_font()` 在系统中搜索一种特殊的字体
        - match_font(name, bold=False, italic=False) -> path
        - 返回字体文件在系统中的完整路径。
        - 如果你要搜索的字体是粗体或者斜体的，则要把 bold 参数和 italic 参数设置成 True，该函数将会尝试去搜索一个正确的字体族。
        - 尝试搜索的 name 参数可以是一个用逗号隔开的列表。如果根据提供的名字没有找到任何东西，则返回 None 。
    - `pygame.font.SysFont()` 从系统字体库创建一个 Font 对象
        - SysFont(name, size, bold=False, italic=False) -> Font
        - 从系统字体库中加载并返回一个新的字体对象。
        - 该字体将会匹配 bold（加粗）和 italic（斜体）参数的要求。
        - 如果找不到一个合适的系统字体，该函数将会回退并加载默认的 pygame 字体。
        - 尝试搜索的 name 参数可以是一个用逗号隔开的列表。

* **类 class pygame.font.Font**
    从一个字体文件创建一个 Font 对象。
    Font(filename, size) -> Font
    Font(object, size) -> Font
    - 方法
        - pygame.font.Font.render() —— 在一个新 Surface 对象上绘制文本
        - pygame.font.Font.size() —— 确定多大的空间用于表示文本
        - pygame.font.Font.set_underline() —— 控制文本是否用下划线渲染
        - pygame.font.Font.get_underline() —— 检查文本是否绘制下划线
        - pygame.font.Font.set_bold() —— 启动粗体字渲染
        - pygame.font.Font.get_bold() —— 检查文本是否使用粗体渲染
        - pygame.font.Font.set_italic() —— 启动斜体字渲染
        - pygame.font.Font.metrics() —— 获取字符串参数每个字符的参数
        - pygame.font.Font.get_italic() —— 检查文本是否使用斜体渲染
        - pygame.font.Font.get_linesize() —— 获取字体文本的行高
        - pygame.font.Font.get_height() —— 获取字体的高度
        - pygame.font.Font.get_ascent() —— 获取字体顶端到基准线的距离
        - pygame.font.Font.get_descent() —— 获取字体底端到基准线的距离
    根据提供的文件名或者 python 文件对象加载一个新的字体。字体的高度是以像素为单位。如果文件名是 “None”，则加载 Pygame 的默认字体。如果一个字体无法由给定的参数加载，将会产生一个异常。一旦字体已经创建完毕，那么字体的尺寸将不能修改。
    字体对象主要被用于在新 Surface 对象中渲染文本。文本可以渲染为仿真的粗体或者斜体特征，但最好是加载的字体本身就带有粗体或者斜体字形。可以用普通字符串或者 Unicode 编码字符来渲染文本。
* **pygame.font.Font.render()**
    作用：在一个新 Surface 对象上绘制文本
    `render(text, antialias, color, background=None) -> Surface`
    
    该函数创建一个新的 Surface 对象，并在上边渲染指定的文本。Pygame 没有提供直接的方式在一个现有的 Surface 对象上绘制文本，取而代之的方法是：使用 Font.render() 函数创建一个渲染了文本的图像（Surface 对象），然后将这个图像绘制到目标 Surface 对象上。

    仅支持渲染一行文本：“换行”字符不会被渲染。空字符（‘x00’）被渲染将产生一个 TypeError 错误。Unicode 和 char（字节）字符串都可以被接受。对于 Unicode 字符串，仅 UCS-2 字符范围（‘u0001’ 到 ‘uFFFF’）被认为是有效的。任何编码值更大字符的字符会产生一个 UnicodeError 的错误；对于 char 字符串，默认的是使用 LATIN1 编码。color 参数决定的是文本的颜色（例如：(0, 0, 255) 表示蓝色）。可选参数 background 决定了文本的背景颜色。如果没有传递 background 参数，则对应区域内表示的文本背景将会被设置为透明。

    返回的 Surface 对象将保持表示文本所需要的尺寸（与 Font.size() 所返回的尺寸相同）。如果将一个空字符串渲染为文本，将会返回一个空白 Surface 对象，它仅有一个像素点的宽度，但高度与字体高度一样。

    由于取决于文本背景的类型和抗锯齿功能的使用，该函数将会返回不同类型的 Surface 对象。出于性能上的考虑，了解何种类型的图像会被使用是很有帮助的：如果抗锯齿功能没有被使用，返回的图像将采用二元调色的 8 位图像。此时如果背景是透明的，只设置一个 colorkey 来实现；抗锯齿图像会被渲染为 24 位 RGB 图像。此时如果背景是透明的，每个像素都将包含一个 alpha 通道。

    优化：如果你已知文本最终将绘制在一个纯色的背景上，那么文本是抗锯齿的，你可以通过指定文本的背景色来提高性能（将文本背景色设置目标 Surface 对象的颜色）。使用这个技巧，你只需用一个 colorkey 即可保持透明信息，而不需要设置每个像素的 alpha 通道值（这样效率会低很多）。

    如果你尝试渲染 ‘\n’，通常是显示为一个矩形（未知字符）。因此，你需要自己想办法处理换行。

    字体渲染并不是线程安全的行为：在任何时候仅有一个线程可以渲染文本。
* **pygame.font.Font.size()**
    确定多大的空间用于表示文本
    `size(text) -> (width, height)`

    该函数返回渲染文本所需要的尺寸。这可以被用于在文本显示之前，确定文本的显示位置。当然也有助于实现自动换行和其他布局效果。

    注意：大多数字体使用字距调整来调整指定字母间的宽度。例如，“ae” 的宽度并不总是等同于 ‘a’ + ‘e’ 的宽度。

* **pygame.font.Font.set_underline()**
    控制文本是否用下划线渲染
    `set_underline(bool) -> None`

    启用后，所有字体的渲染都会包含下划线。下划线一般是和一个像素点一样细，与字体尺寸无关。

    该函数可以与粗体和斜体模式混合使用。

* **pygame.font.Font.get_underline()**
    检查文本是否绘制下划线
    `get_underline() -> bool`

    如果字体下划线被启用，返回 True。

* **pygame.font.Font.set_bold()**
    启动粗体字渲染
    `set_bold(bool) -> None`

    该函数启用文本的粗体渲染。该函数是通过虚拟拉伸实现加粗，对大多数字体格式来说并不是很好看。如果可能，请加载真粗体格式的字体文件。当渲染的字体为粗体时，该字体将比普通模式下更宽一些。

    该函数可以和斜体及下划线模式混合使用。

* **pygame.font.Font.get_bold()**
    检查文本是否使用粗体渲染
    `get_bold() -> bool`

    如果字体的粗体渲染模式被启用，返回 True。

* **pygame.font.Font.set_italic()**
    启动斜体字渲染
    `set_italic(bool) -> None`

    该函数启用文本的斜体渲染。该函数是通过虚拟倾斜字体实现斜体，对大多数字体格式来说并不是很好看。如果可能，请加载真斜体格式的字体文件。当渲染的字体为斜体时，该字体将比普通模式下更宽一些。

    该函数可以和粗体及下划线模式混合使用。

* **pygame.font.Font.metrics()**
    获取字符串参数每个字符的参数
    `metrics(text) -> list`

    返回一个列表，包含每个字符的属性元组。形式如：[(minx, maxx, miny, maxy, advance), (minx, maxx, miny, maxy, advance), …]
    列表内不可识别的字符对应的元组内参数均为 None。

* **pygame.font.Font.get_italic()**
    检查文本是否使用斜体渲染
    `get_italic() -> bool`

    如果字体的斜体渲染模式被启用，返回 True。

* **pygame.font.Font.get_linesize()**
    获取字体文本的行高
    `get_linesize() -> int`

    返回该字体下文本的单行的高度（以像素为单位）。

    当需要渲染很多行文本时，推荐使用该返回值作为行间距。

* **pygame.font.Font.get_height()**
    获取字体的高度
    `get_height() -> int`

    返回实际渲染的文本的高度（以像素为单位）。

    返回值是字体内每个字符的平均规格。

* **pygame.font.Font.get_ascent()**
    获取字体顶端到基准线的距离
    `get_ascent() -> int`

    获取字体顶端到基准线的距离（以像素为单位）。

* **pygame.font.Font.get_descent()**
    获取字体底端到基准线的距离
    `get_descent() -> int`

    获取字体底端到基准线的距离（以像素为单位）





#### Surface 对象
* **创建Surface对象**
    - `my_surface = pygame.Surface(size) # 三通道`
    - `my_surface = pygame.Surface(size, pygame.SRCALPHA) # 四通道（alpha）`
* **填充颜色**
    `my_surface.fill(color)` color 是元组
* **方法**
    - `get_size()` 返回尺寸


#### pygame.draw 绘制图形
* **pygame.draw.rect**
    用法：pygame.draw.rect(Surface, color, Rect, width=0)

    pygame.draw.rect在surface上画一个矩形，除了surface和color，rect接受一个矩形的坐标和线宽参数，如果线宽是0或省略，则填充。我们有一个另外的方法来画矩形——fill方法，如果你还记得的话。事实上fill可能还会快一点点，因为fill由显卡来完成。

* **pygame.draw.polygon**
    用法：pygame.draw.polygon(Surface, color, pointlist, width=0)

    polygon就是多边形，用法类似rect，第一、第二、第四的参数都是相同的，只不过polygon会接受一系列坐标的列表，代表了各个顶点。

* **pygame.draw.circle**
    用法：pygame.draw.circle(Surface, color, pos, radius, width=0)

    很简单，画一个圆。与其他不同的是，它接收一个圆心坐标和半径参数。

* **pygame.draw.ellipse**
    用法：pygame.draw.ellipse(Surface, color, Rect, width=0)

    你可以把一个ellipse想象成一个被压扁的圆，事实上，它是可以被一个矩形装起来的。pygame.draw.ellipse的第三个参数就是这个椭圆的外接矩形。

* **pygame.draw.arc**
    用法：pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1)

    arc是椭圆的一部分，所以它的参数也就比椭圆多一点。但它是不封闭的，因此没有fill方法。start_angle和stop_angle为开始和结束的角度。

* **pygame.draw.line**
    用法：pygame.draw.line(Surface, color, start_pos, end_pos, width=1)

* **pygame.draw.lines**
    用法：pygame.draw.lines(Surface, color, closed, pointlist, width=1)

    closed是一个布尔变量，指明是否需要多画一条线来使这些线条闭合（感觉就和polygone一样了），pointlist是一个点的数组。

> 除了上面这些，还有aaline和aalines，玩游戏的都知道开出“抗锯齿（antialiasing）”效果会让画面更好看一些，模型的边就不会是锯齿形的了，这两个方法就是在画线的时候做这事情的，参数和上面一样，省略。


以下是关于 Pygame 中图片操作的笔记补充，涵盖了加载图片和缩放图片的内容：

### 图片

#### 加载图片
在 Pygame 中，可以使用 `pygame.image.load()` 函数从文件加载图片，返回一个 `pygame.Surface` 对象，该对象可以直接用于绘制到屏幕上。

- **基本用法**：
  ```python
  import pygame

  # 加载图片
  image = pygame.image.load("path/to/image.png")
  ```

- **注意事项**：
  - **文件路径**：确保路径正确，可以使用绝对路径或相对路径。如果使用相对路径，路径是相对于当前工作目录的。
  - **支持格式**：Pygame 支持多种图片格式，如 PNG、JPEG、BMP、GIF 等。推荐使用 PNG，因为它支持透明度。
  - **错误处理**：如果图片加载失败，Pygame 会抛出 `pygame.error` 异常，建议添加异常处理：
    ```python
    try:
        image = pygame.image.load("path/to/image.png")
    except pygame.error as e:
        print(f"无法加载图片: {e}")
        image = None  # 或者设置默认图片
    ```

- **绘制图片**：
  加载后的图片可以通过 `blit()` 方法绘制到屏幕或其他表面上：
  ```python
  screen = pygame.display.set_mode((800, 600))
  screen.blit(image, (x, y))  # 在位置 (x, y) 绘制图片
  ```

- **透明度支持**：
  如果图片（如 PNG）包含透明区域，Pygame 会自动处理透明效果，无需额外设置。

#### 缩放图片
在 Pygame 中，可以使用 `pygame.transform.scale()` 函数对图片进行缩放，以适应不同的显示尺寸。

- **基本用法**：
  ```python
  import pygame

  # 加载原始图片
  original_image = pygame.image.load("path/to/image.png")
  # 缩放到指定尺寸 (new_width, new_height)
  scaled_image = pygame.transform.scale(original_image, (new_width, new_height))
  ```

- **注意事项**：
  - **尺寸指定**：`pygame.transform.scale()` 的第二个参数是一个元组 `(width, height)`，表示目标宽度和高度。
  - **宽高比问题**：直接指定目标尺寸可能会导致图片变形（宽高比不一致）。如果需要保持宽高比，可以手动计算合适的尺寸：
    ```python
    original_width, original_height = original_image.get_size()
    target_width, target_height = 800, 600  # 目标区域尺寸
    aspect_ratio = original_width / original_height
    if aspect_ratio > target_width / target_height:
        # 图片比目标区域宽，按高度缩放
        new_height = target_height
        new_width = int(new_height * aspect_ratio)
    else:
        # 图片比目标区域高，按宽度缩放
        new_width = target_width
        new_height = int(new_width / aspect_ratio)
    scaled_image = pygame.transform.scale(original_image, (new_width, new_height))
    # 计算居中位置
    pos_x = (target_width - new_width) // 2
    pos_y = (target_height - new_height) // 2
    screen.blit(scaled_image, (pos_x, pos_y))
    ```

- **其他缩放方法**：
  - `pygame.transform.smoothscale()`：提供更平滑的缩放效果，但可能会比 `scale()` 慢一些。用法与 `scale()` 相同：
    ```python
    scaled_image = pygame.transform.smoothscale(original_image, (new_width, new_height))
    ```

- **性能考虑**：
  - 缩放操作是计算密集型的，建议在程序初始化时一次性完成缩放，而不是在游戏循环中频繁调用。
  - 如果图片尺寸非常大，考虑使用图像编辑工具预先调整图片大小，以减少运行时开销。

- **其他变换**：
  除了缩放，Pygame 还提供了其他图像变换方法，如旋转、翻转等：
  - 旋转：`pygame.transform.rotate(image, angle)`，`angle` 是旋转角度（度数），逆时针旋转。
  - 翻转：`pygame.transform.flip(image, flip_x, flip_y)`，`flip_x` 和 `flip_y` 是布尔值，分别表示是否水平和垂直翻转。
