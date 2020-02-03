import json
import requests

#Change IP address to the Jaeger Host

allProcs = {}
totalTime = 0.0

def storeJSON(TraceID):
  global totalTime
  global AllProcs
  timePerProc = {}

  url = "http://localhost:16686/api/traces/"+str(TraceID.strip())
  response = requests.get(url)
  data = json.loads(response.text)

  with open("Request"+str(TraceID.strip())+".json", "w") as jFile:
      json.dump(data, jFile)  

def getAllTraceIDs(File):
    procTimes = {}
    with open(File, "r") as allTraces:
        for TraceID in allTraces:
            storeJSON(TraceID)

getAllTraceIDs("TraceLogs")



