Title: Test Drive: Clojure
Author: Ross Donaldson
Date: 2014-02-23 18:29
Slug: 2014-02-23_test_drive_clojure
Category:
Tags:
Summary:
status: draft


* Getting the data working... at all.
* Some idiosyncracies. For instance: this works fine:
```clojure
(map identity ($ 0 ufo-data))
```
But this explodes:
```clojure
(take 2 ufo-data)
```


### Too many tabs!

The data is fucked up. Column 6 is a text field... which allows tabs!

```r
> t <- read.csv('~/Code/ufoh/lib/ufo_awesome.tsv', sep='\t', header=FALSE, stringsAsFactors=FALSE)
> dim(t)
[1] 61870     6
```

```bash
cut -f 6- -d$'\t' ufo_awesome.tsv | sed -e 's/\t//g' >> ufo_awesome_repaired_col_6.tsv
```
