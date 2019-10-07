### Notes for grequests-https-talk

This dir contains markdown notes which are linked from [grequests-https-talk](http://saurabh-hirani.github.io/slides/decks/grequests-https-talk/main.html)

### Add/remove sample output section

This dir also contains 2 scripts which are used to add/remove ```Sample output``` sections from each markdown file.
This is useful to hide/show sample outputs during presentations.

```shell
# cat test.md

Sample output

f1
f2
```

```shell
# ./add-comments.sh test.md
Patching test.md

# cat test.md

<!--
Sample output
f1
f2
-->
```

```shell
# ./remove-comments.sh test.md
Patching test.md

# cat test.md

Sample output
f1
f2
```
