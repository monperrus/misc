# Misc of @monperrus

## in this repo

* [A curated list of Java agents](https://github.com/monperrus/misc/blob/master/awesome-java-agents.md)
* [direct-bibtex-in-google-scholar.user.js: userscript to add a bibtex button in Google Scholar](https://github.com/monperrus/misc/blob/master/direct-bibtex-in-google-scholar.user.js)
* [java-ls-methods.groovy: outputs the list of functions of Java file passed as parameter together with a checksum of the method body](https://github.com/monperrus/misc/blob/master/direct-bibtex-in-google-scholar.user.java-ls-methods.groovy)
* [repair.md: some notes on program repair](https://github.com/monperrus/misc/blob/master/repair.md)
* [push-file-to-github.sh: Bash script to push a file to github via the REST API](https://github.com/monperrus/misc/blob/master/push-file-to-github.sh)
* [how-to-open-science-software-research.md](https://researchdata.springernature.com/posts/57389-how-to-make-a-good-open-science-repository)
* [README-template.md: template for github readme](https://github.com/monperrus/misc/blob/master/README-template.md)
* [open-science-reproducibility-reading-notes.md: notes about Open science and Reproducibility](https://github.com/monperrus/misc/blob/master/open-science-reproducibility-reading-notes.md)
* [biblio-software-repair.bib: bibtex source of "The Living Review on Automated Program Repair "](https://github.com/monperrus/misc/blob/master/biblio-software-repair.bib)
* [list_gists.py: lists gists for a given user](https://github.com/monperrus/misc/blob/master/list_gists.py)
* Latex:
  * [prepare-latex-hal-arxiv.sh: Creates a zip file containing all sources of a LaTeX document to be submitted to Arxiv](https://github.com/monperrus/misc/blob/master/prepare-latex-hal-arxiv.sh)
  * [preprocess-latex.py: preprocess a latex file](https://github.com/monperrus/crypto/blob/main/preprocess-latex.py)
* [ddc.md: notes on diverse double compilation](https://github.com/monperrus/crypto/blob/main/ddc.md)
* [shamir.md: compatible implementations of Shamir's Secret Sharing](https://github.com/monperrus/crypto/blob/main/shamir.md)
* [genai-science.md: notes on generative AI and science](https://github.com/monperrus/crypto/blob/main/genai-science.md)

## gists

To be updated with:

```
$ cd workspace/misc
$ ./list_gists.py
```

* [colors.py: a python program that outputs a colored loren ipsum with ASC         II color sequences.](https://gist.github.com/monperrus/12ccb77344c494e9fc54e7fdd567f903)
* [document_file.py: write a python program that parses another python program, summarizes the full file, replace the module docstring and rewrite the program ](https://gist.github.com/monperrus/dc7428b4612910c80dd7dbefd69a8866)
* [pace.py: a python program to compute pace min/kilo from a tcx file](https://gist.github.com/monperrus/cab33728b0637333f330fdc1912e4a2d)
* [merge-laps.py: a python script to merge all activities in a tcx file](https://gist.github.com/monperrus/a5eb677edba5963b0a16bb0907d1828c)
* [in_canada.py: go over all tcx files, if the tcx coordinates are in canada, print the file name](https://gist.github.com/monperrus/6a2ef620f0c845ebc68475f475a60073)
* [repos.py: iterate over all repos of a github organization in python ](https://gist.github.com/monperrus/b70446d4fc041a3a2182d86eebb0299c)
* [t-sne.py: t-sne visualization in python, with tooltips on points](https://gist.github.com/monperrus/b73b8c318ff440b7e7596f5da7850c69)
* [example-hash.py: python compute a hash of file and sign it with cryptography.hazmat](https://gist.github.com/monperrus/1e5138f6ff978c05900af9bf689def61)
* [example-fastapi.py: a running example of a fastapi server](https://gist.github.com/monperrus/760ab835a2504cf08eec3ce9a1a64e5b)
* [example-dbus.py: a simple python application which expose an example service hello on dbus](https://gist.github.com/monperrus/9d5334a08dd2bea916dea601864b5b43)
* [example-flask.py: a simple python application which expose an example service hello](https://gist.github.com/monperrus/50bac0eb0174c6b2352617587932ae14)
* [example-ncurse.py: a python ncurse app with two column](https://gist.github.com/monperrus/0d1b6e0efda64da3fadd77b28ccd9eaf)
* [http-server.py: in python 3, start an http server, when a request is received, save the GET query parameter in file code.txt and shutdown the server](https://gist.github.com/monperrus/21151e2db4a7fdc505bff157918e61b5)
* [example-wsgi-input.py: pipe wsgi.input into subprocess.Popen](https://gist.github.com/monperrus/1565af160c726ac04cebc7b4857cfa1b)
* [chinese.py: implement the chinese remainder theorem in python
](https://gist.github.com/monperrus/f84480b0b2924cc5fba0a0c6eaf4ba39)
* [osmtosvg.py: write a transformer xml in osm format (openstreetmap) to svg which only keeps map lines](https://gist.github.com/monperrus/842cb622894bca6974f9e5db2d6a4ac9)
* [clean_bash_history.py: a python script to remove secrets and keys  in bash history file](https://gist.github.com/monperrus/35b280ea6c345d0bd4c7101a66105558)
* [dns-over-https.py: a python script that performs dns resolution on 8.8.8.8 doh](https://gist.github.com/monperrus/c69c25e7c801cccc8050bea1415a18d1)
* [create-pdf-photos.py: small python script to concatenate pictures as jpg files into a PDF of the same size](https://gist.github.com/monperrus/6e5a9c73dba907966292ee0b9783e56a)
* [systray-notes.py: a python systray application that adds a list of items in system tray icon](https://gist.github.com/monperrus/8066244330ac01308a6695aa18aedf50)
* [ls-repos.py: python script to list github repos of a user ordered by last update](https://gist.github.com/monperrus/3afdae159d1eb0e677b35bac28cdc3a0)
* [process_age.py: get age of process in python](https://gist.github.com/monperrus/29de44da9fe858015980d2cbe852e4b1)
* [run-tests.py: a python script to identify the type of build and tests in the current directory and run the tests accordingly (ex maven test for maven, etc)](https://gist.github.com/monperrus/553d1a4cc84d47f2d9dc1f0b6ab11729)
* [github-search.py: a python script to call the github search api looking for code](https://gist.github.com/monperrus/b1ffe956fed22745b1ba59e7a5447c20)
* [recollq.py: Recollq with JSON output](https://gist.github.com/monperrus/92d0b527355a59cecf7a066cbd05c74c)
* [joplin_systray.py: python system tray to show and start joplin notes](https://gist.github.com/monperrus/6e43a5216179662655c50b901d0d152b)
* [howcome-dd-on-states.py: an example implementation of Howcome for Python (debugging on program states), author: Andreas Zeller](https://gist.github.com/monperrus/fb4d475ff1283cb68afaf4b882ac1b92)
* [github-show-all-comments.user.js: Greasemonkey / Tampermonhey / Violentmonkey userscript to automatically show all comments on Github](https://gist.github.com/monperrus/4f3fa3ecd4fcc9c617734acb7069869c)
* [fcgi_client.py: A standalone FastCGI client in Python 3](https://gist.github.com/monperrus/611e7b6c5e7ef5b3d26e9b027f69d329)
* [inject_spoon_snapshot.py: inject_spoon_snapshot.py](https://gist.github.com/monperrus/4bf62ca7bf369b73b01538b73d57e889)
* [build.sh: spoon build.sh](https://gist.github.com/monperrus/866f482f73af5f910ec7c3c191d44053)
* [export-nextcloud-notes-to-enex.py: export Nextcloud Notes to the Enex file format for importing into Evernote or Joplin](https://gist.github.com/monperrus/93b5fe05025a726b13f64a971e9127c2)
* [deploy-contract-ledger-nano.js: deploy a contract with a ledger nano (javascript with ethers library)](https://gist.github.com/monperrus/421478389fc7defb3d9ee3a060cf9bdb)
* [debank-curl.js: calls the debank API](https://gist.github.com/monperrus/118a4331282027984bde6ced62f27d2c)
* [mark.py: mark calendar email responses as READ on EWS Exchange server](https://gist.github.com/monperrus/23b694cee69ca4e023e8182c91a4f0b3)
* [tzid-microsoft-owa.js: timezones tzid of Microsoft Exchange / OWA version 15.2.1258.23](https://gist.github.com/monperrus/12f852e9b629e7028494ffc92da52aeb)
* [ecryptfs-map.py: ecryptfs-map: maps a decrypted filename to the ecrypfs-encrypted counterpart (and vice versa) and outputs the filename to the console](https://gist.github.com/monperrus/7a114ccc1c2fd20dcc5e852cdf813c5d)
* [export-nextcloud-passwords-to-bitwarden-json.py: Basic migration from Nextcloud JSON (export) to Bitwarden JSON (import)](https://gist.github.com/monperrus/c671817d53f6fc4bfe8d1773f28262d7)
* [export-keepass-to-nextcloud-password-json.py: Export KeePass folders and passwords to Nextcloud Passwords backup JSON format](https://gist.github.com/monperrus/5f3ca5ac9aa59159b33770701c0d5dc7)
* [export-keepass-to-bitwarden-json.py: Export KeePass KDBX (folders and passwords) to Bitwarden JSON](https://gist.github.com/monperrus/578395c30667581677d1ec20b7d445de)
* [mulisoft.py: python code in mulisoft advertisement ](https://gist.github.com/monperrus/55a22836175779e2967a62da4cab6e33)
* [spoon-ci-job.sh: used in spoon jenkins](https://gist.github.com/monperrus/62c7b95812f15af16ec7faef4a8bd306)
* [gaia-request.py: ](https://gist.github.com/monperrus/c13146fb22e084075d0c7becdf17ac1c)
* [remove-unused-imports.py: remove-unused-imports.py: pre-commit hook to find and remove unused imports in Java source code using maven checkstyle](https://gist.github.com/monperrus/faf7a6c66bce3ce8fe04ff0acbcf75c4)
* [notesforgooglescholar.user.js: notesforgooglescholar: Greasemonkey script to take notes on search results of Google Scholar directly in the browser](https://gist.github.com/monperrus/5c73fe64711ff351e6c151c3778ae6b0)
* [dblp-rss.py: Creates an RSS feed with DBLP JSON data from its API. ](https://gist.github.com/monperrus/978079d39c1cc7b4cbae78ddd1b8ed99)
* [common-letters.py: prints the common letters between an AZERTY and QWERTY keyboard (without Shift and Alt-GR)](https://gist.github.com/monperrus/421395b7be4073cc9398)
* [preprocess_latex.sh: Prepares LateX sources by unfolding the input/include graph and removing the comments](https://gist.github.com/monperrus/5524007)
* [pyfsm.py: Contains a small model-driven development toolchain for teaching purpose](https://gist.github.com/monperrus/4399016)
* [migration-jskit-jskomment.py: Migrates the XML export file of js-kit/echo to the format of jskomment (http://code.google.com/p/jskomment/)](https://gist.github.com/monperrus/3088907)
* [GM_XHR.js: allows using all Jquery AJAX methods in Greasemonkey](https://gist.github.com/monperrus/999065)

## Utilities

* [check.py](https://github.com/monperrus/misc/blob/master/check.py)
