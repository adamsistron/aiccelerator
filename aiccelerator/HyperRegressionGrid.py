"""
Initially built with the following code
----------------------------------
from lazypredict import Supervised
for algorithm_type in Supervised.REGRESSORS:
    try:
        algorithm = algorithm_type[1]().get_params()
        print(algorithm_type[0]+"_grid = {")
        for key in algorithm:
            if type(algorithm[key])== type(''):
                print("\t'{}': ['{}'],".format(key,algorithm[key]))
            else:
                print("\t'{}': [{}],".format(key,algorithm[key]))
        print('}')
    except:
        print("Error with "+algorithm_type[0])
----------------------------------
Then completed the dict values from reading the documentation of each model
"""

import numpy as np

AdaBoostRegressor_grid = {
	'base_estimator': [None],
	'learning_rate': [0.01,0.05,0.1,0.3,1],
	'loss': ['linear', 'square', 'exponential'],
	'n_estimators': [50, 100],
	'random_state': [None],
}

BaggingRegressor_grid = {
	'base_estimator': [None],
	'bootstrap': [True,False],
	'bootstrap_features': [True,False],
	'max_features': [1, 2, 4],
	'max_samples': [0.5, 1.0],
	'n_estimators': [5,10,20,50],
	'n_jobs': [-2],
	'oob_score': [True,False],
	'random_state': [None],
	'verbose': [0],
	'warm_start': [False],
}

BayesianRidge_grid = {
	'alpha_1': [1e-06],
	'alpha_2': [1e-06],
	'alpha_init': [None],
	'compute_score': [False],
	'copy_X': [True],
	'fit_intercept': [True,False],
	'lambda_1': [1e-06],
	'lambda_2': [1e-06],
	'lambda_init': [None],
	'n_iter': [300,500,1000],
	'normalize': [False],
	'tol': [0.001],
	'verbose': [False],
}

DecisionTreeRegressor_grid = {
	'ccp_alpha': [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035],
	'criterion': ['mse', 'friedman_mse', 'mae'],
	'max_depth': [None, 2, 'auto', 'sqrt', 'log2'],
	'max_features': [None],
	'max_leaf_nodes': [None],
	'min_impurity_decrease': [0.0],
	'min_impurity_split': [None],
	'min_samples_leaf': [2, 1, 0.5, 0.1],
	'min_samples_split': [2, 1, 0.5, 0.1],
	'min_weight_fraction_leaf': [2, 1, 0.5, 0.1, 0.0],
	'presort': ['deprecated'],
	'random_state': [None],
	'splitter': ['best','random'],
}

DummyRegressor_grid = {
	'constant': [None],
	'quantile': [0.0,0.8,1.0],
	'strategy': ['mean','median','quantile'],
}

ElasticNet_grid = {
	'alpha': [1e-06,0.1,0.5,1.0],
	'copy_X': [True],
	'fit_intercept': [True,False],
	'l1_ratio': [0.1,0.5,0.9],
	'max_iter': [300, 500, 1000],
	'normalize': [False],
	'positive': [False],
	'precompute': [False],
	'random_state': [None],
	'selection': ['cyclic','random'],
	'tol': [0.0001, 0.00001, 0.001],
	'warm_start': [False],
}

