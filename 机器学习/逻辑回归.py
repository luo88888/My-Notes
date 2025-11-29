import numpy as np
from typing import Literal, Optional


class LogisticRegression:
    """
    逻辑回归（二分类）
    支持 L1 / L2 正则化、mini-batch 梯度下降
    最好对数据进行标准化，否则效果可能非常差
    """
    
    def __init__(
        self,
        learning_rate: float = 0.01,
        max_iter: int = 1000,
        batch_size: int = 32,
        tol: float = 1e-4,  # 早停阈值，如果连续几轮的损失变化小于这个值，则停止训练
        regularizer: Literal[None, 'l1', 'l2'] = 'l2',
        lambda_: float = 0.01,          # 正则化强度（C = 1/lambda）
        random_state: Optional[int] = None,
        verbose: bool = False           # 是否打印训练过程
    ):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.batch_size = batch_size
        self.tol = tol
        self.regularizer = regularizer
        self.lambda_ = lambda_
        self.random_state = random_state
        self.verbose = verbose
        
        # 将在 fit 时初始化
        self.w = None   # np.ndarray, shape = (n_features,)
        self.b = None   # float
        self.n_features = None
        
        if random_state is not None:
            np.random.seed(random_state)
    
    @staticmethod
    def _sigmoid(z: np.ndarray) -> np.ndarray:
        """数值稳定的 sigmoid 函数"""
        # 防止溢出：当 z 很大时直接返回 1，小则返回 0
        z = np.clip(z, -30, 30)
        return 1.0 / (1.0 + np.exp(-z))
    
    def _compute_loss(self, y: np.ndarray, y_hat: np.ndarray) -> float:
        """计算平均交叉熵损失（不含正则化项）
        Args:
            y: 真实标签，shape = (n_samples,)，值为 0 或 1
            y_hat: 预测概率，shape = (n_samples,)，值应在 [0, 1] 区间
        Returns:
            loss: 平均交叉熵损失（标量）
        """
        eps = 1e-15
        # 将预测概率裁剪到 [eps, 1 - eps] 避免 log(0)
        y_hat_clipped = np.clip(y_hat, eps, 1 - eps)
        loss = -np.mean(y * np.log(y_hat_clipped) + (1 - y) * np.log(1 - y_hat_clipped))
        return loss
    
    def _compute_regularization(self) -> float:
        """计算正则化惩罚值（用于监控）"""
        if self.regularizer == 'l2':
            return 0.5 * self.lambda_ * np.sum(self.w ** 2)
        elif self.regularizer == 'l1':
            return self.lambda_ * np.sum(np.abs(self.w))
        return 0.0
    
    def _compute_gradient(
        self, 
        X_batch: np.ndarray, 
        y_batch: np.ndarray
    ) -> tuple[np.ndarray, float]:
        """计算一个 batch 的梯度（含正则化）
        Args:
            X_batch: 特征矩阵，shape = (batch_size, n_features)
            y_batch: 真实标签，shape = (batch_size,)，值为 0 或 1
        Returns:
            grad_w: 梯度，shape = (n_features,)
            grad_b: 梯度，shape = (1,)
        """
        n_batch = len(y_batch)
        # (batch_size, n_features) @ (n_features, 1) + scalar = (batch_size, 1)
        z = X_batch @ self.w + self.b
        y_hat = self._sigmoid(z)
        error = y_hat - y_batch                     # (batch_size, 1)
        # (n_features, batch_size) @ (batch_size, 1) = (n_features, 1)
        grad_w = (X_batch.T @ error) / n_batch      # (n_features, 1)
        grad_b = np.mean(error)                     # scalar
        
        # 添加正则化梯度（注意：不对 bias 进行正则化）
        if self.regularizer == 'l2':
            grad_w += self.lambda_ * self.w
        elif self.regularizer == 'l1':
            # L1 的次梯度：sign(w)
            grad_w += self.lambda_ * np.sign(self.w)
        
        return grad_w, grad_b
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        训练模型
        X: shape = (n_samples, n_features)
        y: shape = (n_samples,)，值为 0 或 1
        """
        X = np.asarray(X, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)
        
        if X.ndim != 2 or y.ndim != 1:
            raise ValueError("X 必须是 2 维数组，y 必须是 1 维数组")
        if X.shape[0] != y.shape[0]:
            raise ValueError("样本数量不匹配")
        if not np.all(np.isin(y, [0, 1])):
            raise ValueError("y 必须只包含 0 和 1（二分类）")
        
        n_samples, self.n_features = X.shape
        
        # 参数初始化（常用 Xavier / Glorot 初始化）
        self.w = np.random.randn(self.n_features) * np.sqrt(2.0 / self.n_features)
        self.b = 0.0
        
        prev_loss = np.inf
        
        for iteration in range(1, self.max_iter + 1):
            # Shuffle 数据（mini-batch）
            indices = np.random.permutation(n_samples)
            X_shuffled = X[indices]
            y_shuffled = y[indices]
            
            for start in range(0, n_samples, self.batch_size):
                end = start + self.batch_size
                X_batch = X_shuffled[start:end] # end 越界不会出错，会自动截断
                y_batch = y_shuffled[start:end]
                
                grad_w, grad_b = self._compute_gradient(X_batch, y_batch)
                
                # 参数更新
                self.w -= self.learning_rate * grad_w
                self.b -= self.learning_rate * grad_b
            
            # 每轮结束后计算整体损失，用于早停判断
            if iteration % 10 == 0 or iteration == self.max_iter:
                y_hat = self._sigmoid(X @ self.w + self.b)
                loss = self._compute_loss(y, y_hat) + self._compute_regularization()
                
                if self.verbose:
                    print(f"Iter {iteration:4d} | Loss: {loss:.6f}")
                
                # 早停
                if np.abs(prev_loss - loss) < self.tol:
                    if self.verbose:
                        print(f"收敛于第 {iteration} 轮")
                    break
                prev_loss = loss
        
        return self
    
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """返回正类（y=1）的概率，shape = (n_samples,)"""
        X = np.asarray(X, dtype=np.float64)
        if X.shape[1] != self.n_features:
            raise ValueError(f"特征数量不匹配，期望 {self.n_features}，得到 {X.shape[1]}")
        
        z = X @ self.w + self.b
        return self._sigmoid(z)
    
    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """返回类别标签 0/1
        Args:
            X: 特征矩阵，shape = (n_samples, n_features)
            threshold: 阈值，默认为 0.5，大于等于该值的为 1，否则为 0
        Returns:
            y_pred: 类别标签，shape = (n_samples,)，值为 0 或 1
        """
        prob = self.predict_proba(X)
        return (prob >= threshold).astype(int)
    
    def get_params(self) -> dict:
        """返回训练好的参数"""
        return {"w": self.w.copy(), "b": self.b}



if __name__ == "__main__":
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, log_loss
    
    # 生成数据
    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, 
                               n_informative=15, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 训练模型
    model = LogisticRegression(
        learning_rate=0.1,
        max_iter=1000,
        batch_size=32,
        regularizer='l2',
        lambda_=0.01,
        verbose=True,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Log Loss:", log_loss(y_test, y_prob))