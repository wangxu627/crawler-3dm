#! /bin/bash

pushd proj_3dm
SUFFIX=`date '+%m%d'`
mkdir images
scrapy crawl game_list -o result.json
mv images/ images_$SUFFIX/
mv result.json result_$SUFFIX.json
popd