from sklearn.model_selection import GridSearchCV

stregr = StackingRegressor(regressors = [gb,xgbr,rfr,extr],
                           meta_regressor = gbr)

params={
    'meta_regressor__n_estimators': [4800],
    'meta_regressor__learning_rate': [0.04127859055165332],
    'meta_regressor__max_depth': [3],
    'meta_regressor__subsample': [0.5],
    'meta_regressor__max_features': ['sqrt'],

    'gradientboostingregressor__n_estimators': [4800],
    'gradientboostingregressor__learning_rate': [0.04127859055165332],
    'gradientboostingregressor__max_depth': [3],
    'gradientboostingregressor__subsample': [0.5],
    'gradientboostingregressor__max_features': ['sqrt'],

    'randomforestregressor__n_estimators': [2000],
    'randomforestregressor__max_leaf_nodes': [291],
    'randomforestregressor__max_depth': [14],

    'extratreesregressor__n_estimators': [1100],
    'extratreesregressor__max_leaf_nodes': [867],
    'extratreesregressor__max_depth': [18],

    'xgbregressor__lambda': [0.10252576383026227],
    'xgbregressor__alpha': [0.43737951603549957],
    'xgbregressor__colsample_bytree': [0.9],
    'xgbregressor__subsample': [0.8],
    'xgbregressor__learning_rate': [0.018],
    'xgbregressor__n_estimators': [1400],
    'xgbregressor__max_depth': [13],
    'xgbregressor__min_child_weight': [35]
}

grid = GridSearchCV(estimator = stregr,
                    param_grid=params,
                    cv=KFold(n_splits=3,shuffle=True),
                    refit=True,
                    verbose=1,
                    n_jobs=-1,
                    scoring="neg_mean_squared_error")

grid.fit(train_data_rbs, train_target)
grid_best = grid.best_estimator_
