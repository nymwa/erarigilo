# ERARIGILO

error generation tool

## usage (en)

note: please use SpaCy v3. SpaCy v2 is not supported.

- `erg ready en`
	- SpaCy Tokenization & Tagging
- `erg run en`
	- Error Generation
	- Please write which error modules you use in `config.yaml`.
- `erg show en`
	- Show Generated Errors
- `erg form en`
	- Make parallel data

example

```
echo 'I have a pen.' | erg ready en | erg run en --no-error | erg show en

src: I have a pen .
trg: I have a pen .
history (0): 
+-----+---------+-------+-------+--------+-----------+-----------+-------+-------+-------+---------+--------+------------+-----------+-----------+
|   i |   shift | src   | trg   | cond   | l_space   | r_space   | tag   | pos   | dep   | lemma   | norm   | ent_type   | ent_iob   | history   |
|-----+---------+-------+-------+--------+-----------+-----------+-------+-------+-------+---------+--------+------------+-----------+-----------|
|   0 |       0 | ____  | I     |        | o         | o         | PRP   | PRON  | nsubj | I       | i      |            | O         | ____      |
|   1 |       0 | ____  | have  |        | o         | o         | VBP   | VERB  | ROOT  | have    | have   |            | O         | ____      |
|   2 |       0 | ____  | a     |        | o         | o         | DT    | DET   | det   | a       | a      |            | O         | ____      |
|   3 |       0 | ____  | pen   |        | o         | o         | NN    | NOUN  | dobj  | pen     | pen    |            | O         | ____      |
|   4 |       0 | ____  | .     |        | o         | o         | .     | PUNCT | punct | .       | .      |            | O         | ____      |
+-----+---------+-------+-------+--------+-----------+-----------+-------+-------+-------+---------+--------+------------+-----------+-----------+

```

```
echo 'I have a pen.' | erg ready en | erg run en --no-error | erg form en

I have a pen .  I have a pen .
```

```
cat config.yaml

- del:
   mean: 0.1
   std: 0.1

echo 'I have a pen.' | erg ready en | erg run en | erg show en

rc: I a pen
trg: I have a pen .
history (1): del(0.31)
+-----+---------+-------+-------+--------+-----------+-----------+-------+-------+-------+---------+--------+------------+-----------+-----------+
|   i |   shift | src   | trg   | cond   | l_space   | r_space   | tag   | pos   | dep   | lemma   | norm   | ent_type   | ent_iob   | history   |
|-----+---------+-------+-------+--------+-----------+-----------+-------+-------+-------+---------+--------+------------+-----------+-----------|
|   0 |       0 | ____  | I     |        | o         | o         | PRP   | PRON  | nsubj | I       | i      |            | O         | ____      |
|   1 |       0 |       | have  |        | o         | o         | VBP   | VERB  | ROOT  | have    | have   |            | O         | del       |
|   2 |       0 | ____  | a     |        | o         | o         | DT    | DET   | det   | a       | a      |            | O         | ____      |
|   3 |       0 | ____  | pen   |        | o         | o         | NN    | NOUN  | dobj  | pen     | pen    |            | O         | ____      |
|   4 |       0 |       | .     |        | o         | o         | .     | PUNCT | punct | .       | .      |            | O         | del       |
+-----+---------+-------+-------+--------+-----------+-----------+-------+-------+-------+---------+--------+------------+-----------+-----------+
```

