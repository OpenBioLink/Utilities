# Scripts for 
## eval.py

Skript used to evaluate a single prediction file. 

Usage:

```bash
python eval.py {path_to_pred_file} {path_to_testset_file}
```

## eval_experiment.py

Script used to evaluate a experiment (Multiple datasets -> Multiple prediction files)

```bash
python eval_experiment.py --datasets {list of datasets} --predictions {list of prediction file names}
```

**File structure**

Path to prediction file: f"./{dataset}/predictions/{prediction}"
Path to testset file: f"./{dataset}/data/test.txt"

F.e.:

```python eval_experiment.py --datasets OBL WN18RR --predictions predfile1.txt predfile2.txt```

---- OBL
	|
	---- predictions
		|
		---- predfile1.txt
		|
		---- predfile2.txt
	|
	---- data
		|
		---- test.txt

---- WN18RR
	|
	---- predictions
		|
		---- predfile1.txt
		|
		---- predfile2.txt
	|
	---- data
		|
		---- test.txt

​    

​             

