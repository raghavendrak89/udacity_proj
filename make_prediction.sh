#!/usr/bin/env bash

PORT=8000
echo "Port: $PORT"

# POST method predict
curl -d '{
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":7.575
   },
   "TAX":{
      "0":396.0
   },
   "PTRATIO":{
      "0":25.3
   },
   "B":{
      "0":496.9
   },
   "LSTAT":{
      "0":5.98
   }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
