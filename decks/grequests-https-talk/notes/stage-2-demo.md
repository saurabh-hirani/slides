### Stage-2

```
cat stages/02/python27/requirements.txt

cat stages/02/python37/requirements.txt

STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=2 PYVERSIONS=27 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh

STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=2 PYVERSIONS=37 PROTO=https COUNT=3 PROFILE=1 ./bin/run-stages.sh
```
