import bluetooth

#input the MAC address for bluetooth module below
bd_addr = "00:14:03:06:15:D0" 
port = 1
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM) #using RFCOMM bluetooh connection
sock.connect((bd_addr,port)) #connect to bluetooth socketin this variable

data = "" #store data that is transmitted via the bluetooth device
text_file = open("sensordata.txt", 'w') #open text file to write to.

while 1:
	try:
		data += sock.recv(1024)
		data_end = data.find('\n')
		if data_end != -1:
			rec = data[:data_end]
			print data
			text_file.write(data)

			data.split(",")
            
            #appended 1,2,3.. to the begining of sensor data so that it can easily be placed into it's own file.

			if data[0] == '1':
                                ecg_value= open("ecgvalue.txt", 'a')
				ecg_value.write(data)
				ecg_value.close()
			elif data[0] == '2':
                                emg_value = open("emgvalue.txt", 'a')
				emg_value.write(data)
				emg_value.close()
			elif data[0] == '3':
                                gsr_value = open("gsr.txt" , 'a')
				gsr_value.write(data)
				gsr_value.close()
                        elif data[0] == '4':
                                temp_value = open("temp.txt", 'a')
                                temp_value.write(data)
                                temp_value.close()
			else:
                                bp_data = open("bpvalue.txt", 'a')
                                bp_data.write(data)
                                bp_data.close()
                                
			data = data[data_end+1:]
			
except KeyboardInterrupt: 
		break
text_file.close()
sock.close()
