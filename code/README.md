### The input csv data is contained in the input_data folder
### If you have the .dat csv files, then it can be converted into .csv files using the code in Spark notebook in source_code.
### The csv files can be merged into single file using the code in the Dask notebook and the output will be generated in the output_file folder
### To start a dask scheduler use: dask-scheduler --port "port_number"
### To start dask worker on the node use: dask-worker "scheduler port number"
### All the code for running code on the cluster using dask, joblib and scikit-learn is written in the Dask_and_scikitlearn_on_server,cluster.ipynb file in source_code folder 
### All the code for running code on the local machine using spark and scikit-learn is written in the Spark_and_scikitlearn_on_local_machine.ipynb file in source_code folder 
### The file random_forest_implementation has the code for multi-threading and multi-processing mode.
### For multi-processing mode, forest_modified file is imported, which is almost exact replica of the original forest file of scikit-learn ensemble classifier (https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/forest.py)
### _joblib.py is the file which is replica of original joblib from scikit-learn utils (https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_joblib.py)
### To run in multi-processing mode, inside the function **train_model** , use RandomForestClassifier, which is being imported from forest_modified file.
### To run in original Scikit-Learn multi-threading mode, inside the function **train_model** , use RandomForestClassifier_original instead of RandomForestClassifier
