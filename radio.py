class radio():
    def __init__(self,color,brand,ACPower,headphone):
        self.color = color
        self.brand = brand
        self.ACPower = ACPower
        self.headphone = headphone
        
    def power(self,pswitch):
        if pswitch == 'ON':
            print("Radio is ON! ")
        else:
            print("Radio is OFF! ")
            
    def mode(self,mode):
        self.mode = mode
        if mode == 'AM':
            print("Mode is set to AM. ")
        elif mode == 'FM':
            print("Mode is set to FM. ")
        else:
            print("Mode not found. ")
            
    def frequency(self,freq):
        if freq <= 108 and freq >=88:
            print("You are listening to: ",freq,self.mode)
        else:
            print("Bad Frequency. ")
            
    def volume(self,vol):
        self.vol = int(vol)
        if self.vol > 0 and self.vol < 11:
            print("Volume is set at: ",self.vol)
        else:
            print("Bad Volume. ")
        
    def song(self,songname):
        print("Playing: ",songname)
        
    def destroy(self):
        print("Radio is destroyed. ")
        
Radio = radio("Black","Sony","25W","SonyXB")
Radio.power("ON")
Radio.mode("FM")
Radio.frequency(102.2)
Radio.volume(8)
Radio.song("I believe I can fly")
Radio.power("OFF")
Radio.destroy()
