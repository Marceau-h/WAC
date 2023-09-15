# WAC

## Web As CoNLL-U

Source corpora: 

[D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012](https://wortschatz.uni-leipzig.de/en/download/French)

Licence :

GNU Affero General Public License v3.0

## Usage
The Web as CoNLL-U (WAC) uses the aforementioned corpora as q source. The corpora are available in the [Leipzig Corpora Collection](https://wortschatz.uni-leipzig.de/en/download).
It processes it with the `fr_dep_news_trf` pipeline and then converts it to the CoNLL-U format, as of the SUD recommendations

The source-code is now available in this very repository, `GPU_WACoNNLU.py` is the main file, and it needs the requirements listed in `requirements.txt` to run.




