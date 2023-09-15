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

## Why would you use it?

This `tranformation` was made to be used with [GREW-March](https://grew.fr/grew_match/), a tool to match patterns on graphs.
As of this tool uses the CoNLL-U format, we needed to convert the WAC into this format.
The `GPU_WACoNNLU.py` script is the result of this conversion.
But we still had one issue, the WAC is a huge corpus, and the tool, meant to be used on the UD corpora, was not able to handle it.
That is why a second script, `wackier_wac.py` was made, in order to split the WAC into folders of only 4 files each.
The script also generates a `corpora_list.json` file, which is used by the `GREW-Match` tool to know which corpora do we have and what are their properties (the path to the folder still needs to be completed manually).
