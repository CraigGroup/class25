#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 10:10:00
#SBATCH -p standard
#SBATCH -A phys_python
#SBATCH --job-name=MC_pi

#SBATCH --output=MC_pi_%A_%a.out
#SBATCH --error=MC_pi_%A_%a.error



python ./MC_pi.py 1000000 2


