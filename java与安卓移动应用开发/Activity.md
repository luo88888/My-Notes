## Activity

### Activity 的组成

### 运行周期

- **生命周期概述**：`Activity` 的生命周期是指从创建到销毁经历的各个阶段，理解这些阶段有助于管理资源和优化用户体验。
- **主要方法**：
  - **onCreate()**：Activity 创建时调用，用于初始化布局（通过 `setContentView()`）、绑定控件和设置初始数据，通常是生命周期的起点。
  - **onStart()**：Activity 变得可见时调用，用户可以看到界面，但还无法交互，常用于启动动画或准备资源。
  - **onResume()**：Activity 获得焦点并可与用户交互时调用，界面完全在前台，适合开启摄像头、监听器等实时功能。
  - **onPause()**：Activity 失去焦点时调用，通常是另一个 Activity 覆盖或部分遮挡，适合保存数据、暂停动画或关闭实时功能。
  - **onStop()**：Activity 完全不可见时调用，可能因被其他 Activity 覆盖或应用进入后台，适合释放较大资源（如数据库连接）。
  - **onDestroy()**：Activity 被销毁时调用，通常是用户关闭或系统回收资源，需释放所有资源（如取消定时器、关闭文件流）。

- **注意**：合理处理生命周期方法，避免内存泄漏和资源浪费，确保应用流畅运行。

### 创建 Activity 的步骤

1. **创建 java 文件和 xml 布局文件**
    - 创建一个新的 Java/Kotlin 类，继承 Activity 或 AppCompatActivity（推荐后者，兼容性更好）。
    ```java
    public class MyActivity extends AppCompatActivity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_my); // 关联布局文件
        }
    }
    ```
    - 在 res/layout 目录下创建一个对应的 XML 布局文件（如 activity_my.xml），定义用户界面。
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Hello, Activity!" />
    </LinearLayout>
    ```
2. **在 AndroidManifest.xml 中对 Activity 进行注册**
    - 在 `<application>` 标签内添加 `<activity>` 标签，指定 Activity 的名称。
    ```xml
    <activity
    android:name=".MyActivity"
    android:exported="false" />
    ```
    - 如果该 Activity 是应用的默认启动页面（主页面），需要添加 `<intent-filter>`
    ```xml {.line-numbers highlight=[4-7]}
    <activity
        android:name=".MyActivity"
        android:exported="true">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
    ```