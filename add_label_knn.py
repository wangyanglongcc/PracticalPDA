import pandas as pd
import os
from sklearn.model_selection import train_test_split,GridSearchCV,StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import warnings
warnings.filterwarnings('ignore')

def knn(save_model=True):
    path = r'E:\打标'
    df = pd.read_excel(os.path.join(path,'商品打标模型分类数据源.xlsx'),skiprows=1)
    df = pd.get_dummies(df,columns=['isexceedavg_returngoods'])
    df = pd.get_dummies(df,columns=['isexceedavg_reputation'])
    df = pd.get_dummies(df,columns=['isprefect'])
    # df['label'] = df['label'].replace(df['label'].unique(),list(range(df['label'].unique().size)))
    df = df.drop(['commoditycode','customcategoryname'],1)
    X = df.drop('label',1).values
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    Y = df['label'].values
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state = 1116)
    clf = KNeighborsClassifier()
    param_grid = {
        'n_neighbors':range(1,10),
        'weights':['uniform','distance'],
        'algorithm':['auto','kd_tree','ball_tree','brute'],
        'leaf_size':range(10,50,5),
        'p':[1,2]
    }
    kfold = StratifiedKFold(n_splits=10,random_state=1116)
    grid_cv = GridSearchCV(clf,param_grid,scoring='accuracy',n_jobs=1,cv=kfold)
    grid_cv.fit(x_train,y_train)
    best_model = grid_cv.best_estimator_
    print(grid_cv.best_score_)
    print(grid_cv.best_params_)
    if save_model:
        joblib.dump(best_model,'knn.model')

if __name__ == '__main__':
    knn()