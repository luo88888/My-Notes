## Intent

### 1 Intent 简介

Intent 是 Android 系统中用于组件间通信的重要机制。它是一个抽象的描述，表明要执行的操作，通常用于启动 Activity、Service 或 Broadcast Receiver 等组件。Intent 可以携带数据，并通过它在不同的组件之间传递信息。

Intent 的主要作用包括：
- **组件间通信**：在 Activity、Service、Broadcast Receiver 之间传递消息或启动组件。
- **数据传递**：通过 Intent 携带数据（如字符串、对象等）在组件间共享。
- **系统交互**：与系统或其他应用程序交互，例如打开浏览器、拨打电话等。

Intent 分为两种类型：**显示 Intent** 和 **隐式 Intent**，分别用于明确指定目标组件和通过动作匹配目标组件。

---

### 2 Intent 相关属性

Intent 包含以下核心属性（也称为 Intent 的组成部分）：
- **Action**：指定 Intent 要执行的操作，例如 `ACTION_VIEW`（查看数据）、`ACTION_SEND`（分享数据）。可以通过 `setAction()` 设置。
- **Data**：与 Action 相关的具体数据，通常以 URI 形式表示，例如网页链接或文件路径。可以通过 `setData()` 设置。
- **Category**：为 Action 提供附加分类信息，例如 `CATEGORY_DEFAULT`。可以通过 `addCategory()` 添加。
- **Type**：指定 Intent 的 MIME 类型，用于明确数据类型。可以通过 `setType()` 设置。
- **Component**：明确指定目标组件的类名，用于显示 Intent。可以通过 `setComponent()` 或 `setClass()` 设置。
- **Extras**：附加数据，以键值对形式存储，可以传递各种类型的数据。可以通过 `putExtra()` 添加。
- **Flags**：控制 Intent 的行为，例如是否清除任务栈（`FLAG_ACTIVITY_CLEAR_TOP`）。可以通过 `setFlags()` 设置。

这些属性共同定义了 Intent 的行为和目标，帮助系统找到合适的组件来处理请求。

---

### 3 显示 Intent

显示 Intent（Explicit Intent）是指明确指定目标组件的 Intent，通常用于在同一应用内启动已知的 Activity、Service 或 Broadcast Receiver。

**特点**：
- 目标组件通过 `ComponentName` 或直接指定类名来确定。
- 适用于应用内部组件间的通信，效率高且安全性较好。

**用法**：
- 通过构造函数 `Intent(Context packageContext, Class<?> cls)` 创建。
- 或者使用 `setClass()` 或 `setComponent()` 指定目标组件。

**示例**：
```java
Intent intent = new Intent(this, SecondActivity.class);
startActivity(intent);
```

---

### 4 隐式 Intent

隐式 Intent（Implicit Intent）不指定具体的目标组件，而是通过 Action、Data、Category 等属性描述要执行的操作，由系统根据 Intent Filter 匹配适合的组件来处理。

**特点**：
- 适用于与系统或其他应用交互，例如打开浏览器、发送邮件。
- 需要在 `AndroidManifest.xml` 中为目标组件定义 `<intent-filter>` 来匹配隐式 Intent。
- 可能存在多个组件匹配的情况，系统会弹出选择对话框。

**用法**：
- 通过设置 `Action` 和其他属性来描述操作。
- 使用 `startActivity()` 或其他方法启动。

**示例**：
```java
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setData(Uri.parse("https://www.google.com"));
startActivity(intent);
```

**注意事项**：
- 隐式 Intent 可能因没有匹配组件而抛出 `ActivityNotFoundException`，建议使用 `resolveActivity()` 检查是否有匹配组件。
```java
if (intent.resolveActivity(getPackageManager()) != null) {
    startActivity(intent);
}
```

---

### 5 Intent 示例用法

#### 5.1 启动 Activity

Intent 最常见的用途是启动一个新的 Activity，可以通过显示或隐式 Intent 实现。

**显示 Intent 启动 Activity**：
```java
// 启动一个特定的 Activity
Intent intent = new Intent(this, SecondActivity.class);
// 传递数据
intent.putExtra("key", "Hello from MainActivity");
startActivity(intent);
```

**隐式 Intent 启动 Activity**：
```java
// 打开浏览器查看网页
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setData(Uri.parse("https://www.google.com"));
startActivity(intent);
```

**获取返回结果**：
使用 `startActivityForResult()` 启动 Activity，并在 `onActivityResult()` 中处理返回数据。
```java
// 启动 Activity 并期待返回结果
Intent intent = new Intent(this, SecondActivity.class);
startActivityForResult(intent, REQUEST_CODE);

// 处理返回结果
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == REQUEST_CODE && resultCode == RESULT_OK) {
        String result = data.getStringExtra("result_key");
        // 处理返回的数据
    }
}
```

#### 5.2 启动服务

Intent 也可以用于启动 Service，用于后台任务处理。

**显示 Intent 启动 Service**：
```java
Intent intent = new Intent(this, MyService.class);
startService(intent); // 启动服务
// 或者使用 bindService() 绑定服务
```

**隐式 Intent 启动 Service**（较少使用）：
需要在 `AndroidManifest.xml` 中为 Service 定义 Intent Filter。

**停止服务**：
```java
Intent intent = new Intent(this, MyService.class);
stopService(intent);
```

#### 5.3 传递广播

Intent 还可以用于发送广播，通知系统或应用内的其他组件。

**发送广播**：
```java
Intent intent = new Intent("com.example.CUSTOM_ACTION");
intent.putExtra("message", "This is a broadcast message");
sendBroadcast(intent);
```

**注册广播接收器**（动态注册）：
```java
BroadcastReceiver receiver = new BroadcastReceiver() {
    @Override
    public void onReceive(Context context, Intent intent) {
        String message = intent.getStringExtra("message");
        // 处理广播消息
    }
};
registerReceiver(receiver, new IntentFilter("com.example.CUSTOM_ACTION"));
```

**注意**：
- 从 Android 8.0 开始，静态注册的广播接收器对大多数隐式广播无效，建议使用动态注册或 `Context.sendBroadcast()`。
- 可以使用 `sendOrderedBroadcast()` 发送有序广播，控制接收顺序。
