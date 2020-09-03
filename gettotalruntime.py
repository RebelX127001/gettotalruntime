def getRuntime():
     startTime = time.time()
     #Add main code here to calculate the total runtime to get the job done
     for i in range (0, 20):
             print (i)
             time.sleep(1)
     endTime = time.time()
     timeElapsed = endTime - startTime
     if timeElapsed < 60:
        print ("Total Runtime In Seconds:", timeElapsed)
     else:
         print ("Total Runtime In Minutes:", timeElapsed/60)
getRuntime()
