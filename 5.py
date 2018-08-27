import pyautogui, time, os
#
#UBUNTU LibreOfficeWriter Arial 22 Preview 56%
#
#while(1):
#   print pyautogui.position()
time.sleep(5) 
os.system( 'rm scr_*.jpg txt_*.txt' )
for i in range(6):
   print 'i=',i 
   pyautogui.moveTo(126, 83) # next page (126, 83)
   print pyautogui.position()
   cmd='/usr/bin/scrot -q 99 /home/val/scr_'+str(i)+'.jpg'
   print cmd
   os.system( cmd )
   os.system( 'ls -l /home/val/scr_'+str(i)+'.jpg' )
   cmd='/usr/bin/tesseract /home/val/scr_'+str(i)+'.jpg /home/val/txt_'+str(i)
   print cmd
   os.system( cmd )
   os.system( 'ls -l /home/val/txt_'+str(i)+'.txt' )
#   time.sleep(1) 
   pyautogui.click()		# click

i=i+1
print 'i=',i 
pyautogui.moveTo(126, 83) # next page (126, 83)
print pyautogui.position()
cmd='/usr/bin/scrot -q 99 /home/val/scr_'+str(i)+'.jpg'
print cmd
os.system( cmd )
os.system( 'ls -l /home/val/scr_'+str(i)+'.jpg' )
cmd='/usr/bin/tesseract /home/val/scr_'+str(i)+'.jpg /home/val/txt_'+str(i)
print cmd
os.system( cmd )
os.system( 'ls -l /home/val/txt_'+str(i)+'.txt' )
print '\nmake one txt file'
os.system('cat /home/val/txt_* >txt_txt')