ElasticNetCV_grid = {
	'alphas': [None],
	'copy_X': [True],
	'cv': [None],
	'eps': [0.001],
	'fit_intercept': [True],
	'l1_ratio': [.1, .5, .7, .9, .95, .99, 1],
	'max_iter': [300, 500, 1000],
	'n_alphas': [100],
	'n_jobs': [-2],
	'normalize': [False],
	'positive': [False],
	'precompute': ['auto'],
	'random_state': [None],
	'selection': ['cyclic','random'],
	'tol': [0.0001, 0.00001, 0.001],
	'verbose': [0],
}
ExtraTreeRegressor_grid = {
	'ccp_alpha': [0.0],
	'criterion': ['mse','friedman_mse','mae'],
	'max_depth': [None],
	'max_features': ['auto','sqrt','log2'],
	'max_leaf_nodes': [None],
	'min_impurity_decrease': [0.0],
	'min_impurity_split': [None],
	'min_samples_leaf': [1],
	'min_samples_split': [2],
	'min_weight_fraction_leaf': [0.0],
	'random_state': [None],
	'splitter': ['random','best'],
}
ExtraTreesRegressor_grid = {
	'bootstrap': [False],
	'ccp_alpha': [0.0],
	'criterion': ['mse'],
	'max_depth': [None],
	'max_features': ['auto'],
	'max_leaf_nodes': [None],
	'max_samples': [None],
	'min_impurity_decrease': [0.0],
	'min_impurity_split': [None],
	'min_samples_leaf': [1],
	'min_samples_split': [2],
	'min_weight_fraction_leaf': [0.0],
	'n_estimators': [100],
	'n_jobs': [-2],
	'oob_score': [False],
	'random_state': [None],
	'verbose': [0],
	'warm_start': [False],
}
GammaRegressor_grid = {
	'alpha': [1.0],
	'fit_intercept': [True],
	'max_iter': [100],
	'tol': [0.0001],
	'verbose': [0],
	'warm_start': [False],
}
GaussianProcessRegressor_grid = {
	'alpha': [1e-10],
	'copy_X_train': [True],
	'kernel': [None],
	'n_restarts_optimizer': [0],
	'normalize_y': [False],
	'optimizer': ['fmin_l_bfgs_b'],
	'random_state': [None],
}
GeneralizedLinearRegressor_grid = {
	'alpha': [1.0],
	'family': ['normal'],
	'fit_intercept': [True],
	'link': ['auto'],
	'max_iter': [100],
	'solver': ['lbfgs'],
	'tol': [0.0001],
	'verbose': [0],
	'warm_start': [False],
}
GradientBoostingRegressor_grid = {
	'alpha': [0.9],
	'ccp_alpha': [0.0],
	'criterion': ['friedman_mse'],
	'init': [None],
	'learning_rate': [0.1],
	'loss': ['ls'],
	'max_depth': [3],
	'max_features': [None],
	'max_leaf_nodes': [None],
	'min_impurity_decrease': [0.0],
	'min_impurity_split': [None],
	'min_samples_leaf': [1],
	'min_samples_split': [2],
	'min_weight_fraction_leaf': [0.0],
	'n_estimators': [100],
	'n_iter_no_change': [None],
	'presort': ['deprecated'],
	'random_state': [None],
	'subsample': [1.0],
	'tol': [0.0001],
	'validation_fraction': [0.1],
	'verbose': [0],
	'warm_start': [False],
}
HistGradientBoostingRegressor_grid = {
	'early_stopping': ['auto'],
	'l2_regularization': [0.0],
	'learning_rate': [0.1],
	'loss': ['least_squares'],
	'max_bins': [255],
	'max_depth': [None],
	'max_iter': [100],
	'max_leaf_nodes': [31],
	'min_samples_leaf': [20],
	'monotonic_cst': [None],
	'n_iter_no_change': [10],
	'random_state': [None],
	'scoring': ['loss'],
	'tol': [1e-07],
	'validation_fraction': [0.1],
	'verbose': [0],
	'warm_start': [False],
}
HuberRegressor_grid = {
	'alpha': [0.0001],
	'epsilon': [1.35],
	'fit_intercept': [True],
	'max_iter': [100],
	'tol': [1e-05],
	'warm_start': [False],
}
KNeighborsRegressor_grid = {
	'algorithm': ['auto'],
	'leaf_size': [30],
	'metric': ['minkowski'],
	'metric_params': [None],
	'n_jobs': [-2],
	'n_neighbors': [5],
	'p': [2],
	'weights': ['uniform'],
}
KernelRidge_grid = {
	'alpha': [1],
	'coef0': [1],
	'degree': [3],
	'gamma': [None],
	'kernel': ['linear'],
	'kernel_params': [None],
}
Lars_grid = {
	'copy_X': [True],
	'eps': [2.220446049250313e-16],
	'fit_intercept': [True],
	'fit_path': [True],
	'jitter': [None],
	'n_nonzero_coefs': [500],
	'normalize': [True],
	'precompute': ['auto'],
	'random_state': [None],
	'verbose': [False],
}
LarsCV_grid = {
	'copy_X': [True],
	'cv': [None],
	'eps': [2.220446049250313e-16],
	'fit_intercept': [True],
	'max_iter': [500],
	'max_n_alphas': [1000],
	'n_jobs': [-2],
	'normalize': [True],
	'precompute': ['auto'],
	'verbose': [False],
}
Lasso_grid = {
	'alpha': [1.0],
	'copy_X': [True],
	'fit_intercept': [True],
	'max_iter': [1000],
	'normalize': [False],
	'positive': [False],
	'precompute': [False],
	'random_state': [None],
	'selection': ['cyclic'],
	'tol': [0.0001],
	'warm_start': [False],
}
LassoCV_grid = {
	'alphas': [None],
	'copy_X': [True],
	'cv': [None],
	'eps': [0.001],
	'fit_intercept': [True],
	'max_iter': [1000],
	'n_alphas': [100],
	'n_jobs': [-2],
	'normalize': [False],
	'positive': [False],
	'precompute': ['auto'],
	'random_state': [None],
	'selection': ['cyclic'],
	'tol': [0.0001],
	'verbose': [False],
}
LassoLars_grid = {
	'alpha': [1.0],
	'copy_X': [True],
	'eps': [2.220446049250313e-16],
	'fit_intercept': [True],
	'fit_path': [True],
	'jitter': [None],
	'max_iter': [500],
	'normalize': [True],
	'positive': [False],
	'precompute': ['auto'],
	'random_state': [None],
	'verbose': [False],
}
LassoLarsCV_grid = {
	'copy_X': [True],
	'cv': [None],
	'eps': [2.220446049250313e-16],
	'fit_intercept': [True],
	'max_iter': [500],
	'max_n_alphas': [1000],
	'n_jobs': [-2],
	'normalize': [True],
	'positive': [False],
	'precompute': ['auto'],
	'verbose': [False],
}
LassoLarsIC_grid = {
	'copy_X': [True],
	'criterion': ['aic'],
	'eps': [2.220446049250313e-16],
	'fit_intercept': [True],
	'max_iter': [500],
	'normalize': [True],
	'positive': [False],
	'precompute': ['auto'],
	'verbose': [False],
}
LinearRegression_grid = {
	'copy_X': [True],
	'fit_intercept': [True],
	'n_jobs': [-2],
	'normalize': [False],
}
LinearSVR_grid = {
	'C': [1.0],
	'dual': [True],
	'epsilon': [0.0],
	'fit_intercept': [True],
	'intercept_scaling': [1.0],
	'loss': ['epsilon_insensitive'],
	'max_iter': [1000],
	'random_state': [None],
	'tol': [0.0001],
	'verbose': [0],
}
MLPRegressor_grid = {
	'activation': ['relu'],
	'alpha': [0.0001],
	'batch_size': ['auto'],
	'beta_1': [0.9],
	'beta_2': [0.999],
	'early_stopping': [False],
	'epsilon': [1e-08],
	'hidden_layer_sizes': [(100,)],
	'learning_rate': ['constant'],
	'learning_rate_init': [0.001],
	'max_fun': [15000],
	'max_iter': [200],
	'momentum': [0.9],
	'n_iter_no_change': [10],
	'nesterovs_momentum': [True],
	'power_t': [0.5],
	'random_state': [None],
	'shuffle': [True],
	'solver': ['adam'],
	'tol': [0.0001],
	'validation_fraction': [0.1],
	'verbose': [False],
	'warm_start': [False],
}
NuSVR_grid = {
	'C': [1.0],
	'cache_size': [200],
	'coef0': [0.0],
	'degree': [3],
	'gamma': ['scale'],
	'kernel': ['rbf'],
	'max_iter': [-1],
	'nu': [0.5],
	'shrinking': [True],
	'tol': [0.001],
	'verbose': [False],
}
OrthogonalMatchingPursuit_grid = {
	'fit_intercept': [True],
	'n_nonzero_coefs': [None],
	'normalize': [True],
	'precompute': ['auto'],
	'tol': [None],
}
OrthogonalMatchingPursuitCV_grid = {
	'copy': [True],
	'cv': [None],
	'fit_intercept': [True],
	'max_iter': [None],
	'n_jobs': [-2],
	'normalize': [True],
	'verbose': [False],
}
PassiveAggressiveRegressor_grid = {
	'C': [1.0],
	'average': [False],
	'early_stopping': [False],
	'epsilon': [0.1],
	'fit_intercept': [True],
	'loss': ['epsilon_insensitive'],
	'max_iter': [1000],
	'n_iter_no_change': [5],
	'random_state': [None],
	'shuffle': [True],
	'tol': [0.001],
	'validation_fraction': [0.1],
	'verbose': [0],
	'warm_start': [False],
}
PoissonRegressor_grid = {
	'alpha': [1.0],
	'fit_intercept': [True],
	'max_iter': [100],
	'tol': [0.0001],
	'verbose': [0],
	'warm_start': [False],
}
RANSACRegressor_grid = {
	'base_estimator': [None],
	'is_data_valid': [None],
	'is_model_valid': [None],
	'loss': ['absolute_loss'],
	'max_skips': [np.inf],
	'max_trials': [100],
	'min_samples': [None],
	'random_state': [None],
	'residual_threshold': [None],
	'stop_n_inliers': [np.inf],
	'stop_probability': [0.99],
	'stop_score': [np.inf],
}
RandomForestRegressor_grid = {
	'bootstrap': [True],
	'ccp_alpha': [0.0],
	'criterion': ['mse'],
	'max_depth': [None],
	'max_features': ['auto'],
	'max_leaf_nodes': [None],
	'max_samples': [None],
	'min_impurity_decrease': [0.0],
	'min_impurity_split': [None],
	'min_samples_leaf': [1],
	'min_samples_split': [2],
	'min_weight_fraction_leaf': [0.0],
	'n_estimators': [100],
	'n_jobs': [-2],
	'oob_score': [False],
	'random_state': [None],
	'verbose': [0],
	'warm_start': [False],
}
Ridge_grid = {
	'alpha': [1.0],
	'copy_X': [True],
	'fit_intercept': [True],
	'max_iter': [None],
	'normalize': [False],
	'random_state': [None],
	'solver': ['auto'],
	'tol': [0.001],
}
RidgeCV_grid = {
	'alphas': [ 0.1,  1.0 , 10.0 ],
	'cv': [None],
	'fit_intercept': [True],
	'gcv_mode': [None],
	'normalize': [False],
	'scoring': [None],
	'store_cv_values': [False],
}
SGDRegressor_grid = {
	'alpha': [0.0001],
	'average': [False],
	'early_stopping': [False],
	'epsilon': [0.1],
	'eta0': [0.01],
	'fit_intercept': [True],
	'l1_ratio': [0.15],
	'learning_rate': ['invscaling'],
	'loss': ['squared_loss'],
	'max_iter': [1000],
	'n_iter_no_change': [5],
	'penalty': ['l2'],
	'power_t': [0.25],
	'random_state': [None],
	'shuffle': [True],
	'tol': [0.001],
	'validation_fraction': [0.1],
	'verbose': [0],
	'warm_start': [False],
}
SVR_grid = {
	'C': [1.0],
	'cache_size': [200],
	'coef0': [0.0],
	'degree': [3],
	'epsilon': [0.1],
	'gamma': ['scale'],
	'kernel': ['rbf'],
	'max_iter': [-1],
	'shrinking': [True],
	'tol': [0.001],
	'verbose': [False],
}
#Error with StackingRegressor
TransformedTargetRegressor_grid = {
	'check_inverse': [True],
	'func': [None],
	'inverse_func': [None],
	'regressor': [None],
	'transformer': [None],
}
TweedieRegressor_grid = {
	'alpha': [1.0],
	'fit_intercept': [True],
	'link': ['auto'],
	'max_iter': [100],
	'power': [0.0],
	'tol': [0.0001],
	'verbose': [0],
	'warm_start': [False],
}
XGBRegressor_grid = {
	'objective': ['reg:squarederror'],
	'base_score': [None],
	'booster': [None],
	'colsample_bylevel': [None],
	'colsample_bynode': [None],
	'colsample_bytree': [None],
	'gamma': [None],
	'gpu_id': [None],
	'importance_type': ['gain'],
	'interaction_constraints': [None],
	'learning_rate': [None],
	'max_delta_step': [None],
	'max_depth': [None],
	'min_child_weight': [None],
	'missing': [np.nan],
	'monotone_constraints': [None],
	'n_estimators': [100],
	'n_jobs': [-2],
	'num_parallel_tree': [None],
	'random_state': [None],
	'reg_alpha': [None],
	'reg_lambda': [None],
	'scale_pos_weight': [None],
	'subsample': [None],
	'tree_method': [None],
	'validate_parameters': [None],
	'verbosity': [None],
}
LGBMRegressor_grid = {
	'boosting_type': ['gbdt'],
	'class_weight': [None],
	'colsample_bytree': [1.0],
	'importance_type': ['split'],
	'learning_rate': [0.1],
	'max_depth': [-1],
	'min_child_samples': [20],
	'min_child_weight': [0.001],
	'min_split_gain': [0.0],
	'n_estimators': [100],
	'n_jobs': [-2],
	'num_leaves': [31],
	'objective': [None],
	'random_state': [None],
	'reg_alpha': [0.0],
	'reg_lambda': [0.0],
	'silent': [True],
	'subsample': [1.0],
	'subsample_for_bin': [200000],
	'subsample_freq': [0],
}