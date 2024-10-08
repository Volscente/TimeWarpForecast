v0.1.6
------
- [x] Add Data in `data/store_sales/`
- [x] Add Configuration `store_sales_config.toml` in `configuration`
- [x] Add Module `data_preparation`
- [x] Add Function `group_avg_column_by_frequency` in `src/data_preparation/data_preparation_utils.py`
- [x] Add Data `test_data_preparation_dataset.csv` in `data/test`
- [x] Add PyTest Fixture `fixture_data_preparation_dataset` in `tests/conftest.py`
- [x] Add PyTest `test_group_avg_column_by_frequency` in `tests/test_data_preparation.py`
- [x] Add Function `add_dummy_time_step` in `src/data_preparation/data_preparation_utils.py`
- [x] Add PyTest `test_add_dummy_time_step` in `tests/test_data_preparation.py`
- [x] Add Function `add_lag_feature` in `src/data_preparation/data_preparation_utils.py`
- [x] Add PyTest `test_add_lag_feature` in `tests/test_data_preparation.py`
- [x] Add Function `plot_regression_plot` in `src/exploratory_data_analysis/exploratory_data_analysis_utils.py`
- [x] Refactor function `plot_predictions_vs_time_series ` in `src/exploratory_data_analysis/exploratory_data_analysis_utils.py` in order to plot both past and future predictions
- [x] Add Function `add_seasonality` in `src/data_preparation/data_preparation_utils.py`
- [x] Add PyTest `test_add_seasonality` in `tests/test_data_preparation.py`
- [x] Add PyTest `test_add_seasonality_exception` in `tests/test_data_preparation.py`
- [x] Add Function `plot_seasonality` in `src/exploratory_data_analysis/exploratory_data_analysis_utils.py`
- [x] Add Function `plot_periodgram` in `src/exploratory_data_analysis/exploratory_data_analysis_utils.py`
- [x] Add Notebook `store_sales_eda.ipynb` in `notebooks/store_sales`
- [x] Add Notebook `store_sales_model_training.ipynb` in `notebooks/store_sales`

v0.1.5
------
- [x] Update Notebook `pandas_code_utils.ipynb` in `notebooks/code_utils`

v0.1.4
------
- [x] Add Data `samples.csv` in `data/raw`
- [x] Add Data `trade_inventories.csv` in `data/raw`
- [x] Add Data `co2__mm_mlo.csv` in `data/raw`
- [x] Add Data `restaurant_visitors.csv` in `data/raw`
- [x] Add Data `money_stock.csv` in `data/raw`
- [x] Add Data `personal_spending.csv` in `data/raw`
- [x] Add Section PRDARIMA into `notebooks/code_utils/statsmodels_code_utils.ipynb`
- [x] Add Section SARIMA into `notebooks/code_utils/statsmodels_code_utils.ipynb`
- [x] Add Section SARIMAX into `notebooks/code_utils/statsmodels_code_utils.ipynb`

v0.1.3
------
- [x] Add Notebook `pandas_code_utils.ipynb` in `notebooks/code_utils`
- [x] Add Notebook `statsmodels_code_utils.ipynb` in `notebooks/code_utils`
- [x] Add Doc `statistics.md` in `docs`
- [x] Add Data `us_population.csv` in `data/raw`
- [x] Add Data `daily_female_births.csv` in `data/raw`
- [x] Add Data `energy_productions.csv` in `data/raw`
- [x] Add Data `airline_passengers.csv` in `data/raw`
- [x] Add Data `macrodata.csv` in `data/raw`

v0.1.2
------
- [x] Update `time_series_forecasting.md` in `docs`
- [x] Add Data `us_retail_sales.csv` in `data/raw`
- [x] Add Notebook `us_retrail_sales.ipynb` in `notebooks/hybrid_models`
- [x] Add Class `BoostedHybridModel` in `src.model_training.model_training.py`
- [x] Add PyTest Fixture `fixture_test_boosted_hybrid_model_data` in `tests/conftest.py`
- [x] Add PyTest Fixture `fixture_test_boosted_hybrid_model` in `tests/conftest.py`
- [x] Add function `fit` in class `BoostedHybridModel`

v0.1.1
------
- [x] Add `time_series_forecasting.md` in `docs`
- [x] Add data `tunnel.csv` in `data/raw`
- [x] Add config `linear_regression_config.yaml` in `config`
- [x] Add module `logging_module.py` in `src/logging_module`
- [x] Add config `log_configuration.yaml` in `src/logging_module`
- [x] Add PyTest `test_get_logger` in `tests/test_logging_moduke.py`
- [x] Add PyTest `test_get_logger_exceptions` in `tests/test_logging_moduke.py`
- [x] Add module `general_utils.py` in `src/general_utils`
- [x] Add function `read_configuration` in `src/general_utils/general_utils.py`
- [x] Add function `build_path_from_list` in `src/general_utils/general_utils.py`
- [x] Add PyTest `test_read_configuration` in `tests/test_general_utils.py`
- [x] Add PyTest `test_read_configuration_exceptions` in `tests/test_general_utils.py`
- [x] Add PyTest `test_build_path_from_list` in `tests/test_general_utils.py`
- [x] Add function `read_data_from_config` in  `src/general_utils/general_utils.py`
- [x] Add module `conftest.py` in `tests`
- [x] Add Fixture `fixture_data_config` in `tests/conftest.py`
- [x] Add PyTest `test_read_data_from_config` in `tests/test_general_utils.py`
- [x] Add PyTest `test_read_data_from_config_exceptions` in `tests/test_general_utils.py`

v0.1.0
------
- [x] Add `.github/workflows/pull_request_workflow.yml`
- [x] Add `.github/pull_request_template.md`
- [x] Add `scripts/pylint_lint.sh`
- [x] Add `scripts/sqlfluff_lint_and_fix.sh`