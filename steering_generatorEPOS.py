#!/usr/bin/python

##
##
###############################################################################################################
import sys
import random
import os,os.path
from datetime import datetime
from datetime import date



######
if len(sys.argv)>1:
  energy = str(sys.argv[1])
  thin = str(sys.argv[2])
  wmax = str(sys.argv[3])
  rmax = str(sys.argv[4])
  rand1 = random.randint(1,900000000) # 1 <= N <= 900 000 000
  rand2 = random.randint(1,900000000)
  rand3 = random.randint(1,900000000)
  angle = 0
  primary = 14 #proton
  #primary = 1206 #carbon
  #primary = 5628 #iron
  ##primary == A * 100 +Z A==atomic weight, Z == # protons
  date = datetime.now()
  date2 = datetime.strftime(date,"%y%m%d-%H%M%S")

  #####
  #using 1e-8 for EeV showers and 1e-7 for 100PeV for a roughly 10 GeV cut off(wmax ==10), could go 1e-6 and 1e-7 for a 100 GeV cutoff (wmax == 100); lets make wmax 10 because optimized Wmax = ethin * E0 (i.e. 1e-8 * 1e9 for a 1EeV shower == 10)

  ########
  output = open("/corsikaqgp/steering/"+str(date2)+'_'+'EPOS.steering','w+')
  #output.write("DIRECT  /Corsika/showerLib/"+str(date2)+"_EPOS_\n")    
  output.write("DIRECT  ./particles/output/"+str(angle)+"deg_"+str(primary)+"prm_"+str(energy)+"GeV_"+str(date2)+"_EPOS_\n")     
  output.write("RUNNR   1                        run number\n")
  output.write("EVTNR   1                              number of first shower event\n")
  output.write("NSHOW   1                              number of showers to generate\n")
  output.write("THIN    "+str(thin)+" "+str(wmax)+" "+str(rmax)+"                thinning definition\n")
  output.write("THINH   10.  10.                      relative threshold and weight for hadron thinning\n")  
  output.write("PRMPAR  "+str(primary)+"                        primary particle code\n")


  output.write("THETAP  "+str(angle)+" "+str(angle)+"                       range of zenith angle (degree)\n")
  output.write("PHIP    0.  0.                       range of azimuth angle (degree)\n")

  output.write("SEED    "+str(rand1)+"   0   0                      seed for 1. random number sequence\n")
  output.write("SEED    "+str(rand2)+"   0   0                      seed for 2. random number sequence\n")
  output.write("SEED    "+str(rand3)+"   0   0                      seed for 2. random number sequence\n")
  ######
  output.write("ERANGE  "+str(energy)+" "+str(energy)+"     energy range of primary particle (GeV)\n")
  output.write("ESLOPE  -0                        slope of primary energy spectrum\n")
  #output.write("ESLOPE  -2.7                        slope of primary energy spectrum\n")
  output.write("OBSLEV  200.0E2                         observation level (in cm)\n")
  output.write("MAGNET  20.0   42.8                  magnetic field centr. Europe\n")


  ### EPOS ###
  output.write("EPOS    T   0\n")
  output.write("EPOSIG  T\n")
  output.write("EPOPAR input ../epos/epos.param        !initialization input file for epos\n")
  output.write("EPOPAR fname inics ../epos/epos.inics  !initialization input file for epos\n")
  output.write("EPOPAR fname iniev ../epos/epos.iniev  !initialization input file for epos\n")
  output.write("EPOPAR fname initl ../epos/epos.initl  !initialization input file for epos\n")
  output.write("EPOPAR fname inirj ../epos/epos.inirj  !initialization input file for epos\n")
  output.write("EPOPAR fname inihy ../epos/epos.ini1b  !initialization input file for epos\n")
  output.write("EPOPAR fname check none                !dummy output file for epos\n")
  output.write("EPOPAR fname histo none                !dummy output file for epos\n")
  output.write("EPOPAR fname data  none                !dummy output file for epos\n")
  output.write("EPOPAR fname copy  none                !dummy output file for epos\n")
  #####

  output.write("HADFLG  0  0  0  0  0  2               flags hadr.interact.&fragmentation\n")
  output.write("ECUTS   1.  1.  0.001  0.001          energy cuts for particles\n")
  output.write("MUADDI  F                              additional info for muons\n")
  output.write("MUMULT  T                              muon multiple scattering angle\n")
  output.write("ELMFLG  T   T                          em. interaction flags (NKG,EGS)\n")
  output.write("STEPFC  1.0                            mult. scattering step length fact.\n")
  output.write("RADNKG  1000.E2                         outer radius for NKG lat.dens.distr.\n")
  output.write("ARRANG  0.0                             rotation of array to north\n")
  output.write("*LONGI   T   5.  T  T                   longit.distr. & step size & fit & out\n")
  output.write("ECTMAP  1.E0                          cut on gamma factor for printout\n")
  output.write("MAXPRT  1                              max. number of printed events\n")

  ### cherenkov stuff

  output.write("CERARY  41 41 10000 10000 100 100   def. of Cherenkov aray grid (cm)\n")
  output.write("CWAVLG  200.  700.                Cherenkov wavelength band (nm)\n")
  output.write("CERSIZ  100.                      bunch size Cherenkov photons\n")
  output.write("CERFIL  T                         Cherenkov output to extra file\n")
  output.write("CSCAT   1  0. 0.                  scatter Cherenkov events (cm)\n")
  output.write("ATMOD   1                         atmospheric model selection\n")
  #####
  output.write("HILOW   100.                      transition energy between models (GeV)\n")
  output.write("DEBUG   F  6  F  999999999        debug flag, log. unit, delayed debug\n")


  output.write("PAROUT  T F                            suppress DAT file\n")
  output.write("EXIT\n")


  output.close()

  print 'Usage:'
  print './corsika74000Linux_EPOS_fluka < /corsikaqgp/steering/'+str(date2)+'_'+'EPOS.steering > /corsikaqgp/steeringEPOS_'+str(date2)+'.out'










#### if the file is not input ####
else:
  print "Usage: python steering_generatorEPOS.py energy thin wmax rmax"
  print "Energy in GeV"

  




