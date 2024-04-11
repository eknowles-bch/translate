# translate

1.	Anaconda should be installed for this to work. Open a terminal window. Navigate to the directory where you would like to run this (it should include the python script and the csv with the columns that you want to translate) then create a new conda environment: 

cd /emma/work/translation 
conda create --name translate python=3.9 pandas tqdm pip

2.	Activate your conda environment:
   
conda activate translate

3.	Install the translator package using pip:

pip install deep_translator

4.	Run the python script, specify the csv with the column(s) to be translated, the columns you want to translate, and the target language:
   
python translate_es_en.py EPIMex_for_trans.csv info_dx_2 scid_initial_dx_2 --target_language en

5.	This should output a new version of your csv with the prefix _translated. It should include versions of your Spanish columns in English. Running this is kind of slow! But it should get the job done and there is a progress bar to let you know how things are going. 

