v.0.1.2
------
- [x] Update `time_series_forecasting.md` in `docs`
- [x] Add Data `us_retail_sales.csv` in `data/raw`
- [x] Add Notebook `us_retrail_sales.ipynb` in `notebooks/hybrid_models`
- [x] Add Class `BoostedHybridModel` in `src.model_training.model_training.py`
- [x] Add PyTest Fixture `fixture_test_boosted_hybrid_model_data` in `tests/conftest.py`
- [x] Add PyTest Fixture `fixture_test_boosted_hybrid_model` in `tests/conftest.py`
- [x] Add function `fit` in class `BoostedHybridModel`
- [x] Add PyTest `test_boosted_hybrid_model_fit` in `tests/test_model_training.py`

v.0.1.1
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

v.0.1.0
------
- [x] Add `.github/workflows/pull_request_workflow.yml`
- [x] Add `.github/pull_request_template.md`
- [x] Add `scripts/pylint_lint.sh`
- [x] Add `scripts/sqlfluff_lint_and_fix.sh`