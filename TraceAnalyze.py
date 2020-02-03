import json
import os
import csv

allProcs = {}
totalTime = 0.0
allReqs = {}
reqCount = 0

def getSpanMetrics(TraceID):
  global totalTime
  global reqCount
  timePerProc = {}
  graphNodes = {}
  allSpans = {}
  
  reqCount += 1
  data = 0
  with open(TraceID, "r") as jsonF:
    data = json.loads(jsonF.read())
		
  for proc in data["data"][0]["processes"]:
      allProcs[proc] = {}
      allProcs[proc]["name"] =  data["data"][0]["processes"][proc]["serviceName"]
      if(allProcs[proc]["name"] not in allReqs):
          allReqs[allProcs[proc]["name"]] = []
      

  print([i["spanID"] for i in data["data"][0]["spans"]])
  for span in data["data"][0]["spans"]:
      allSpans[span["spanID"]] = {}
      allSpans[span["spanID"]]['process'] = allProcs[span["processID"]]["name"]
      allSpans[span["spanID"]]['duration'] = range(span["startTime"], span["startTime"]+span["duration"])
      
      if(len(span["references"]) > 0):
          if(span["references"][0]["spanID"] in graphNodes):
              graphNodes[span["references"][0]["spanID"]].append(span["spanID"])
          else:
              graphNodes[span["references"][0]["spanID"]] = [span["spanID"]]

  #span_list = data["data"][0]["spans"]
  
  temp_span = {}
  for span in allSpans:
      temp_span[span] = allSpans[span]["duration"]
  
  for span in temp_span:
  	print(span)
  
  for span in graphNodes:
    x = set()  
    for child_span in graphNodes[span]:
        x = x | set(allSpans[child_span]["duration"])
    temp_span[span]= set(temp_span[span]) - x

  for span in allSpans:
      allSpans[span]["duration"] = len(temp_span[span])
      totalTime += len(temp_span[span])
  
  for span in allSpans:
      if (allSpans[span]["process"] in timePerProc):
          timePerProc[allSpans[span]['process']] += allSpans[span]["duration"]
      else:
          timePerProc[allSpans[span]['process']] = allSpans[span]["duration"]
     
      
  for time in timePerProc:
      allReqs[time].append(timePerProc[time])

  return timePerProc

def getAllTraces():
    procTimes = {}
    path_to_json = "./"
    allTraces = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    for TraceID in allTraces:
        timePerProc = getSpanMetrics(TraceID)
        for proc in timePerProc:
            if(proc in procTimes):
                procTimes[proc] += timePerProc[proc]
            else:
                procTimes[proc] = timePerProc[proc]
    
    print("Service,Time")
    for proc in procTimes:
        procTimes[proc] /= totalTime
        print(proc, ",", procTimes[proc])

    with open("allRequests.csv", "w") as rFile:
        writer = csv.writer(rFile)
        hRow = [i for i in allReqs]
        hRow.insert(0, "Sl No.")
        writer.writerow(hRow)
        requestTS = [[i+1] for i in range(reqCount)]
        requestTS.insert(0, ["Sl No."])

        for service in allReqs:
            requestTS[0].append(service)
            for i in range(reqCount):
                    requestTS[i+1].append(allReqs[service][i])
        
        writer.writerows(requestTS)
            
                    
#getAllTraces()
getSpanMetrics("Request0309b497fe9ed685.json")
