# JaegerRequestAnalysis

Repository to help analyze time spent in each process recorded by jaegertracing/jaeger:all-in-one container.

## Results

Detailed CSV file of time spent in every request.

| Sl No. | url-shorten-service | write-home-timeline-service | user-timeline-service | unique-id-service | user-mention-service | text-service | media-service | compose-post-service | post-storage-service | nginx-web-server | user-service | social-graph-service |
|--------|---------------------|-----------------------------|-----------------------|-------------------|----------------------|--------------|---------------|----------------------|----------------------|------------------|--------------|----------------------|
| 1      | 703                 | 2118                        | 2476                  | 202               | 879                  | 1367         | 207           | 3279                 | 1033                 | 1100             | 220          | 1073                 |
| 2      | 647                 | 1423                        | 2757                  | 198               | 789                  | 1413         | 397           | 3404                 | 651                  | 1635             | 215          | 1294                 |
| 3      | 838                 | 2070                        | 2455                  | 196               | 1131                 | 1388         | 258           | 3258                 | 1028                 | 1511             | 284          | 1041                 |
| 4      | 437                 | 1997                        | 2537                  | 256               | 881                  | 1165         | 278           | 3558                 | 716                  | 1723             | 285          | 959                  |
| 5      | 554                 | 1051                        | 1989                  | 163               | 904                  | 1290         | 211           | 3101                 | 509                  | 1695             | 183          | 1455                 |
| 6      | 679                 | 1646                        | 2789                  | 226               | 796                  | 1521         | 234           | 2969                 | 868                  | 1212             | 324          | 1069                 |
| 7      | 856                 | 2384                        | 2884                  | 252               | 863                  | 1500         | 817           | 3163                 | 797                  | 991              | 283          | 1098                 |
| 8      | 651                 | 1068                        | 2944                  | 252               | 1062                 | 1134         | 231           | 3866                 | 850                  | 1264             | 229          | 1163                 |
| 9      | 588                 | 908                         | 2254                  | 206               | 882                  | 1089         | 267           | 2804                 | 691                  | 1535             | 224          | 883                  |
| 10     | 852                 | 2339                        | 2588                  | 229               | 709                  | 1665         | 294           | 2741                 | 528                  | 1669             | 213          | 921                  |

Normalized fraction of time spent in each process recorded by jaeger over all the requests.

| Service                     | Time                 |
|-----------------------------|----------------------|
| post-storage-service        | 0.05193824188361299  |
| user-service                | 0.01637337362299682  |
| compose-post-service        | 0.22913141719397376  |
| media-service               | 0.017415177054009533 |
| unique-id-service           | 0.01556491886635278  |
| url-shorten-service         | 0.043472801806287424 |
| nginx-web-server            | 0.09694501602374421  |
| social-graph-service        | 0.07579789080912669  |
| write-home-timeline-service | 0.11612430905598091  |
| text-service                | 0.0939785077436617   |
| user-timeline-service       | 0.18406863937199405  |
| user-mention-service        | 0.05918970656825913  |

These results are useful in characterizing performance of individual microservices and to identify bottlenecks.
The detailed request data can be used to identify anomalous behaviour in requests corrosponding to the tail latencies.

## Requirements
* [jaegertracing/all-in-one Image](https://hub.docker.com/r/jaegertracing/all-in-one)
* Set the Enviroment variable "LOG_LEVEL=debug" to log all the TraceIDs

## Usage
* Run the Script to retrieve all the traces in JSON format from Jaeger. 
``` 
./ExtractTraces.sh <Container-Name> <Duration>
./ExtractTraces.sh Jaeger_1 5m
```
This will extract all the traces in the past 5 minutes.

* Run the Trace Analyze Script. <br/> This will store all the request data in a CSV file and will print the time fractions spent in each process.
