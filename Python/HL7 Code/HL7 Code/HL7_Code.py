import hl7
import os
message = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
message += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
message += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
message += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F'
h = hl7.parse(message)

with open ("C:\Users\gerson64\Documents\GitHub\HL7_EMR_Parser\Data\mayo_clinic_EKG1.txt", "r") as hlfile:
   data = hlfile.readlines()             
data=''.join(data)

h2 = hl7.parse(data)

#print type(h2)
#print len(h2)
#print h2

print h2.segment('OBX')[0][0]
print h2.segment('OBX')[0][0]
