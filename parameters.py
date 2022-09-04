import numpy as np

Target = "CPU"  # CPU or GPU

if Target=="GPU": device = 0   # device number if multiple GPU devices are available

cupyfuse = True   # True, False : A decorator to speed up cupy operations

ProbType = "RBC"   # RBC, Hydro


#### Flow Parameters #############
if ProbType == "RBC":
    Ra = 1e4   # Rayleigh number
    Pr = 0.71  # Prandtl number
    Ro = 0.3   # Rossby number, can use Ro instead of Ta, but enabla Ta = Ra/(Ro**2*Pr) in the next line
    Ta = 0.0 #Ra/(Ro**2*Pr) # Taylor number, can use Ta directly. For no-rotation, ensure Ta=0 

if ProbType == "Hydro":
    nu = 0.01   # kinematic viscosity
    Omega = 0.0  # rotation rate
#########################################################


#### Boundary Conditions ##########################
# N: no-slip, P: periodic, S: free-slip,  LDC: Lid driven cavity
# PPN means periodic in x and y directions and no-slip in z directions

BCtype = "NNN"    # NNN, PPN, PPS, PPP, LDC

#####################################################


#######################################
#Change the aspect ration keeping Lz=1 always
Lx, Ly, Lz = 1.0, 1.0, 1.0    #Domain size

# Size index: 0 1 2 3  4  5  6  7   8   9   10   11   12   13    14
# Grid sizes: 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384
sInd = np.array([5, 5, 5])

GridType = "UUU"   # UUU, DDD, UUD

if GridType == "DDD": 
    betax = 1.2  # stretching in x
    betay = 1.2  # stretching in y
    betaz = 1.2  # stretching in z

if GridType == "UUD": 
    betaz = 1.2  # stretching in z
#########################################################


#### Initial Conditions ##########################

ICtype = 0    # 0-dead state (u, P, T=0, 0, 0)

#####################################################


#########Simulation Parameters #########################
restart = False   # True or False to restart or fresh start of the simulations

time = 0    # initial time for fresh start

dt = 0.01   # minimum value time-step in the simulation

tMax = 0.1  # maximum Simulation time

Cn = 0.5    # Courant number for CFL condition

opInt = 1 #int(0.01/dt)  # Number of iterations after which output must be printed to standard I/O

fwInt = 100  # solution File writing interval

rwInt = 5   # restart File writing interval

FpTolerance = 1.0e-6   # tolerance value in RBGS (predictor) solver

PoissonTolerance = 1.0e-6    # tolerance value in Poisson (multigrid) solver

gssorMG = 1.0     # SOR factor in multigrid solver

gssorWp = 1.0     # SOR factor in RBGS solver

gssorPp = 1.0     # SOR factor in Jacobi solver, the Jacobi solver is used only for code debugging

maxiteration = 1000    #M mximum iteration in RBGS
#################################################


###############Multigrid Parameters########################
VDepth = min(sInd) - 1   # Depth of each V-cycle in multigrid

preSm = 5   # Number of iterations during pre-smoothing

pstSm = 5   # Number of iterations during post-smoothing

vcCnt = 10  # Maximum V-cycle 
#############################################################


#############################
Volume = Lx*Ly*Lz   # volume of the domain

if ProbType == "RBC": nu, kappa, Omega = np.sqrt(Pr/Ra), 1.0/np.sqrt(Ra*Pr), np.sqrt((Ta*Pr)/Ra)

if (int(tMax/fwInt)>20):
    print("# Warning! File writing exceeding limit. New fwInt is set")
    fwInt = int(tMax/10)
