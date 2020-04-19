#!/usr/bin/env bash

PORT=80
echo "Port: $PORT"

# POST method predict
curl -d '{
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":8.575
   },
   "TAX":{
      "0":496.0
   },
   "PTRATIO":{
      "0":35.3
   },
   "B":{
      "0":596.9
   },
   "LSTAT":{
      "0":6.98
   }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
