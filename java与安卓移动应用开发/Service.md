## Service

### 1 Service 简介

Service 是 Android 系统中用于处理长时间运行任务的组件之一，它没有用户界面，通常在后台运行。Service 适用于执行不需要用户交互的操作，例如播放音乐、下载文件、监听系统事件等。

**主要特点**：
- **后台运行**：Service 在后台运行，不直接与用户交互。
- **持久性**：即使启动它的 Activity 被销毁，Service 通常仍会继续运行（除非被明确停止）。
- **组件通信**：可以与其他组件（如 Activity）通过绑定机制进行通信。

**分类**：
- **Started Service**：通过 `startService()` 启动，执行一次性任务，需手动停止。
- **Bound Service**：通过 `bindService()` 启动，允许多个组件绑定并与之交互，通常用于需要返回数据的场景。
- **Foreground Service**：在前台运行，显示通知，用户可见，常用于重要任务（如音乐播放）。
- **IntentService**：一种特殊的 Service，适用于处理耗时任务，自动管理线程和任务队列。

**应用场景**：
- 后台音乐播放
- 文件下载或上传
- 定时任务或监听系统事件

---

### 2 Service 的创建和声明

#### 2.1 创建 Service
要创建一个 Service，需要继承 `Service` 类，并重写关键的生命周期方法（如 `onCreate()`、`onStartCommand()` 等）。

**基本代码示例**：
```java
public class MyService extends Service {
    @Override
    public void onCreate() {
        super.onCreate();
        // 初始化操作
        Log.d("MyService", "Service Created");
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        // 处理任务逻辑
        Log.d("MyService", "Service Started");
        return START_STICKY; // 服务被系统杀死后尝试重启
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        // 清理资源
        Log.d("MyService", "Service Destroyed");
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        // 如果是绑定服务，返回 IBinder 对象
        return null;
    }
}
```

#### 2.2 声明 Service
Service 必须在 `AndroidManifest.xml` 文件中声明，以便系统识别。

**声明示例**：
```xml
<service
    android:name=".MyService"
    android:enabled="true"
    android:exported="false" />
```
- `android:name`：指定 Service 类的完整路径。
- `android:enabled`：是否启用 Service，默认为 `true`。
- `android:exported`：是否允许其他应用访问，设为 `false` 表示仅本应用可用。

如果 Service 需要被其他应用访问（例如通过隐式 Intent），需设置 `exported="true"` 并定义 Intent Filter。

---

### 3 Service 的运行与停止

#### 3.1 启动 Service
Service 可以通过 `startService()` 方法启动，通常使用 Intent 指定目标 Service。

**代码示例**：
```java
Intent intent = new Intent(this, MyService.class);
startService(intent);
```

- 启动后，Service 会调用 `onCreate()`（首次创建时）和 `onStartCommand()` 方法。
- 如果 Service 已经在运行，则只会调用 `onStartCommand()`。

#### 3.2 停止 Service
Service 可以通过以下方式停止：
- **手动停止**：调用 `stopService()` 方法。
- **自我停止**：Service 内部调用 `stopSelf()` 方法。

**代码示例**：
```java
// 外部停止 Service
Intent intent = new Intent(this, MyService.class);
stopService(intent);

// Service 内部停止
stopSelf();
```

**注意**：
- 如果 Service 同时被启动和绑定，只有在所有绑定断开且未通过 `startService()` 启动时才会销毁。
- 前台服务需要调用 `stopForeground(true)` 停止前台状态。

---

### 4 Service 的生命周期

Service 的生命周期根据启动方式不同而有所差异，主要分为两种模式：启动模式（Started）和绑定模式（Bound）。

#### 4.1 Started Service 生命周期
- **onCreate()**：Service 首次创建时调用，用于初始化资源。只调用一次。
- **onStartCommand(Intent intent, int flags, int startId)**：每次通过 `startService()` 启动时调用，处理任务逻辑。
  - 返回值决定系统杀死 Service 后的行为：
    - `START_STICKY`：系统尝试重启 Service，但不保留 Intent。
    - `START_NOT_STICKY`：不重启。
    - `START_REDELIVER_INTENT`：重启并传递原始 Intent。
- **onDestroy()**：Service 被销毁时调用，用于清理资源。

