hadoop jar JARS/hadoop-streaming-3.1.0.jar -mapper mapper.py -reducer reducer.py -input input/twitter.txt -output output
