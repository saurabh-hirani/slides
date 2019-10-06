### Stage-1

```

cat stages/01/python27/requirements.txt

STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=1 PYVERSIONS=27 PROTO=https COUNT=5 PROFILE=1 ./bin/run-stages.sh

STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 PROFILE=1 ./bin/run-stages.sh | grep -E '===|total_time|installed_modules'
STAGE=1 PYVERSIONS=37 PROTO=https COUNT=5 PROFILE=1 ./bin/run-stages.sh
```
