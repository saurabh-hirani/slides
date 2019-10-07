#!/bin/bash

ls $* | while read file; do
    if [[ $file == 'README.md' ]]; then
        echo "Skipping $file"
        continue
    fi
    if ! grep '<!--' "$file" > /dev/null ; then
        echo "Skipping $file"
        continue
    fi
    echo "Patching $file"
    sed -i '' 's/<!--//g;s/-->//g' $file
done
