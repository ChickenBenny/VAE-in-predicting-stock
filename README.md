# VAE-LSTM in stock prediction
### Project的出發點
我認為台灣的股票市場為非效率市場假說，股票市場有太多的內線消息、投資人情緒及有心人士拉盤等狀況。假若測股票市場是由多個分布所組成的混和分布，若能找到方式有效的解析股市分布和特徵，便能有效股市進行預測。

### 重點整理
此Project的重點會放在透過深度學行的模型，對特徵進行萃取，得出一個能表示股市分布的特徵向量，並利用該特徵向量進行股市的預測。(後續若有時間會做對萃取的特徵進行拆解的project)

1. 比較PCA和AutoEncoder的降維效果
2. 比較AutoEncoer和Variational Autoencoder在萃取特徵上的表現
3. 比較AE+LSTM、VAE+LSTM和LSTM在預測股市上的表現

![](https://i.imgur.com/YTJ7ex1.png)

**Notice: 模型皆未調整超參數，主要研究VAE對預測結果的影響**
### 資料
此Porject的data為台積電2010-2021年的資料。
特徵:
1. 個股每日資訊
2. 外幣資訊
3. 相關產業股票資訊(e.g. 聯發科、三星、英特爾等等)
4. 技術指標
5. 三大法人交易資訊

### PCA和AutoEncoder的降維比較
PCA和AutoEncoder這兩個方法，大家因該都是耳熟能詳。兩者的差異在於PCA是使用線性變換的方式，透過乘上一個矩陣，組合出能夠最有效區分所有資訊的特徵。而AutoEncoder的則是使用兩個對稱的NN模型，對原始資料進行編碼再還原，找出能夠最大限度降低information loss的Encoder和Decoder。

![](https://i.imgur.com/OSja9d3.png)

#### PCA其實是狹義版的AutoEncoder
在數學上線性其實是非線性的特例，假若今天我們使用一層的Enocder和Decoder，並且Activation function選擇使用線性的(y = x)，在適當的訓練下我們的AutoEncoder會達到與PCA相同的效果。

#### 線性降維較非線降維有更多的information loss

![](https://i.imgur.com/U8QrGSs.png)

實驗將分成兩個部分，如下:
1. 創建出一個有2個feature的函式，分別透過PCA和AE將其維度降至一維，在重建特徵。藉此去比較線性和非線性再進行維度下降時，比較哪種方式能夠保有較多的資訊。
2. 創建出一個有3個feature的函式，一樣透過線性跟非線性的方式降至二維，比較在較高維度進行降維時的效果差異。

*Notice: 詳細過程可以去看PCAvsAEdemo的Notebook*
* 2個特徵的實驗結果

![](https://i.imgur.com/f3AA99S.png)
* 3個特徵的實驗結果
![](https://i.imgur.com/tjXGCF4.png)


### AE和VAE的比較
Autoencoder的概念是將高維的特徵，轉換到一個能代表該特徵特性的空間上，而這空間上的向量我們稱作維特徵向量。但有一個大問題便是，AutoEncoder在沒有特殊的限制下，往往會有Overfitting的狀況，因此VAE改良了此特性，在訓練時強制Enocder產生出一個空間分布，而這個空間分布要能最好的映射到原始的分布，藉此降低Overfitting的狀況。(大家可以把VAE當作是AE+正規化)
如果大家有興趣可以參考:
1. 原始論文 : https://arxiv.org/abs/1312.6114
2. https://medium.com/towards-data-science/difference-between-autoencoder-ae-and-variational-autoencoder-vae-ed7be1c038f2
3. https://medium.com/towards-data-science/understanding-variational-autoencoders-vaes-f70510919f73

### 實驗結果
有興趣的可以去看stock_prediction的Notebook。

預測準確度比較(我們這邊單純以隔天上漲為1和下跌為-1，針對模型沒看過的testing data進行Accuracy的比較)
![](https://i.imgur.com/K8XH9FI.png)

### 結論
1. VAE確實能夠對特徵萃取有正向的影響，假設台股真的為非效率市場假說，那麼去解析特徵是很有可能從中找尋出更佳的預測特徵。
2. VAE在時間序列的資料能有效地防止Overfitting的狀況產生。