**生命周期流程**：
`onCreate()` -> `onStartCommand()` -> `onDestroy()`

#### 4.2 Bound Service 生命周期
- **onCreate()**：同上。
- **onBind(Intent intent)**：当组件通过 `bindService()` 绑定到 Service 时调用，返回 IBinder 对象用于通信。
- **onUnbind(Intent intent)**：当所有绑定断开时调用，处理清理工作。
- **onDestroy()**：同上。

**生命周期流程**：
`onCreate()` -> `onBind()` -> `onUnbind()` -> `onDestroy()`

**注意**：
- 如果 Service 同时被启动和绑定，必须两者都结束（停止启动状态和解除所有绑定）才会销毁。

---

### 5 绑定服务

绑定服务（Bound Service）允许组件（如 Activity）与 Service 建立连接并进行双向通信。绑定服务通常用于需要返回数据或持续交互的场景。

#### 5.1 绑定服务的实现方式
绑定服务需要通过 `bindService()` 方法启动，并使用 `Binder` 机制实现通信。

**步骤**：
1. 在 Service 中创建 `Binder` 对象，用于返回给客户端。
2. 在 `onBind()` 方法中返回 `Binder` 对象。
3. 在客户端通过 `ServiceConnection` 监听绑定状态并获取 `Binder` 对象。

**代码示例**：
```java
public class MyBoundService extends Service {
    private final IBinder binder = new LocalBinder();

    public class LocalBinder extends Binder {
        MyBoundService getService() {
            return MyBoundService.this;
        }
    }

    @Override
    public IBinder onBind(Intent intent) {
        return binder;
    }

    public String getData() {
        return "Data from Service";
    }
}

// 在 Activity 中绑定 Service
public class MainActivity extends AppCompatActivity {
    private MyBoundService boundService;
    private boolean isBound = false;

    private ServiceConnection connection = new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            MyBoundService.LocalBinder binder = (MyBoundService.LocalBinder) service;
            boundService = binder.getService();
            isBound = true;
        }

        @Override
        public void onServiceDisconnected(ComponentName name) {
            isBound = false;
        }
    };

    @Override
    protected void onStart() {
        super.onStart();
        Intent intent = new Intent(this, MyBoundService.class);
        bindService(intent, connection, Context.BIND_AUTO_CREATE);
    }

    @Override
    protected void onStop() {
        super.onStop();
        if (isBound) {
            unbindService(connection);
            isBound = false;
        }
    }
}
```

#### 5.2 注意事项
- 绑定服务默认不会创建 Service，只有在首次绑定时才会创建。
- 使用 `Context.BIND_AUTO_CREATE` 标志可以自动创建 Service。
- 当所有客户端解除绑定后，Service 会销毁（除非它也被 `startService()` 启动）。

---

### 6 IntentService

`IntentService` 是 `Service` 的一个子类，专门用于处理耗时任务，具有以下特点：
- **自动线程管理**：IntentService 在单独的工作线程中处理任务，避免阻塞主线程。
- **任务队列**：按顺序处理 Intent 请求，处理一个 Intent 后才会处理下一个。
- **自动停止**：任务完成后自动调用 `stopSelf()` 停止服务。

#### 6.1 使用 IntentService
需要继承 `IntentService` 并重写 `onHandleIntent()` 方法来处理任务逻辑。

**代码示例**：
```java
public class MyIntentService extends IntentService {
    public MyIntentService() {
        super("MyIntentService"); // 指定线程名称
    }

    @Override
    protected void onHandleIntent(@Nullable Intent intent) {
        // 在工作线程中处理任务
        if (intent != null) {
            String data = intent.getStringExtra("data");
            Log.d("MyIntentService", "Handling data: " + data);
            // 模拟耗时操作
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

// 启动 IntentService
Intent intent = new Intent(this, MyIntentService.class);
intent.putExtra("data", "Task Data");
startService(intent);
```

#### 6.2 注意事项
- `IntentService` 不支持绑定，无法通过 `bindService()` 使用。
- 每个 Intent 按顺序处理，适合处理离散的耗时任务（如下载多个文件）。
- 不能在 `onHandleIntent()` 中直接更新 UI，需通过 Handler 或广播通知 UI 线程。
