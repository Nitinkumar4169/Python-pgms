#153.Write a python pgm to generate a random OTP
import secrets
import time

def genearate_otp(length=6):
  digits = "123456789"
  otp = "".join(secrets.choice(digits) for _ in range(length))
  return otp

def verify_otp(real_otp,expiry_time):
  start_time = time.time()

  usr_otp = input("Enter OTP: ")

  current_time = time.time()

  if current_time - start_time > expiry_time:
     print("❌ OTP expired!")
  elif usr_otp == real_otp:
     print("✅ OTP verified successfully!")
  else:
     print("❌ Invalid OTP!")
        
#main pgm
otp = genearate_otp(6)
print("Your otp is: ",otp)

expiry_time = 30 #second
print("⏳ OTP Valid for ",expiry_time,"seconds")  

verify_otp(otp, expiry_time)