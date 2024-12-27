run:
	@python bank_loan_model_package_folder/main.py

run_uvicorn:
	@uvicorn bank_loan_model_package_folder.api:app --reload

install:
	@pip install -e .

test:
	@pytest -v tests

reset_trained_models:
	@rm -rf ${TRAIN_MDL_DIR}
	@mkdir ${TRAIN_MDL_DIR}
